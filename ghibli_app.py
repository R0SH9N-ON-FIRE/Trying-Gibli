import streamlit as st
import requests

# Ghibli-style UI
def ghibli_style():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Comfortaa:wght@400;700&display=swap');

        html, body, [class*="css"]  {
            font-family: 'Comfortaa', cursive;
            background-color: #fdf6e3;
            color: #3c3c3c;
        }

        .stApp {
            background-image: url("https://i.imgur.com/8fKQw3E.jpg");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }

        h1, h2, h3 {
            color: #2e7d32;
        }

        .stSelectbox label {
            font-weight: bold;
            color: #5d4037;
        }
        </style>
    """, unsafe_allow_html=True)

ghibli_style()

# Title and intro
st.title("🌿✨ Studio Ghibli Film Explorer ✨🌿")
st.markdown("जादुई कहानियों की दुनिया में आपका स्वागत है — जहाँ भावनाएँ और कल्पना मिलती हैं।")

# Background music
st.markdown("""
    <audio autoplay loop>
        <source src="https://www.bensound.com/bensound-music/bensound-sunny.mp3" type="audio/mpeg">
    </audio>
""", unsafe_allow_html=True)

# API call
API_URL = "https://ghibliapi.vercel.app/films"

@st.cache_data
def get_films():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("डेटा लाने में समस्या हुई।")
        return []

films = get_films()

# Dropdown
film_titles = [film["title"] for film in films]
selected_title = st.selectbox("🎥 कोई फिल्म चुनें", film_titles)

# Show details
selected_film = next((film for film in films if film["title"] == selected_title), None)

if selected_film:
    st.image(selected_film["image"], width=300, caption=selected_film["title"])
    st.subheader(f"{selected_film['title']} ({selected_film['release_date']})")
    st.markdown(f"**निर्देशक:** {selected_film['director']}")
    st.markdown(f"**निर्माता:** {selected_film['producer']}")
    st.markdown(f"**समय:** {selected_film['running_time']} मिनट")
    st.markdown(f"**कहानी:** {selected_film['description']}")

# Footer
st.markdown("---")
st.markdown("❤️ रोशन द्वारा बनाया गया | Studio Ghibli से प्रेरित")
