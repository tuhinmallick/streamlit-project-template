#!/bin/bash
# starts the traffic app and restarts it if crashed

while true; do
    [ -e stopme ] && break
    poetry run streamlit run app/dashboard.py
done
