import google.generativeai as genai

# Paste your Gemini API Key here temporarily
genai.configure(api_key="AQ.Ab8RN6IGGHPQIfkhIhbgz3S99-WQKHNycIS6q7uAAmJIg2JAmg")

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_post(topic, industry, audience, tone, length, emojis, hashtags):

    prompt = f"""
You are one of the world's best LinkedIn content creators.

Generate ONE highly engaging LinkedIn post.

Requirements:

Topic: {topic}

Industry: {industry}

Audience: {audience}

Tone: {tone}

Length: {length}

Use Emojis: {emojis}

Use Hashtags: {hashtags}

Output Format:

🚀 Hook

Body

Key Takeaways

Call To Action

Relevant Hashtags

Make it look like a viral LinkedIn post.
"""

    response = model.generate_content(prompt)

    return response.text