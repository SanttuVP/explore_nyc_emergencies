# Explore NYC 311 Service Requests

This repository contains a Streamlit application for analyzing 311 service requests in New York City. This project was created as a

## Introduction

This experimental application provides an interactive way to explore the 311 service requests in New York City. Users can select a complaint type of interest and the application will generate various summary statistics and visualizations, including a interactive map of the incident locations. The application is built using Python, Streamlit, PostgreSQL, and Plotly.

This project was created as an experiment using "prompt engineering" for creating useful data discovery applications through conversational AI as a person who do not write code as their primary profession.

## Data Sources

The data used in this application comes from two main sources:

1. **311 Service Requests from 2010 to Present**: This dataset provides information about the service requests made to 311 in New York City from 2010 to the present. It is made available under the [NYC Open Data Policy and Terms of Use](https://opendata.cityofnewyork.us/overview/#termsofuse). It can be downloaded from [NYC Open Data](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9).

2. **NYC Neighborhoods**: This dataset provides geographical information about the neighborhoods in New York City. It is licensed under the Open Data Commons Attribution License and can be downloaded from [Beta NYC](https://data.beta.nyc/dataset/pediacities-nyc-neighborhoods).


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
