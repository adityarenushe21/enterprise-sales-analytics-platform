# Enterprise Sales & Commercial Analytics Dashboard

An end-to-end data analytics project built using Python, PostgreSQL, and Power BI.

The project focuses on cleaning raw e-commerce data, storing it in a relational database, and building an interactive business dashboard to analyze sales, customers, products, payments, and delivery performance.

---

## Project Workflow

The project follows a complete analytics pipeline:

Raw CSV Files
↓
Python ETL
↓
PostgreSQL Database
↓
Power BI Dashboard
↓
Business Insights

---

## Tech Stack

- Python
- Pandas
- PostgreSQL
- SQL
- Power BI
- DAX

---

## Project Structure

```
DATA ANALYSIS PRJ
│
├── datasets/
├── cleaned_data/
├── python/
│   ├── etl.py
│   └── data_profiling.py
│
├── sql/
│   ├── create_tables.sql
│   └── analysis_queries.sql
│
├── dashboard/
│   ├── dashboard_page1.png
│   ├── dashboard_page2.png
│   └── MY_DASHBOARD.pbix
│
└── README.md
```

---

## ETL Process

The ETL pipeline performs the following operations:

- Loads raw Olist e-commerce datasets
- Converts date columns into datetime format
- Creates delivery-related business features
- Calculates delivery days
- Classifies delivery status (On Time / Late / Not Delivered)
- Handles missing values
- Translates Portuguese product categories into English
- Removes duplicate records
- Saves cleaned datasets for analysis

---

## Database Design

The cleaned datasets are imported into PostgreSQL.

Tables used:

- Customers
- Orders
- Order Items
- Payments
- Products
- Sellers
- Reviews

Relationships are maintained using primary and foreign keys.

---

## Dashboard Features

The Power BI dashboard includes:

- Total Revenue
- Total Orders
- Average Delivery Days
- Average Customer Rating
- Late Orders
- Monthly Revenue Trend
- Revenue by Product Category
- Orders by State
- Payment Method Distribution
- Delivery Status Analysis

Interactive slicers allow filtering by year, state, and payment method.

---

## Dashboard Preview

### Dashboard Page 1
<img width="1167" height="652" alt="Screenshot 2026-07-10 000925" src="https://github.com/user-attachments/assets/7cb94f5a-59ba-41cc-88c4-4f536749d95d" />




### Dashboard Page 2
<img width="1161" height="653" alt="Screenshot 2026-07-10 000937" src="https://github.com/user-attachments/assets/8807add7-6eff-47df-a493-9f5187ec3f2e" />



## Key Business Insights

The dashboard helps answer questions such as:

- Which product categories generate the highest revenue?
- Which states contribute the most orders?
- Which payment methods are preferred by customers?
- How many deliveries are completed on time?
- How does delivery performance affect customer ratings?
- How does revenue change over time?

---

## Future Improvements

- Build automated ETL pipeline
- Connect directly to PostgreSQL instead of CSV files
- Deploy dashboard using Power BI Service
- Add customer segmentation and sales forecasting

---

## Dataset

Brazilian E-commerce Public Dataset by Olist

https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

---

## Author

Aditya Renushe
