import streamlit as st
from utils.page import Page


class About(Page):
    """About page"""

    def __init__(self, data, **kwargs):
        name = "About"
        super().__init__(name, data, **kwargs)

    def content(self):

        st.markdown("This is my about page.")
