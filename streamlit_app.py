import streamlit as st
from generator import generate_post
# -------------------- Page Config --------------------
st.set_page_config(
    page_title="LinkedIn AI Content Generator",
    page_icon="🚀",
    layout="wide"
)

# -------------------- Header --------------------
st.title("🚀 LinkedIn AI Content Generator")
st.markdown("Generate professional LinkedIn posts using Generative AI.")

# -------------------- Sidebar --------------------
st.sidebar.title("⚙️ Settings")

tone = st.sidebar.selectbox(
    "Select Tone",
    [
        "Professional",
        "Casual",
        "Inspirational",
        "Storytelling",
        "Motivational"
    ]
)

length = st.sidebar.selectbox(
    "Post Length",
    [
        "Short",
        "Medium",
        "Long"
    ]
)

emoji = st.sidebar.checkbox("Include Emojis", value=True)
hashtags = st.sidebar.checkbox("Include Hashtags", value=True)

# -------------------- Main Inputs --------------------
topic = st.text_input("📌 Topic")

industry = st.selectbox(
    "Industry",
    [
        "Artificial Intelligence",
        "Banking",
        "Marketing",
        "Finance",
        "Healthcare",
        "Education",
        "Technology"
    ]
)

audience = st.text_input("🎯 Target Audience")

# -------------------- Generate Button --------------------
if st.button("✨ Generate LinkedIn Post"):

    if topic == "":
        st.warning("Please enter a topic.")

    else:

        with st.spinner("Generating your LinkedIn post..."):

            post = generate_post(
                topic,
                industry,
                audience,
                tone,
                length,
                emoji,
                hashtags
            )

        st.success("Post Generated!")

        st.subheader("Generated LinkedIn Post")

        st.write(post)

        st.download_button(
            "📥 Download Post",
            data=post,
            file_name="linkedin_post.txt",
            mime="text/plain"
        )