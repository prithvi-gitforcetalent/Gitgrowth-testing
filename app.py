import streamlit as st

# Page Configurations
st.set_page_config(
    page_title="Interactive Content Hypothesis",
    page_icon="💡",
    layout="centered"
)

# CSS for Styling
st.markdown(
    """
    <style>
    .main {
        background-color: #fcf7f2; /* Light cream background */
        font-family: 'Helvetica Neue', sans-serif;
    }
    .header {
        color: #004d33; /* Dark Green */
        text-align: center;
        font-weight: bold;
        font-size: 36px;
        margin-bottom: 20px;
    }
    .subheader {
        color: black; /* Black text */
        text-align: center;
        font-size: 18px;
        margin-top: -10px;
        margin-bottom: 40px;
        line-height: 1.6;
    }
    .question-box {
        margin-top: 30px;
        margin-bottom: 30px;
        text-align: center;
    }
    .question-text {
        font-size: 24px; /* Increased font size for better balance */
        font-weight: bold;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: white;
        color: #004d33;
        font-size: 20px; /* Slightly larger font size */
        font-weight: bold;
        border: 2px solid #004d33;
        border-radius: 30px; /* Slightly larger buttons */
        padding: 15px 35px; /* Increased padding for better proportions */
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    }
    .stButton>button:hover {
        background-color: #67a06f; /* Green-ish hover color */
        color: white;
        box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.2); /* More prominent shadow on hover */
    }
    .button-container {
        display: flex;
        justify-content: center;
        gap: 40px; /* Increased gap for better balance */
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header Section
st.markdown('<div class="header">Our Hypothesis</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="subheader">
        Static content marketing is no longer effective. Today's audiences demand 
        content that feels relevant, engaging, and personalized. Generic, one-size-fits-all 
        messaging fails to resonate, lacks depth, and doesn't provide enough value.<br><br>
        We believe that the future of content lies in 
        <strong>interactive, prospect-focused experiences</strong> that adapt to the unique needs 
        of each audience segment. These experiences drive meaningful engagement, build trust, 
        and deliver real value—far beyond what static content can achieve.
    </div>
    """,
    unsafe_allow_html=True
)

# Initialize session state to track progress
if "current_level" not in st.session_state:
    st.session_state.current_level = 0
    st.session_state.answers = []

# Questions and flow logic
questions = [
    {"question": "Do you believe in personalized marketing?"},
    {"question": "Do you think static content is outdated?"},
    {"question": "Do you want to explore interactive content tools?"},
    {"question": "Would you invest in interactive content solutions?"},
]

# Insights based on answers
def get_insight(answers):
    if answers == ["Yes", "Yes", "Yes", "Yes"]:
        return "You are highly aligned with interactive content strategies. Embracing these solutions can transform your engagement and conversions."
    elif answers.count("No") > 2:
        return "You may not yet see the full potential of personalization. Consider testing smaller strategies to evaluate their impact."
    else:
        return "You see the value of personalization but may need more confidence in ROI. Start small and iterate based on results."

# Render question dynamically
if st.session_state.current_level < len(questions):
    current_question = questions[st.session_state.current_level]

    st.markdown('<div class="question-box">', unsafe_allow_html=True)
    st.markdown(f'<div class="question-text">{current_question["question"]}</div>', unsafe_allow_html=True)

    # Buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes", key=f"yes_{st.session_state.current_level}"):
            st.session_state.answers.append("Yes")
            st.session_state.current_level += 1
            st.rerun()

    with col2:
        if st.button("No", key=f"no_{st.session_state.current_level}"):
            st.session_state.answers.append("No")
            st.session_state.current_level += 1
            st.rerun()
else:
    # Show the final insight
    insight = get_insight(st.session_state.answers)
    st.markdown("### Final Insight")
    st.success(insight)

    # Optional: Add a reset button
    if st.button("Start Over"):
        st.session_state.current_level = 0
        st.session_state.answers = []
        st.rerun()
