# Montgomery County Noise Complaint Data Engineering Project

## Problem Statement

This project aims to develop a robust data engineering solution for the Montgomery County Noise Complaint dataset. The dataset includes various reports of noise complaints, which are essential for analyzing disturbance patterns. The primary objectives are:

- **Improve Data Quality**: Enhance the accuracy and consistency of the data.
- **Efficient Data Storage and Retrieval**: Implement scalable data storage solutions and optimize data access.
- **Insightful Data Analysis**: Provide analytical capabilities to uncover trends and patterns in noise complaints across different times and regions.

The end goal is to offer refined and actionable insights to stakeholders. These insights will assist in improving community noise regulations and enforcement strategies.


## Data Description

This dataset contains 9,450 records of noise complaints from Montgomery County, Maryland, reported through 311 services or web forms. It includes the following fields:

- **Case Number**: Unique identifier for each noise complaint.
- **Case Open Date** & **Case Close Date**: The dates when the complaint was opened and resolved.
- **Case Year**: The year the complaint was reported.
- **Case Sub-Type**: The type of noise complaint.
- **Address**: The location of the noise incident, which may be anonymized.

# Data Processing Workflow Overview

## Project Structure

- **Dataset API**: Entry point for data, made accessible through an API, potentially containerized using Docker for deployment.
- **Cloud Storage**: Serves as a repository for raw data collected from the Dataset API.
- **Dataproc (Apache Spark)**: Utilizes managed Spark clusters for robust data processing.
- **BigQuery**: Acts as the data warehouse for storing processed data, enabling complex queries and analytics.
- **Looker Studio**: Final stage where data visualization and business intelligence are conducted.

The orchestration of these components is managed by MAGE, which coordinates the workflow from data ingestion to visualization.

![ProjectFlow](https://github.com/pgrarchives/DEzoomcamp2024/assets/112724112/3080160f-38fe-4a50-b4ae-074ad817099e)

## Data Flow

1. Data is ingested from the Dataset API.
2. Ingested data is stored in Cloud Storage.
3. Data is processed using Dataproc with Apache Spark.
4. Processed data is loaded into BigQuery for analysis.
5. Insights and reports are generated through Looker Studio.

This workflow enables a comprehensive approach to data engineering, from collection to actionable insights.

Dataset source: https://catalog.data.gov/dataset/noise-complaints 
