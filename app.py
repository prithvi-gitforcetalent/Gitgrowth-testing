import streamlit as st

# Page Configurations
st.set_page_config(
    page_title="Interactive Content Hypothesis",
    page_icon="💡",
    layout="wide",  # Change to wide for better mobile responsiveness
)

# CSS for Mobile-Friendly and Light Mode Styling
st.markdown(
    """
    <style>
    /* Force Light Mode */
    :root {
        color-scheme: light;
        --primary-color: #004d33;
        --background-color: #fcf7f2;
        --text-color: black;
    }
    
    /* Responsive Typography */
    @media (max-width: 600px) {
        .header {
            font-size: 28px !important;
        }
        .subheader {
            font-size: 16px !important;
        }
        .question-text {
            font-size: 20px !important;
        }
        .stButton>button {
            font-size: 16px !important;
            padding: 10px 25px !important;
        }
    }
    
    /* Base Styles */
    .main {
        background-color: #fcf7f2; /* Light cream background */
        font-family: 'Helvetica Neue', sans-serif;
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
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
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: white;
        color: #004d33;
        font-size: 20px;
        font-weight: bold;
        border: 2px solid #004d33;
        border-radius: 30px;
        padding: 15px 35px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        width: 100%; /* Full width for better mobile touch target */
        max-width: 300px; /* Limit max width */
        margin: 10px auto; /* Center buttons */
    }
    .stButton>button:hover {
        background-color: #67a06f;
        color: white;
        box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.2);
    }
    .button-container {
        display: flex;
        flex-direction: column; /* Stack buttons vertically on mobile */
        align-items: center;
        gap: 20px;
        margin-top: 20px;
    }
    
    /* Prevent dark mode overrides */
    body, .stApp {
        background-color: #fcf7f2 !important;
        color: black !important;
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
    if st.button("Yes", key=f"yes_{st.session_state.current_level}"):
        st.session_state.answers.append("Yes")
        st.session_state.current_level += 1
        st.rerun()

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
