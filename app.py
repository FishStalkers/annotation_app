import os
import streamlit as st

st.set_page_config(page_title="Annotation App", page_icon=":pencil2:", layout="wide", initial_sidebar_state="collapsed")

def display_home():
    st.markdown("<h1 style='text-align: center; color: black;'>Annotation App</h1>", unsafe_allow_html=True)
    display_utils()
    display_image_names()

    #display the correct image in the main window
    if st.session_state.active_image != "":
        st.image("data/images/"+st.session_state.active_image, use_column_width=True)
        st.write(st.session_state.active_image) #TODO: UNTESTED

def display_image_names():
    st.session_state["active_image"] = ""
    filelist=[]
    for root, dirs, files in os.walk("data/images"):
        for file in files:
            filename=os.path.join(root, file)
            #remove the prefix of the path
            filename=filename.replace("data/images/", "")
            filelist.append(filename)
            #remove DS_Store
            if filename == ".DS_Store":
                filelist.remove(filename)
    
    def update_active_image(i):
        st.session_state.active_image = i
        print(st.session_state.active_image)
        st.write(st.session_state.active_image)

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

display_home()
