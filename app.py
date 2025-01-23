import streamlit as st

# Page Configurations
st.set_page_config(
    page_title="B2B SaaS Content Marketing Hypothesis",  # Updated Page Title
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
        Sample Sample Sample. Sample Sample Sample Sample Sample Sample. Sample Sample Sample Sample Sample Sample Sample Sample Sample.<br><br>
        Sample Sample Sample Sample Sample Sample 
        <strong>Sample</strong> Sample Sample Sample Sample Sample Sample Sample Sample 
        Sample Sample Sample Sample Sample Sample Sample Sample Sample.
    </div>
    """,
    unsafe_allow_html=True
)

# Initialize session state to track progress
if "current_question" not in st.session_state:
    st.session_state.current_question = "root"
    st.session_state.answers = []

# Questions and branches
root_question = "Are you a growth focused founder or a SaaS product marketer?"

branch_yes = [
    "Sample Question - 1 (Yes Branch)",
    "Sample Question - 2 (Yes Branch)",
    "Sample Question - 3 (Yes Branch)",
]

branch_no = [
    "Sample Question - 1 (No Branch)",
    "Sample Question - 2 (No Branch)",
    "Sample Question - 3 (No Branch)",
]


# Insight function
def get_insight():
    return " ".join(["Sample"] * 100)


# Render questions dynamically
if st.session_state.current_question == "root":
    st.markdown('<div class="question-box">', unsafe_allow_html=True)
    st.markdown(f'<div class="question-text">{root_question}</div>', unsafe_allow_html=True)

    if st.button("Yes"):
        st.session_state.current_question = "yes_branch_0"
        st.rerun()

    if st.button("No"):
        st.session_state.current_question = "no_branch_0"
        st.rerun()

# Yes Branch
elif "yes_branch" in st.session_state.current_question:
    index = int(st.session_state.current_question.split("_")[-1])
    if index < len(branch_yes):
        st.markdown('<div class="question-box">', unsafe_allow_html=True)
        st.markdown(f'<div class="question-text">{branch_yes[index]}</div>', unsafe_allow_html=True)

        if st.button("Yes"):
            st.session_state.current_question = f"yes_branch_{index + 1}"
            st.rerun()

        if st.button("No"):
            st.session_state.current_question = f"yes_branch_{index + 1}"
            st.rerun()
    else:
        st.markdown("### Final Insight")
        st.success(get_insight())
        # Lead magnet
        email = st.text_input("Enter your email to stay updated:", placeholder="you@example.com")
        if st.button("Submit Email"):
            if email:
                st.success("Thank you! You'll be the first to know.")
            else:
                st.error("Please enter a valid email.")

# No Branch
elif "no_branch" in st.session_state.current_question:
    index = int(st.session_state.current_question.split("_")[-1])
    if index < len(branch_no):
        st.markdown('<div class="question-box">', unsafe_allow_html=True)
        st.markdown(f'<div class="question-text">{branch_no[index]}</div>', unsafe_allow_html=True)

        if st.button("Yes"):
            st.session_state.current_question = f"no_branch_{index + 1}"
            st.rerun()

        if st.button("No"):
            st.session_state.current_question = f"no_branch_{index + 1}"
            st.rerun()
    else:
        st.markdown("### Final Insight")
        st.success(get_insight())
        # Lead magnet
        email = st.text_input("Enter your email to stay updated:", placeholder="you@example.com")
        if st.button("Submit Email"):
            if email:
                st.success("Thank you! You'll be the first to know.")
            else:
                st.error("Please enter a valid email.")
