from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title = "My webpage", page_icon = ":smiling_imp:", layout ="wide")

st.sidebar.success('Select a person or project above!')

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

local_css('style\style.css')

def load_lottieurl(url):
    r = requests.get(url)  #send an HTTP request to the target user
    if r.status_code != 200:
        return None
    return r.json() 

lottie_coding = load_lottieurl('https://assets2.lottiefiles.com/packages/lf20_tno6cg2w.json')
lottie_ai = load_lottieurl('https://assets4.lottiefiles.com/private_files/lf30_m075yjya.json')
family_image = Image.open('C:/Users/Lenovo/OneDrive/Desktop/stream_website1/images/image1.jpg') 
family_image = family_image.resize((400,600))
three_amigos = Image.open('images/image3.jpg')
three_amigos = three_amigos.resize((600,400))
my_image = Image.open('C:/Users/Lenovo/OneDrive/Desktop/stream_website1/images/image2.jpg')
my_image_1 = my_image.resize((400,400))


# --------------------HEADER-------------------
with st.container():
    text_column, image_column = st.columns(2)
    with text_column:
        st.subheader("Hi my name is Rahul Gupta :wave:")
        st.title("Self Taught Developer :panda_face:")
        st.write("I am from India")
        st.write("AND I am currently learning to code")
    with image_column:
        st.image(my_image_1, caption = 'Me Myself and I')

#what do i do
with st.container():
    st.write("---")
    left_column,right_column = st.columns(2)

    with left_column:
        st.header("About Me!")
        st.write(
            """
        - I am currently an undergraduate CSE student:
        - My preferred domains are MachineLearning, AI and Backend Web Development.
        - Also I have been playing professional badminton from the last 10 years.
        - I own a ps4 and spend a considerable chunk of time playing it.
        - When it comes to reading I prefer real books as opposed to using Kindle :exclamation:

        """
        
        )
        st.write("Follow my social media accounts below for more information! :smile:")
        st.write("[Github:- >](https://github.com/Rahulg321)")
        st.write("[Twitter:- >](https://twitter.com/rg5353070)")
        st.write("[LinkedIn:- >](https://www.linkedin.com/in/rahul-gupta-86194a213/)")

    with right_column:
        st_lottie(lottie_coding, height = 300, key = "coding")


with st.container():
    st.write('---')
    st.header('My Work!')
    image_column, text_column = st.columns((1,2))

    with image_column:
        st_lottie(lottie_ai, height = 300, key ="ai")
    
    with text_column:
        st.write(
            """
            **Meet Me!** 
            - As of now I am currently praticising Learning **ML** and **AI**.
            - Also I am interested in Backend by Learning **DJANGO**.
            - Preferred Languages are **SQL**, **PYTHON** and **C**.
            """
        )
with st.container():
    st.write('---')
    st.header('Family!')
    image_column, text_column = st.columns((1,2))

    with image_column:
        st.image(family_image, caption = 'MySisters!')
    
    with text_column:
        st.write(
            """
            **My family** : Meet Gayatri and Vasudha.

            - Gaytari is currently a lawyer working in a Law Firm in Delhi.
            - Vasudha is a full time Web Developer and a housewife living in Patiala.

            ### Want to learn more about them?
            - **See their page in the navigation section on the left**

            """
        )

with st.container():
    st.write('---')
    st.header('Friends!')
    image_column, text_column = st.columns((1,2))

    with image_column:
        st.image(three_amigos, caption = 'Having a Drink Together')
    
    with text_column:
        st.write(
            """
            **My friends**: Meet Sidak and Pranvi!
            - Pranvi is a Management Student studying Bcom in Aurobindo and working in a Startup
            - Sidak is a Management Student studying Bcom in AuroBindo and working in many social groups

            ### Learn more About Them!
            **Using the link in the navigation section on the left!**
        

            """
        )


#Contact With me

with st.container():
    st.write('---')
    st.header('Get In Touch With Me!')
    st.write('ASK A QUESTION!!!')

    contact_form = """
    <form action="https://formsubmit.co/rg5353070@gmail.com" method="POST">
    
    <input type = 'hidden' name = "_captcha" value = "false">
    <label>Enter your Name!</label>
    <input type ='text' name = 'name' placeholder ="Your Name" required>
    <label>Enter your Email Address!</label>
    <input type ='email' name = 'email' placeholder = "Your Email" required>
    <label>Your Question Here!</label>
    <textarea name  = 'Message' placeholder = "Your question?" required> </textarea>
    <button type ="submit"> Send </button>
    </form>
    
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html = True)
    with right_column:
        st.empty()

    





















