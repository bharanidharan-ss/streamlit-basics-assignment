import streamlit as st
import pandas as pd
st.title("Sales Summary Dashboard")
st.subheader("Simple interactive app to filter sales by category")
data = {
    "Product": ["Laptop", "Shirt", "Phone", "Shoes", "Watch"],
    "Category": ["Electronics", "Clothing", "Electronics", "Footwear", "Accessories"],
    "Sales": [50000, 2000, 30000, 4000, 7000]
}
df = pd.DataFrame(data)
st.sidebar.header("Filter Options")
category = st.sidebar.selectbox("Select Category", df["Category"].unique())
filtered_df = df[df["Category"] == category]
st.write(f"Showing data for category: {category}")
st.dataframe(filtered_df)
st.line_chart(filtered_df["Sales"])