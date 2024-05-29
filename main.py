import streamlit as st
from streamlit_option_menu import option_menu
import Details, Events, Coffee, Home,About


st.set_page_config(
    page_title= "YCC Finance",
)

class Multiapp:

    def __init__(self):
        self.apps=[]
    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })
    def run():
        hide_st_style="""
    <style>
       header{
          visibility: hidden;
       }
       .block-container{
          padding-top:0px;
       }
    </style>
        """
        st.markdown(hide_st_style,unsafe_allow_html=True)

        with st.sidebar:
           
            app= option_menu(
                menu_title='YCC',
                options=['Home','Details','Events', 'Coffee Machine','About'],
                menu_icon='house-fill',
                default_index=0,
                styles={
                    "container":{"padding":"100px","background_color":"red","height":"100%",},
                    "icon":{"color":"white","font-size":"20px"},
                    "nav-link": {"color":"white","font-size":"20px","text-align":"left","margin":"0px","--hover-color":"#080558"},
                    "nav-link-selected":{"background-color":"#02a21"},

                }
            
            )
            
            st.markdown("""**Note:** For the best experience, please view this dashboard in **landscape** mode on **mobile devices**. ***Thank you!***""")
        if  app=="Home":
            Home.app()
        if  app=="Details":
            Details.app()
        if  app=="Events":
            Events.app()
        if  app=="Coffee Machine":
            Coffee.app()
        if app=="About":
            About.app()
        
run()
            
            
