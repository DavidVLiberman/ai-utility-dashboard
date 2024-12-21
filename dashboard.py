import streamlit as st
import pandas as pd
import requests
import random

# App title and sidebar navigation
st.title("AI Utility Dashboard 🌟")
st.sidebar.title("Navigation")
nav = st.sidebar.radio("Go to:", ["Home", "AI Chatbot", "Weather Insights", "Interactive Charts"])

# Home Page
if nav == "Home":
    st.write("Welcome to the **AI Utility Dashboard**! Navigate through the app using the sidebar.")
    st.image("https://source.unsplash.com/featured/?technology", caption="Explore and Learn!", use_column_width=True)

# AI Chatbot
elif nav == "AI Chatbot":
    st.subheader("AI Chatbot 🤖")
    user_input = st.text_input("Ask the AI anything:")
    if user_input:
        responses = ["That's fascinating!", "I'm here to help.", "Can you clarify?", "Let's dive deeper."]
        st.write("AI Response:", random.choice(responses))

# Weather Insights
elif nav == "Weather Insights":
    st.subheader("Weather Insights 🌦️")
    city = st.text_input("Enter your city:")
    if city:
        # Replace with your OpenWeatherMap API key
        api_key = "your_openweather_api_key"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url).json()
        if response.get("cod") != 200:
            st.write("City not found!")
        else:
            weather = response["weather"][0]["description"].title()
            temp = response["main"]["temp"]
            st.write(f"**Weather:** {weather}")
            st.write(f"**Temperature:** {temp}°C")

# Interactive Charts
elif nav == "Interactive Charts":
    st.subheader("Interactive Charts 📊")
    data = {"Category": ["A", "B", "C", "D"], "Values": [random.randint(10, 100) for _ in range(4)]}
    df = pd.DataFrame(data)
    st.write("Sample Data:")
    st.dataframe(df)
    st.bar_chart(df.set_index("Category"))
