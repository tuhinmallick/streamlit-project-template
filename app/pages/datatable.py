import streamlit as st
from utils.page import Page
import plotly_express as px
from utils.sidebar import filter_table_option


class DataTable(Page):
    def __init__(self, data, **kwargs):
        name = "Table"
        super().__init__(name, data, **kwargs)


    def content(self):

        st.markdown("## Data Table")

        num_records = filter_table_option()

        fig = px.line(self.data["base"].head(num_records), x="datetime", y="values")
        st.plotly_chart(fig, use_container_width=True)

        st.table(self.data["base"].head(num_records))