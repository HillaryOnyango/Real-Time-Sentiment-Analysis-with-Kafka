Kafka Data Pipeline for Real-Time Sentiment Analysis
Project Overview
This project implements a robust data engineering pipeline for real-time ingestion, processing, filtering, and visualization of tweets from verified Twitter/X accounts using Apache Kafka. Designed with a focus on scalability, fault tolerance, and observability, the pipeline filters out negative sentiments, misleading content, and falsehoods, processes tweets for sentiment classification, and delivers insights via a Streamlit dashboard. The project serves as a reference for building production-grade data engineering workflows.
Key Features

Scalable Data Ingestion: Streams tweets from verified Twitter/X accounts into Kafka topics with fault-tolerant producers.
Content Filtering: Applies NLP-based filters to remove negative sentiments (VADER score < -0.05), misleading content, and falsehoods.
Stream Processing: Performs real-time sentiment analysis using TextBlob or VADER with Kafka consumers.
Persistent Storage: Stores processed data in PostgreSQL with optimized schema design.
Real-Time Visualization: Displays sentiment trends and filtering metrics on a Streamlit dashboard.
Containerized Deployment: Uses Docker and Docker Compose for reproducible, scalable deployments.
Monitoring and Observability: Integrates with Prometheus and Grafana for pipeline performance tracking (planned).

Data Engineering Focus

Scalability: Leverages Kafka’s partitioning and consumer groups for horizontal scaling.
Fault Tolerance: Ensures data durability with Kafka’s replication and retry mechanisms.
Observability: Includes logging and planned integration with Prometheus/Grafana for monitoring throughput and latency.
Modularity: Separates ingestion, filtering, processing, and storage into distinct modules for maintainability.
Documentation: Provides comprehensive guides for pipeline setup, monitoring, and scaling.

Technologies Used

Apache Kafka: Distributed streaming platform for high-throughput message brokering.
Python: Libraries include kafka-python (producer/consumer logic), TextBlob/VADER (sentiment analysis), scikit-learn/NLTK (content filtering).
Twitter/X API: Real-time tweet streaming from verified accounts.
PostgreSQL: Optimized storage for structured data.
Streamlit: Dashboard for real-time visualization.
Docker & Docker Compose: Containerization for consistent deployments.
Prometheus & Grafana (planned): Pipeline monitoring.

System Architecture
[Twitter/X API (Verified Accounts)] → [Kafka Topic: raw_tweets] → [Content Filter Consumer] → [Kafka Topic: filtered_tweets] → [Sentiment Analysis Consumer] → [PostgreSQL] → [Streamlit Dashboard]

The architecture emphasizes separation of concerns, with dedicated Kafka topics for raw and filtered data, enabling modular processing and scalability.
Prerequisites

Docker and Docker Compose installed.
Python 3.9+.
Twitter/X API credentials (Bearer Token or API Key/Secret).
PostgreSQL database (configured via Docker).

Installation

Clone the Repository:
git clone https://github.com/your-username/kafka-data-pipeline-sentiment.git
cd kafka-data-pipeline-sentiment


Set Up Environment Variables:Create a .env file in the project root:
TWITTER_BEARER_TOKEN=your_twitter_bearer_token
POSTGRES_USER=your_postgres_user
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_DB=sentiment_db
KAFKA_BOOTSTRAP_SERVERS=localhost:9092


Launch Docker Containers:
docker-compose up -d

This starts Kafka, Zookeeper, PostgreSQL, and the Streamlit dashboard.

Install Python Dependencies:
pip install -r requirements.txt



Usage

Run the Producer:Streams tweets to the raw_tweets Kafka topic:
python producer.py


Run the Content Filter Consumer:Filters tweets for negative sentiments and misinformation, producing to filtered_tweets:
python content_filter_consumer.py


Run the Sentiment Analysis Consumer:Processes filtered tweets and stores results in PostgreSQL:
python sentiment_consumer.py


Access the Streamlit Dashboard:Open http://localhost:8501 to view real-time sentiment trends and pipeline metrics.


Project Structure
├── producer.py               # Ingests tweets into Kafka
├── content_filter_consumer.py # Filters negative/misleading content
├── sentiment_consumer.py     # Processes sentiment and stores data
├── dashboard.py              # Streamlit visualization
├── docker-compose.yml        # Docker configuration
├── requirements.txt          # Python dependencies
├── docs/                     # Comprehensive pipeline documentation
└── README.md                 # This file

Documentation
The docs/ directory contains detailed documentation to support data engineering workflows:

Architecture Guide: Pipeline design, data flow, and scalability considerations.
API Documentation: Twitter/X API setup and rate limit handling.
Module Documentation: Code-level comments and module-specific READMEs.
Filtering Logic: Details on sentiment thresholds and misinformation detection.
Setup Guide: Instructions for deploying and scaling the pipeline.
Monitoring Guide: Planned setup for Prometheus/Grafana monitoring.

Data Engineering Metrics

Pipeline Latency: < 1 second from ingestion to visualization.
Throughput: > 1000 tweets/second with Kafka partitioning.
Filtering Accuracy: > 85% precision/recall for negative/misleading content.
Sentiment Accuracy: > 80% agreement with manual labels.
Fault Tolerance: Zero data loss with Kafka replication factor ≥ 2.
Scalability: Supports multiple consumer instances under load.

Future Work

Integrate advanced NLP models (e.g., BERT) for enhanced filtering.
Implement real-time alerts for pipeline anomalies or negative content spikes.
Develop a CI/CD pipeline with Kafka Connect for automated deployments.
Enhance observability with Prometheus/Grafana for real-time metrics.
Support multilingual content filtering for broader applicability.

Contributing
Contributions are welcome! Please submit issues or pull requests. Follow the setup guide and adhere to data engineering best practices.
License
This project is licensed under the MIT License. See the LICENSE file for details.
Author
Hillary Onyango