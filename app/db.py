from sqlalchemy import create_engine, text
from config import POSTGRES_URL

engine = create_engine(POSTGRES_URL)

def create_tweets_table():
    with engine.begin() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS tweets (
                id SERIAL PRIMARY KEY,
                tweet TEXT NOT NULL,
                sentiment VARCHAR(50),
                polarity FLOAT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """))

def save_tweet(tweet, sentiment, polarity):
    with engine.begin() as conn:
        conn.execute(
            text("INSERT INTO tweets (tweet, sentiment, polarity) VALUES (:t, :s, :p)"),
            {"t": tweet, "s": sentiment, "p": polarity}
        )

# Create the table (run this once)
create_tweets_table()