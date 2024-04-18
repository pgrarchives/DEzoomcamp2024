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

Dataset source: https://catalog.data.gov/dataset/noise-complaints 

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
![Screenshot 2024-04-17 195418](https://github.com/pgrarchives/DEzoomcamp2024/assets/112724112/484d9302-69ce-475a-8d33-6a255ca997d7)
![Screenshot 2024-04-17 195509](https://github.com/pgrarchives/DEzoomcamp2024/assets/112724112/978dfa29-5161-4d51-9065-1f66a032ddc0)
![Screenshot 2024-04-17 195551](https://github.com/pgrarchives/DEzoomcamp2024/assets/112724112/8673fdab-ddb1-427c-96ba-66f715f155ac)
![image](https://github.com/pgrarchives/DEzoomcamp2024/assets/112724112/d2908c4c-2ac2-45a2-9ec4-65443bd7675f)
![image](https://github.com/pgrarchives/DEzoomcamp2024/assets/112724112/b92def94-1045-4adb-8431-f0e3bc0defef)

# Insights from Noise Complaints Data in Montgomery County

![Screenshot 2024-04-17 205348](https://github.com/pgrarchives/DEzoomcamp2024/assets/112724112/f9a231b8-2b45-4d13-9dc9-175b776d3c5b)
## Key Findings

- **Industrial vs. Residential**: Industrial/commercial noise complaints slightly outnumber those from residential sources.
- **Complaint Trends**: The total number of complaints per year shows variability, indicating potential patterns or seasonal trends that merit further investigation.
- **Complaint Diversity**: A range of noise complaint types exists, with several sub-categories like equipment noise and multi-tenant disturbances.
- **Resolution Timeframes**: The dataset includes average resolution times, which vary across complaint types and can inform response efficiency analysis.

These insights can guide local authorities in noise management and policy-making.

# Project Setup Guide for Noise Complaints Analysis

## Prerequisites
Before you begin, ensure you have a Google Cloud Platform (GCP) account and have generated a service account key for accessing various Google services like MAGE and BigQuery.

## Steps for Reproducibility

1. **Clone the Repository**: Clone the GitHub repo to your local machine to get started with the analysis.
2. **GCP Account and Service Keys**: Create a GCP account if you haven't already and download the service account keys. Place these keys in the designated project folder.
3. **Environment Setup**: Open the project in Visual Studio Code and execute the `docker-compose.yaml` file to set up the necessary environment.
4. **Access MAGE**: With the services running, navigate to `http://localhost:6789/` to access MAGE's interface.
5. **Cloud Storage & BigQuery**: Set up the required buckets in Google Cloud Storage and create the dataset in BigQuery for data storage and management.
6. **Data Processing with Dataproc**: Utilize the Dataproc service for distributed data processing, leveraging Apache Spark for transformations.
7. **Analytics in BigQuery**: Analyze the transformed data within BigQuery, executing queries for insightful trends and metrics.
8. **Visualization with Looker Studio**: Use Looker Studio to create visual dashboards that effectively communicate the analyzed data.

Follow these steps to ensure a smooth setup and replication of the noise complaints analysis project.

# Acknowledgments

Big shoutout to DataTalk.club for their exceptional course that greatly contributed to the development of this project!


