from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title = "The Three Amigos", page_icon = ":crescent_moon:", layout ="wide")

def load_lottieurl(url):
    r = requests.get(url)  #send an HTTP request to the target user
    if r.status_code != 200:
        return None
    return r.json() 

friend_lottie = load_lottieurl('https://assets2.lottiefiles.com/packages/lf20_ghg0pifn.json')
st.sidebar.header('Pranvi and Sidak~')
pranvi_image = Image.open('images\IMAGE4.jpg')
sidak_image = Image.open('images\image5.jpg')



with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.title('THE THREE AMIGOS!!')
    with right_column:
        st_lottie(friend_lottie, height = 200, key = "friend")

#using local css to hide streamlit branding
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

local_css('style\style2.css')

with st.container():
    st.write('---')
    st.header('PRANVI SHARMA :ribbon:')
    text_column, image_column, = st.columns((2,1))

    with text_column:
        st.write(
            """
            **Bonjour!!** :sparkles:
            - **Pranvi SHARMA**
            - currently pursuing BCOM hons.(in finance.) from **SRI AUROBINDO COLLEGE OF COMMERCE**
            - A **VIBRANT** and **INTELLIGENT** student
            - Very **GOAL ORIENTED** person.
            - **HOBBIES** -> **DANCING** :dancer:  and **Singing** :singer:
            - does work with **FULL DEDICATION!!**
            - loves socialising and exploring new places and people
            - Loves to eat(Sometimes too much! :laughing:)
            """
        )

    with image_column:
        st.image(pranvi_image, caption = "Pranvi Sharma")
with st.container():
    st.write('---')
    st.header('ARSHSIDAK SINGH :beer:')
    text_column, image_column, = st.columns((2,1))

    with text_column:
        st.write(
            """
            **ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ** :wave:
            - **Arshsidak Singh**
            - currently pursuing BCOM hons.(in finance.) from **SRI AUROBINDO COLLEGE OF COMMERCE**
            - A **CREATIVE** and **FUN LOVING** person.
            - loves being the center of attention
            - values **Friendship** more than **Family** :laughing:
            - **HOBBIES** -> **Sports** :trophy: **Music** :headphones: and Womanising :high_heel:
            - very **Hardworking** and **Organised Person!**
            - loves socialising and exploring new places and people
            - Loves to spend people's money :laughing:
            - **PHILANDRER**
            """
        )
    
    with image_column:
        st.image(sidak_image, caption = "Arshsidak Singh")




