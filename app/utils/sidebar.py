import streamlit as st


def sidebar_caption():
    """This is a demo of some shared sidebar elements.

    Reused this function to make sure we have the same sidebar elements if needed.
    """

    st.sidebar.header("Yay, this is a sidebar")
    st.sidebar.markdown("This is a markdown element in the **sidebar**.")


def filter_table_option():

    return st.sidebar.slider("Show how many", 0, 30, 1)
