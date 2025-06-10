import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Load data
data_path = 'data/infineon_product_data.csv'
df = pd.read_csv(data_path)

# Data cleaning and preprocessing
def clean_price(price):
    return float(str(price).replace('$', '').replace(',', ''))

df['price'] = df['price'].apply(clean_price)
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['revenue'] = df['price'] * df['units_sold']

# Sidebar - Dark mode
st.sidebar.markdown(
    f"<div style='text-align:center;'><img src='https://www.infineon.com/export/sites/default/media/products/Sensors/PG-VFWLB-76-1-web.png' width='120'/></div>",
    unsafe_allow_html=True
)
st.sidebar.title('Filters')
regions = ['All'] + sorted(df['region'].dropna().unique())
region = st.sidebar.selectbox('Region', regions)
categories = ['All'] + sorted(df['product_category'].dropna().unique())
category = st.sidebar.selectbox('Product Category', categories)
date_min, date_max = df['date'].min(), df['date'].max()
date_range = st.sidebar.date_input('Date Range', [date_min, date_max], min_value=date_min, max_value=date_max)

# Filter data
df_filtered = df.copy()
if region != 'All':
    df_filtered = df_filtered[df_filtered['region'] == region]
if category != 'All':
    df_filtered = df_filtered[df_filtered['product_category'] == category]
df_filtered = df_filtered[(df_filtered['date'] >= pd.to_datetime(date_range[0])) & (df_filtered['date'] <= pd.to_datetime(date_range[1]))]

# Main area - Light mode
st.markdown('<h1 style="text-align:center; color:#007C92;">Infineon Sales & Revenue Dashboard</h1>', unsafe_allow_html=True)

# KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric('Total Revenue', f"${df_filtered['revenue'].sum():,.2f}")
col2.metric('Units Sold', int(df_filtered['units_sold'].sum()))
col3.metric('Unique Products', df_filtered['product_name'].nunique())
col4.metric('Regions', df_filtered['region'].nunique())

# Charts
st.markdown('---')
chart_col1, chart_col2 = st.columns([2,1])

# Revenue by Region (Donut/Polar)
with chart_col1:
    region_rev = df_filtered.groupby('region')['revenue'].sum().reset_index()
    fig_region = px.pie(region_rev, names='region', values='revenue', hole=0.5, color_discrete_sequence=px.colors.qualitative.Pastel)
    fig_region.update_layout(title='Revenue by Region')
    st.plotly_chart(fig_region, use_container_width=True)

# Revenue by Product Category (Bar)
with chart_col2:
    cat_rev = df_filtered.groupby('product_category')['revenue'].sum().reset_index()
    fig_cat = px.bar(cat_rev, x='product_category', y='revenue', color='product_category', color_discrete_sequence=px.colors.qualitative.Set2)
    fig_cat.update_layout(title='Revenue by Product Category', xaxis_title='', yaxis_title='Revenue')
    st.plotly_chart(fig_cat, use_container_width=True)

# Revenue and Units Sold Over Time (Line)
st.markdown('---')
region_options = ['All'] + sorted(df['region'].dropna().unique())
selected_region = st.radio('Select Region for Trend', region_options, horizontal=True)
df_trend = df_filtered.copy()
if selected_region != 'All':
    df_trend = df_trend[df_trend['region'] == selected_region]
time_agg = df_trend.groupby('date').agg({'revenue':'sum', 'units_sold':'sum'}).reset_index()
fig_trend = px.line(time_agg, x='date', y=['revenue', 'units_sold'], labels={'value':'Amount', 'variable':'Metric'}, color_discrete_map={'revenue':'#007C92', 'units_sold':'#F39200'})
fig_trend.update_layout(title='Revenue and Units Sold Over Time')
st.plotly_chart(fig_trend, use_container_width=True)
