# Customer-behaviour-analysis
End-to-end customer shopping behaviour analysis using Python, Pandas, MySQL, and Power bi. covering data cleaning, transformation, and 10 business-driven analytical queries.

# Customer Behaviour Analysis

A complete data analytics project that explores customer shopping patterns, spending habits, and purchasing behaviour using a real-world retail dataset.

## Project Overview

This project follows a full data analytics pipeline — from raw CSV data to  structured SQL insights — to answer key business questions about customer  demographics, product preferences, discount usage, and subscription behaviour.

##  Tech Stack

- Python — Data cleaning & transformation (Pandas, SQLAlchemy)
- MySQL — Data storage & business queries
- SQL — Exploratory & analytical querying
- Power bi - Visual understanding

## Pipeline

Raw CSV → Python (Clean & Transform) → MySQL Analaysis → Visual Dasboard

## Key Business Questions Answered

1.  Total revenue by gender
2.  Revenue breakdown by age group
3.  Discount users who still spent above average
4.  Top 5 highest-rated products
5.  Spending comparison: Standard vs Express shipping
6.  Do subscribed customers spend more?
7.  Products with highest discount usage rate
8.  Customer segmentation: New, Returning & Loyal
9.  Repeat buyers vs subscription behaviour
10. Top 3 most preferred payment methods

##  Data Cleaning Highlights

- Null values filled using **category-wise median** for review ratings
- Age groups created using **quantile-based binning**
- Duplicate/redundant columns removed after validation
- Data exported from Python directly into **MySQL** via SQLAlchemy

## Files

| File | Description |
|------|-------------|
| `customer_behaviour.py` | Data cleaning & SQL export script |
| `customer_behaviour.sql` | All 10 business queries |
| `customer_shopping_behavior.csv` | Raw dataset |
| `customer_behaviour_report.pbix` | power bi report |

<img width="1449" height="816" alt="image" src="https://github.com/user-attachments/assets/0a98bab3-67c5-4282-82fc-aa542252caaa" />


## Key Metrics

- Customers: 3,900
- Avg Purchase: $59.76
- Avg Rating: 3.75

## Insights

- Male customers contribute ~68% sales  
- Clothing is the top category  
- Most users are non-subscribers  
- Free shipping & PayPal are most preferred  
