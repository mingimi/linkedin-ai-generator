import google.generativeai as genai

genai.configure(api_key="AIzaSyC7kClOfl-9dvQY8lfxYAkidUYypgpk2Z8")
model = genai.GenerativeModel("gemini-2.5-flash")
def generate_post(topic, industry, audience, tone, length, emojis, hashtags):

    prompt = f"""
You are an expert LinkedIn Content Creator.

Generate ONE highly engaging LinkedIn post.

Topic: {topic}

Industry: {industry}

Audience: {audience}

Tone: {tone}

Length: {length}

Include Emojis: {emojis}

Include Hashtags: {hashtags}

Structure:
1. Attention-grabbing hook
2. Valuable insights
3. Call to action
4. Relevant hashtags
"""

    response = model.generate_content(prompt)

    return response.text