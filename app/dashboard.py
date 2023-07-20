"""Main module for the streamlit app"""
import numpy as np
import pandas as pd
import streamlit as st
from pages.about import About
from pages.datatable import DataTable
from utils.sidebar import sidebar_caption

# Config the whole app
st.set_page_config(
    page_title="A Dashboard Template",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
)


@st.cache()
def fake_data():
    """some fake data"""

    dt = pd.date_range("2021-01-01", "2021-03-01")
    df = pd.DataFrame(
        {"datetime": dt, "values": np.random.randint(0, 10, size=len(dt))}
    )

    return df


def main():
    """A streamlit app template"""

    st.sidebar.title("Tools")

    pages = {"Table": DataTable, "About": About}

    # Select pages
    # Use dropdown if you prefer
    selection = st.sidebar.radio("Pages", list(pages.keys()))
    sidebar_caption()

    page = pages[selection]

    data = {"base": fake_data()}

    with st.spinner(f"Loading Page {selection} ..."):
        page_runner = page(data)
        page_runner()


if __name__ == "__main__":
    main()
