import streamlit as st
from google import genai

# Page settings
st.set_page_config(
    page_title="AI StudySnap",
    page_icon="📚"
)

# Read Gemini API key
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

# Create Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

# Title
st.title("📚 AI StudySnap")
st.write("Upload your study material and let AI create easy notes.")

# Upload image
uploaded_file = st.file_uploader(
    "📸 Upload a study image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    st.image(
        uploaded_file,
        caption="Uploaded Study Material",
        use_container_width=True
    )

    if st.button("🤖 Generate AI Notes"):

        with st.spinner("AI is analyzing your study material..."):

            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=[
                        """Analyze this study material.

Create simple and easy-to-understand study notes.

Include:
1. Main topic
2. Important points
3. Key definitions
4. Important concepts
5. Short summary
6. 5 important exam questions

Use simple student-friendly language.""",
                        uploaded_file
                    ]
                )

                st.subheader("📝 AI Generated Notes")
                st.write(response.text)

            except Exception as e:
                st.error(f"Gemini error: {e}")