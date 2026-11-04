
import streamlit as st
from PIL import Image
import random

st.set_page_config(
    page_title="REEF AI",
    page_icon="🪸",
    layout="wide"
)

# CUSTOM DESIGN
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg,#061D2B,#0A4350);
    color: white;
}
section[data-testid="stSidebar"] {
    background-color: #082F40;
}
h1,h2,h3,p,label {
    color: white !important;
}
.hero {
    background: linear-gradient(120deg,#087F83,#0BB5A0);
    padding: 35px;
    border-radius: 20px;
    margin-bottom: 25px;
}
.result {
    background: #104B50;
    border: 1px solid #36BFA5;
    border-radius: 18px;
    padding: 25px;
    text-align: center;
}
div.stButton > button {
    background-color: #0AB39F;
    color: white;
    border-radius: 10px;
    border: none;
    width: 100%;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# SIDEBAR
st.sidebar.title("🪸 REEF AI")
st.sidebar.caption("UNDERWATER INTELLIGENCE")

page = st.sidebar.radio(
    "NAVIGATION",
    ["Home", "Classify Coral", "Coral Information", "About Project"]
)

st.sidebar.markdown("---")
st.sidebar.success("Interface is running")

# HOME
if page == "Home":

    st.markdown("""
    <div class="hero">
        <h1>🌊 Explore the Coral World</h1>
        <p>Discover coral reef classification
        through Artificial Intelligence.</p>
    </div>
    """, unsafe_allow_html=True)

    st.title("Welcome to REEF AI")

    st.write("""
    REEF AI is a coral reef image classification
    interface designed to demonstrate how
    Artificial Intelligence can help identify
    different coral conditions.
    """)

    c1,c2,c3 = st.columns(3)

    c1.info("📤 Upload Coral Images")
    c2.info("🤖 Demonstrate AI Classification")
    c3.info("📊 View Classification Results")

    st.subheader("Our Mission")
    st.write("""
    To spread awareness about coral reefs
    and the importance of protecting marine
    ecosystems.
    """)

# CLASSIFICATION
elif page == "Classify Coral":

    st.markdown("""
    <div class="hero">
        <h1>🔬 Coral Classification</h1>
        <p>Upload an image to explore the classifier.</p>
    </div>
    """, unsafe_allow_html=True)

    uploaded = st.file_uploader(
        "Upload a Coral Reef Image",
        type=["jpg","jpeg","png"]
    )

    if uploaded:

        image = Image.open(uploaded).convert("RGB")

        st.image(
            image,
            caption="Uploaded Coral Image",
            width=450
        )

        st.success("Image uploaded successfully!")

        if st.button("🔍 Classify Image"):

            categories = [
                "Healthy Coral",
                "Bleached Coral",
                "Dead Coral",
                "Diseased Coral"
            ]

            # DEMONSTRATION ONLY
            prediction = random.choice(categories)
            confidence = random.randint(85, 98)

            st.markdown("---")
            st.markdown("## Classification Result")

            st.markdown(f"""
            <div class="result">
                <h3>Predicted Category</h3>
                <h1>🪸 {prediction}</h1>
                <h3>Demo Confidence: {confidence}%</h3>
            </div>
            """, unsafe_allow_html=True)

            st.warning(
                "Demonstration result only. "
                "No trained AI model is connected."
            )

# INFORMATION
elif page == "Coral Information":

    st.markdown("""
    <div class="hero">
        <h1>🌊 Coral Reef Information</h1>
        <p>Learn about different coral conditions.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("🟢 Healthy Coral"):
        st.write("Healthy corals support marine biodiversity.")

    with st.expander("🟡 Bleached Coral"):
        st.write("Bleaching occurs when corals lose their symbiotic algae.")

    with st.expander("⚫ Dead Coral"):
        st.write("Dead coral has lost its living coral tissue.")

    with st.expander("🔴 Diseased Coral"):
        st.write("Coral diseases can damage living coral tissue.")

# ABOUT
elif page == "About Project":

    st.markdown("""
    <div class="hero">
        <h1>📘 About Our Project</h1>
        <p>Coral Reef Classification Interface</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Project Objective")

    st.write("""
    This project demonstrates a user-friendly
    interface for coral reef image classification.

    It illustrates how image upload and
    classification results can be presented
    in an Artificial Intelligence application.
    """)

    st.subheader("Technologies Used")

    st.write("""
    - Python
    - Streamlit
    - Google Colab
    - Pillow
    """)

    st.subheader("Classification Categories")

    st.write("""
    1. Healthy Coral
    2. Bleached Coral
    3. Dead Coral
    4. Diseased Coral
    """)
