import pandas as pd
from pathlib import Path


# PROJECT PATHS


PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_PATH = (
    PROJECT_ROOT
    / "datasets"
    / "olistbr"
    / "brazilian-ecommerce"
    / "versions"
    / "2"
)

OUTPUT_PATH = PROJECT_ROOT / "cleaned_data"

# Create cleaned_data folder if it doesn't exist
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

# =====================================================
# LOAD DATASETS
# =====================================================

customers = pd.read_csv(DATA_PATH / "olist_customers_dataset.csv")
orders = pd.read_csv(DATA_PATH / "olist_orders_dataset.csv")
order_items = pd.read_csv(DATA_PATH / "olist_order_items_dataset.csv")
payments = pd.read_csv(DATA_PATH / "olist_order_payments_dataset.csv")
products = pd.read_csv(DATA_PATH / "olist_products_dataset.csv")
reviews = pd.read_csv(DATA_PATH / "olist_order_reviews_dataset.csv")
sellers = pd.read_csv(DATA_PATH / "olist_sellers_dataset.csv")
geolocation = pd.read_csv(DATA_PATH / "olist_geolocation_dataset.csv")
translation = pd.read_csv(DATA_PATH / "product_category_name_translation.csv")

print("=" * 60)
print("DATA LOADED SUCCESSFULLY")
print("=" * 60)


# DATE CONVERSION


date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]

for col in date_columns:
    orders[col] = pd.to_datetime(orders[col], errors="coerce")

print("✓ Date columns converted")


# FEATURE ENGINEERING


orders["delivery_days"] = (
    orders["order_delivered_customer_date"]
    - orders["order_purchase_timestamp"]
).dt.days

orders["delivery_status"] = "Not Delivered"

mask = orders["order_delivered_customer_date"].notna()

orders.loc[
    mask &
    (
        orders["order_delivered_customer_date"]
        <= orders["order_estimated_delivery_date"]
    ),
    "delivery_status",
] = "On Time"

orders.loc[
    mask &
    (
        orders["order_delivered_customer_date"]
        > orders["order_estimated_delivery_date"]
    ),
    "delivery_status",
] = "Late"

orders["order_month"] = orders["order_purchase_timestamp"].dt.month
orders["order_year"] = orders["order_purchase_timestamp"].dt.year
orders["order_day"] = orders["order_purchase_timestamp"].dt.day
orders["order_weekday"] = orders["order_purchase_timestamp"].dt.day_name()

print("✓ Business features created")


# HANDLE MISSING VALUES


products["product_category_name"] = products[
    "product_category_name"
].fillna("Unknown")

products["product_name_lenght"] = products[
    "product_name_lenght"
].fillna(0)

products["product_description_lenght"] = products[
    "product_description_lenght"
].fillna(0)

products["product_photos_qty"] = products[
    "product_photos_qty"
].fillna(0)

products["product_weight_g"] = products[
    "product_weight_g"
].fillna(0)

products["product_length_cm"] = products[
    "product_length_cm"
].fillna(0)

products["product_height_cm"] = products[
    "product_height_cm"
].fillna(0)

products["product_width_cm"] = products[
    "product_width_cm"
].fillna(0)

reviews["review_comment_title"] = reviews[
    "review_comment_title"
].fillna("No Title")

reviews["review_comment_message"] = reviews[
    "review_comment_message"
].fillna("No Comment")

print("✓ Missing values handled")


# TRANSLATE PRODUCT CATEGORIES

products = products.merge(
    translation,
    on="product_category_name",
    how="left",
)

products["product_category_name_english"] = products[
    "product_category_name_english"
].fillna(products["product_category_name"])

print("✓ Product categories translated")


# REMOVE DUPLICATES


geolocation = geolocation.drop_duplicates()

print("✓ Duplicate geolocations removed")

# SAVE CLEANED DATA

print("\nSaving files to:")
print(OUTPUT_PATH)

customers.to_csv(OUTPUT_PATH / "customers.csv", index=False)
orders.to_csv(OUTPUT_PATH / "orders.csv", index=False)
order_items.to_csv(OUTPUT_PATH / "order_items.csv", index=False)
payments.to_csv(OUTPUT_PATH / "payments.csv", index=False)
products.to_csv(OUTPUT_PATH / "products.csv", index=False)
reviews.to_csv(OUTPUT_PATH / "reviews.csv", index=False)
sellers.to_csv(OUTPUT_PATH / "sellers.csv", index=False)
geolocation.to_csv(OUTPUT_PATH / "geolocation.csv", index=False)

print("\n" + "=" * 60)
print("ETL COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nDelivery Status Summary:")
print(orders["delivery_status"].value_counts())

print("\nCleaned files saved successfully!")
print(OUTPUT_PATH)
