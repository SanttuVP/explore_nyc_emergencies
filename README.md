# Explore NYC 311 Service Requests

This repository contains a Streamlit application for analyzing 311 service requests in New York City. This project was created as a

## Introduction

This experimental application provides an interactive way to explore the 311 service requests in New York City. Users can select a complaint type of interest and the application will generate various summary statistics and visualizations, including a interactive map of the incident locations. The application is built using Python, Streamlit, PostgreSQL, and Plotly.

This project was created as an experiment using "prompt engineering" for creating useful data discovery applications through conversational AI as a person who do not write code as their primary profession.


## Installation

1. Clone this repository.
2. Install the required Python packages using pip:
    ```bash
    pip install -r requirements.txt
    ```
3. You will also need to have PostgreSQL installed and running on your machine / remote server / hosted DB.

## Usage

1. Set up your PostgreSQL database and import the necessary data.
2. Set your Mapbox access token in `secrets.toml`.
3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
4. Open your web browser and visit `http://localhost:8501`.


## License

[MIT](https://choosealicense.com/licenses/mit/)
