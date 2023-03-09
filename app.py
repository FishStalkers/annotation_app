import os
import streamlit as st
from PIL import Image
from streamlit_drawable_canvas import st_canvas

st.set_page_config(page_title="Annotation App", page_icon=":pencil2:", layout="wide", initial_sidebar_state="expanded")

def display_image_names():
    filelist=[]
    for root, dirs, files in os.walk("data/images"):
        for file in files:
            filename=os.path.join(root, file)
            #remove the prefix of the path
            filename=filename.replace("data/images/", "")
            filename= filename.replace(".jpg", "")
            filelist.append(filename)
            #remove DS_Store
            if filename == ".DS_Store":
                filelist.remove(filename)
    
    def update_active_image(i):
        st.session_state.active_image = i
        print(st.session_state.active_image)
        #st.image("data/images/"+st.session_state.active_image + '.jpg', use_column_width=True)

    with st.sidebar:
        for i in filelist:
            st.button(i, on_click = update_active_image, args = (i,))

def display_utils():
    remove_top_space_style = """
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """
    
    st.markdown(remove_top_space_style, unsafe_allow_html=True)
    
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

def display_home():
    st.markdown("<h1 style='text-align: center; color: black;'>Annotation App</h1>", unsafe_allow_html=True)
    if "active_image" not in st.session_state:
        st.session_state["active_image"] = ""
        
    if st.session_state["active_image"] != "":
        #st.image("data/images/"+st.session_state["active_image"] + '.jpg', use_column_width=True)
        img = Image.open("data/images/"+st.session_state["active_image"] + ".jpg")
        #st.image(img, use_column_width=True)
        img_size = img.size
        st.write(st.session_state.active_image)
        canvas = st_canvas(width=img_size[0]*0.7, height=img_size[1]*0.5,
                            background_image=img,
                            stroke_width=3, stroke_color= "#b6d130",
                            drawing_mode = "polygon", fill_color = "#00000000")

        st.write(canvas.json_data)
    display_utils()
    #st.session_state["active_image"] = ""
    display_image_names()

display_home()



