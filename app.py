import streamlit as st
import plotly.express as px

# Sidebar
st.sidebar.header('User Input Features')

# Load data
@st.cache_data
def load_data():
    conn = st.experimental_connection('mydb')
    complaint_types = conn.query("SELECT DISTINCT \"Complaint Type\" FROM incidents")
    return complaint_types

complaint_types = load_data()
selected_complaint = st.sidebar.selectbox('Complaint Type', complaint_types['Complaint Type'])

conn = st.experimental_connection('mydb')


# Main
st.header(f'Data for {selected_complaint}')

# Display summary statistics
st.subheader('Summary Statistics')
num_incidents = conn.query(f"SELECT COUNT(*) FROM incidents WHERE \"Complaint Type\" = '{selected_complaint}'")
st.write(f"Number of incidents: {num_incidents.values[0][0]}")
date_range = conn.query(f"SELECT MIN(\"Created Date\"), MAX(\"Created Date\") FROM incidents WHERE \"Complaint Type\" = '{selected_complaint}'")
st.write(f"Date range: {date_range.values[0][0]} to {date_range.values[0][1]}")

# Summary Graphs
st.header('Summary Graphs') 
# Emergency calls by date
calls_by_date = conn.query(f"SELECT date_trunc('day', \"Created Date\"::timestamp) AS date, COUNT(*) FROM incidents WHERE \"Complaint Type\" = '{selected_complaint}' GROUP BY date")

fig = px.histogram(calls_by_date, x='date', y='count', nbins=30, labels={'x':'Date', 'count':'Number of calls'}, title='Emergency calls by date', color_discrete_sequence=['darkblue'])
st.plotly_chart(fig)

# Emergency calls by hour of the day
calls_by_hour = conn.query(f"SELECT EXTRACT(HOUR FROM \"Created Date\"::timestamp) AS hour, COUNT(*) FROM incidents WHERE \"Complaint Type\" = '{selected_complaint}' GROUP BY hour")
fig = px.histogram(calls_by_hour, x='hour', y='count', nbins=24, labels={'x':'Hour of the day', 'count':'Number of calls'}, title='Emergency calls by hour of the day', color_discrete_sequence=['darkgreen'])
st.plotly_chart(fig)

# Incidents by Borough
incidents_by_borough = conn.query(f"SELECT \"Borough\", COUNT(*) FROM incidents WHERE \"Complaint Type\" = '{selected_complaint}' GROUP BY \"Borough\" ORDER BY count DESC LIMIT 10")
fig = px.bar(incidents_by_borough, x='Borough', y='count', labels={'x':'Borough', 'count':'Number of incidents'}, title='Top Boroughs by Number of Incidents', color='Borough', color_continuous_scale='Rainbow')
st.plotly_chart(fig)

# Incidents by Neighborhood for the selected complaint type
incidents_by_neighborhood = conn.query(f"""
SELECT n.neighborhood, i."Complaint Type", COUNT(i."Unique Key") AS incident_count
FROM incidents i
JOIN neighborhoods n ON ST_Contains(n.geom, ST_SetSRID(ST_MakePoint(i."Longitude"::float, i."Latitude"::float), 4326))
WHERE i."Complaint Type" = '{selected_complaint}'
GROUP BY n.neighborhood, i."Complaint Type"
ORDER BY incident_count DESC
LIMIT 10;
""")
fig = px.bar(incidents_by_neighborhood, x='neighborhood', y='incident_count', labels={'x':'Neighborhood', 'y':'Number of incidents'}, title=f'Top 10 Neighborhoods by Number of {selected_complaint} Incidents', color='neighborhood', color_continuous_scale='Rainbow')
st.plotly_chart(fig)


# Set the Mapbox access token
px.set_mapbox_access_token(st.secrets["mapbox"]["access_token"])

# Fetch the coordinates of the incidents
incidents_coordinates = conn.query(f"""
SELECT i."Latitude"::float, i."Longitude"::float
FROM incidents i
WHERE i."Complaint Type" = '{selected_complaint}';
""")

# Create a scatter plot on a map
fig = px.scatter_mapbox(incidents_coordinates, lat='Latitude', lon='Longitude', zoom=10, height=600,
                        color_discrete_sequence=["fuchsia"], size_max=15)

# Use Mapbox style
fig.update_layout(mapbox_style="carto-darkmatter")

# Display the map in the Streamlit app
st.plotly_chart(fig)