import streamlit as st
import pandas as pd
import oracledb
import joblib
from datetime import datetime
import os
from dotenv import load_dotenv
import altair as alt
import numpy as np

load_dotenv()

dsn = os.getenv("DB_DSN")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

@st.cache_data(ttl=600)
def load_data():
    connection = oracledb.connect(user=user, password=password, dsn=dsn)
    cursor = connection.cursor()
    query = """
        SELECT timestamp, sensor_id, hour, temp, humidity_air, moisture_soil, irrigated
        FROM irrigation_data
        ORDER BY timestamp
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0].lower() for desc in cursor.description]
    df = pd.DataFrame(rows, columns=columns)
    cursor.close()
    connection.close()
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

@st.cache_resource
def load_model():
    return joblib.load('data/irrigation_model.joblib')

def main():
    import sys
    st.title("Irrigation System Dashboard")

    df = load_data()
    model = load_model()

    st.sidebar.header("Filters")
    min_date = df['timestamp'].min()
    max_date = df['timestamp'].max()
    date_range = st.sidebar.date_input("Date range", [min_date, max_date], min_value=min_date, max_value=max_date)

    if len(date_range) != 2:
        st.error("Please select a start and end date.")
        return

    start_date, end_date = date_range
    mask = (df['timestamp'].dt.date >= start_date) & (df['timestamp'].dt.date <= end_date)
    filtered_df = df.loc[mask]

    st.subheader("Soil Moisture Over Time (All Sensors)")
    soil_chart = alt.Chart(filtered_df).mark_line().encode(
        x='timestamp:T',
        y='moisture_soil:Q',
        color='sensor_id:N',
        tooltip=['timestamp:T', 'sensor_id:N', 'moisture_soil:Q']
    ).interactive()
    st.altair_chart(soil_chart, use_container_width=True)

    st.subheader("Humidity Over Time (All Sensors)")
    humidity_chart = alt.Chart(filtered_df).mark_line().encode(
        x='timestamp:T',
        y='humidity_air:Q',
        color='sensor_id:N',
        tooltip=['timestamp:T', 'sensor_id:N', 'humidity_air:Q']
    ).interactive()
    st.altair_chart(humidity_chart, use_container_width=True)

    st.subheader("Temperature Over Time (All Sensors)")
    temp_chart = alt.Chart(filtered_df).mark_line().encode(
        x='timestamp:T',
        y='temp:Q',
        color='sensor_id:N',
        tooltip=['timestamp:T', 'sensor_id:N', 'temp:Q']
    ).interactive()
    st.altair_chart(temp_chart, use_container_width=True)

    st.subheader("Irrigation Prediction")
    features = filtered_df[['moisture_soil', 'humidity_air', 'temp', 'hour', 'sensor_id']]
    # Convert sensor_id to numeric for prediction, handle NaN by filling with 0
    sensor_id_extracted = features['sensor_id'].str.extract(r'(\\d+)')
    features['sensor_id_num'] = sensor_id_extracted.fillna(0).astype(int)
    features_for_pred = features[['moisture_soil', 'humidity_air', 'temp', 'hour', 'sensor_id_num']]
    predictions = model.predict(features_for_pred)
    filtered_df['predicted_irrigate'] = predictions

    # Add manual jitter for points
    jitter_strength = 0.1
    filtered_df['predicted_irrigate_jitter'] = filtered_df['predicted_irrigate'] + np.random.uniform(
        -jitter_strength, jitter_strength, size=len(filtered_df)
    )

    # Create a clearer chart using step lines and jittered points for better visibility
    base = alt.Chart(filtered_df).encode(
        x=alt.X('timestamp:T', title='Timestamp'),
        color='sensor_id:N'
    )

    line = base.mark_line(interpolate='step-after').encode(
        y=alt.Y('predicted_irrigate:Q', title='Irrigation Prediction')
    )

    points = base.mark_point(filled=True, size=60).encode(
        y=alt.Y('predicted_irrigate_jitter:Q', title='Irrigation Prediction (jittered)'),
        tooltip=['timestamp:T', 'sensor_id:N', 'predicted_irrigate:Q']
    )

    pred_chart = (line + points).interactive()
    st.altair_chart(pred_chart, use_container_width=True)

    st.write("Legend: 1 = Irrigate, 0 = Do not irrigate")

if __name__ == "__main__":
    main()
