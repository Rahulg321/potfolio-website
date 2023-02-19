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

rakhi_lottie = load_lottieurl('https://assets3.lottiefiles.com/packages/lf20_kjvc9btg.json')
st.sidebar.header('Gayatri and Vasudha~')
vasudha_image = Image.open('images\image6.jpg')
gayatri_image = Image.open('images\image7.jpg')



with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.title('My SISTERS!!')
    with right_column:
        st_lottie(rakhi_lottie, height = 200, key = "sister")

#using local css to hide streamlit branding
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

local_css('style\style2.css')

with st.container():
    st.write('---')
    st.header('Gayatri Gupta :zap:')
    text_column, image_column, = st.columns((2,1))

    with text_column:
        st.write(
            """
            **Hello!!** :wave:
            - **Gayatri Gupta**
            - completed BCOM hons.(in finance.) from **Kcw Ludhiana**
            - completed LLB from **PU CHANDIGARH**
            - A **VIBRANT**, **SMART** and **INTELLIGENT** student
            - Very **GOAL ORIENTED**.
            - **HOBBIES** -> **RUNNING** :runner:  and **COOKING** :yum:
            - does work with **FULL DEDICATION!!**
            - has participated in many social and cultural events
            - Loves to cook espically **PASTA** and **Grilled Sandwiches** 

            ### CONNECT WITH HER ON [LINKEDIN]('https://www.linkedin.com/in/advocate-gayatri-gupta-377060233/)
            """
        )

    with image_column:
        st.image(gayatri_image, caption = "Gayatri Gupta")
with st.container():
    st.write('---')
    st.header('VASUDHA MANGLA :snowflake:')
    text_column, image_column, = st.columns((2,1))

    with text_column:
        st.write(
            """
            **HEY!** :open_hands:
            - **Vasudha Mangla**
            - completed P.hd in **Computer Science**
            - very **SMART** **FUN** and **CREATIVE** person.
            - loves building and trying new things
            - values **Family** more than anything else.
            - **HOBBIES** -> **Travelling** :innocent:
            - very **Hardworking**
            - loves socialising and meeting new people
            """
        )
    
    with image_column:
        st.image(vasudha_image, caption = "Vasudha Mangla")





