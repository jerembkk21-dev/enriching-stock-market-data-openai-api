# enriching-stock-market-data-openai-api
Python project using pandas and the OpenAI API to enrich Nasdaq stock market data with AI-generated sector classifications and investment recommendations.

## 1) Project Overview

This project demonstrates how Generative AI can be integrated into a data analysis workflow to enrich financial datasets. Using Python, pandas, and the OpenAI API, Nasdaq stock market data was processed, combined with performance metrics, and enhanced with AI-generated sector classifications and investment recommendations.

The project shows how AI can support data enrichment, automated categorization, and the generation of business insights from structured datasets.

---

## 2) Objectives

The main objectives of this project were:

- Import and combine Nasdaq company information with stock performance data.
- Calculate and analyze year-to-date (YTD) performance metrics.
- Use the OpenAI API to classify companies into predefined business sectors.
- Generate AI-based recommendations by identifying high-performing sectors and representative companies.
- Demonstrate the use of Generative AI in a data analytics workflow.

---

## 3) Technologies Used

- Python
- Pandas
- OpenAI API
- Generative AI
- Jupyter Notebook / Visual Studio Code
- Git & GitHub

---

## 4) Dataset

The project uses two datasets:

### Nasdaq Company Information
Contains company details including:

- Stock symbol
- Company name
- Headquarters location
- Date added to Nasdaq-100 index
- Founded date

### Nasdaq Price Performance Data

Contains stock performance indicators:

- Daily performance
- Monthly performance
- Year-to-date (YTD) performance
- Long-term performance metrics

---

## 5) Project Workflow

### a) Data Import and Preparation

- Loaded Nasdaq company data using pandas.
- Imported stock performance data.
- Merged datasets using the company stock symbol.

### b) AI-Based Sector Classification

The OpenAI API was used to classify each company into one of the following sectors:

- Technology
- Consumer Cyclical
- Industrials
- Utilities
- Healthcare
- Communication
- Energy
- Consumer Defensive
- Real Estate
- Financial

The generated classifications were stored as a new `sector` column in the dataset.

### c) AI-Generated Recommendations

The enriched dataset was provided to the OpenAI API to generate:

- The two most promising sectors.
- Representative companies within each sector.
- A short explanation supporting the recommendations.

---

## 6) Key Features

- Automated data enrichment using Generative AI.
- API integration with OpenAI.
- Data merging and transformation using pandas.
- AI-powered company classification.
- Automated generation of analytical summaries.

---

## 7) Example Output

Example AI-generated recommendation:

**Technology Sector**

- Apple Inc.
- Nvidia
- Meta Platforms

**Healthcare Sector**

- Intuitive Surgical
- DexCom

The analysis highlights sectors with strong growth potential based on available performance data.

---

## 8) Skills Demonstrated

- Python data analysis
- pandas data manipulation
- API integration
- Generative AI implementation
- Data enrichment techniques
- Automated insight generation
- Data-driven decision support
