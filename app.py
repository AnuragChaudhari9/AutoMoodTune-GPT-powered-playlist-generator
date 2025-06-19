import streamlit as st
import requests
from dotenv import load_dotenv
import os
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate

# Load environment variables
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
weather_key = os.getenv("WEATHER_API_KEY")

# -------- Functions --------

def detect_city_by_ip():
    try:
        res = requests.get("https://ipinfo.io/json")
        return res.json().get("city", "Unknown")
    except:
        return "Unknown"

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}&units=metric"
        res = requests.get(url)
        data = res.json()

        if res.status_code != 200:
            return f"Error fetching weather: {data.get('message', 'unknown error')}"

        desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return f"{desc}, {temp}°C in {city}"
    except:
        return "Could not fetch weather."

def generate_playlist(weather, activity, language):
    prompt = PromptTemplate(
    input_variables=["weather", "activity", "language"],
    template="""
You are a multilingual music expert. Based on the current weather, user activity, and their preferred language, generate a playlist of **exactly 10 songs**.

Weather: {weather}
Activity: {activity}
Language: {language}

Respond in this format:
1. Song name – Artist (if known): Short reason why this fits the context
"""
).format(weather=weather, activity=activity, language=language)

    llm = OpenAI(temperature=0.8, openai_api_key=openai_key)
    return llm(prompt)

# -------- Streamlit UI --------

st.set_page_config(page_title="AutoMoodTune", page_icon="🎧")
st.title("🎧 AutoMoodTune")
st.write("Get a GPT-curated playlist based on your weather, mood, and activity.")

# Auto-detect city and weather
city = detect_city_by_ip()
weather = get_weather(city)

st.info(f"📍 Detected location: **{city}**")
st.info(f"🌦️ Current weather: **{weather}**")

# Free-text user inputs
activity = st.text_input("What are you doing right now? (e.g., driving, cooking, vibing):")
language = st.text_input("Preferred language for songs (e.g., Hindi, English):")

# Generate button
if st.button("Generate Playlist") and activity and language:
    with st.spinner("🎶 Creating your custom playlist..."):
        playlist = generate_playlist(weather, activity, language)
        st.success("Here’s your GPT-powered playlist:")

        for line in playlist.strip().split("\n"):
            if line.strip():
                st.markdown(f"• {line}")