import streamlit as st
from sqlalchemy import create_engine, text
from config import POSTGRES_URL

engine = create_engine(POSTGRES_URL)

def get_data():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT sentiment, COUNT(*) FROM tweets GROUP BY sentiment"))
        return dict(result.fetchall())

st.title("📊 Real-Time Sentiment Dashboard")

data = get_data()
st.bar_chart(data)
