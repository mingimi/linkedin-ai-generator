from google import genai
import streamlit as st

# Initialize Gemini Client
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

def generate_post(topic, industry, audience, tone, length, emojis, hashtags):

    prompt = f"""
You are one of the world's best LinkedIn content creators.

Generate ONE highly engaging LinkedIn post.

Topic: {topic}
Industry: {industry}
Audience: {audience}
Tone: {tone}
Length: {length}

Use Emojis: {emojis}
Use Hashtags: {hashtags}

Structure:
1. Attention-grabbing Hook
2. Valuable Content
3. Call To Action
4. Relevant Hashtags

Write naturally like a viral LinkedIn creator.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text