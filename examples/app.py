import streamlit as st

from pr_streamlit_template import streamlit_custom_page

streamlit_custom_page()

st.sidebar.title("Sidebar")
st.sidebar.markdown("This is a sidebar")
st.sidebar.checkbox("Checkbox", False)
st.sidebar.radio("Radio", ["A", "B", "C"])
