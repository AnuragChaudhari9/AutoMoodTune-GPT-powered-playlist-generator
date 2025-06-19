# 🎧 AutoMoodTune

**GPT-powered playlist generator** that creates music recommendations based on your **real-time weather**, **current activity**, and **preferred language**.

> Powered by **LangChain**, **OpenAI GPT**, **OpenWeatherMap**, and **Streamlit**.

---

## 🌟 Features

- 🌍 Auto-detects your current location via IP
- 🌦️ Fetches real-time weather (temperature, rain, clouds, etc.)
- 🧘‍♀️ Accepts free-text activity input (e.g., working out, driving, reading)
- 🗣️ Generates playlists in your preferred language (e.g., Hindi, Tamil, English)
- 🧠 Uses GPT to explain why each song fits your vibe
- ⚡ Built with LangChain, OpenAI, and Streamlit

---

## 📷 Demo Screenshot

![AutoMoodTune Screenshot](https://github.com/user-attachments/assets/d44bec40-be4d-4271-a3be-eacc0e1e15e4)

---

## 🚀 Quick Start

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/AutoMoodTune.git
cd AutoMoodTune
```
### 2. Create a `.env` File

Create a `.env` file in the root directory with the following:

```env
OPENAI_API_KEY=your_openai_key_here
WEATHER_API_KEY=your_openweathermap_key_here
```
### 3. Install Requirements
```
pip install -r requirements.txt
```
### 4. Run the App
```
streamlit run app.py
```
## 🧠 Tech Stack

| Tool           | Purpose                        |
|----------------|--------------------------------|
| OpenAI         | GPT-based playlist reasoning   |
| LangChain      | Prompt orchestration           |
| Streamlit      | User interface                 |
| OpenWeatherMap | Real-time weather API          |
| IPInfo.io      | Location auto-detection        |
## 📝 Example Usage
![Screenshot (191)](https://github.com/user-attachments/assets/e2a7c05f-a29e-4047-80e4-e98b6f046429)

