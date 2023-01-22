"""Main module for the streamlit app"""
import os

import numpy as np
import pandas as pd
import streamlit as st
from loguru import logger

from pages.about import About
from pages.datatable import DataTable
from utils.sidebar import sidebar_caption

# Config the whole app
st.set_page_config(
    page_title="A Dashboard Template",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)


@st.cache()
def fake_data():
    """some fake data"""

    dt = pd.date_range("2021-01-01", "2021-03-01")
    return pd.DataFrame(
        {"datetime": dt, "values": np.random.randint(0, 10, size=len(dt))}
    )


def main():
    """A streamlit app template"""

    st.sidebar.title("Tools")

    PAGES = {
        "Table": DataTable,
        "About": About
    }

    # Select pages
    # Use dropdown if you prefer
    selection = st.sidebar.radio("Pages", list(PAGES.keys()))
    sidebar_caption()

    page = PAGES[selection]

    DATA = {"base": fake_data()}

    with st.spinner(f"Loading Page {selection} ..."):
        page = page(DATA)
        page()


if __name__ == "__main__":
    main()
