
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide', page_title='scproject')

df = pd.read_csv('cleaned_SC_project_df.csv', encoding='latin1')
df['order_date_(DateOrders)'] = pd.to_datetime(df['order_date_(DateOrders)'])

# Sidebar selection for page navigation
page = st.sidebar.radio("Select Page", ["Basic Analysis", "Advanced Analysis"])

if page == "Basic Analysis":
    st.title('Basic Analysis')
    
    st.header('What is the percentage of each Shipping_Mode?')
    st.plotly_chart(px.pie(df, names='Shipping_Mode'))
    
    st.header('What is the total number of orders per Country?')
    Order_Country_count = df.Order_Country.value_counts().reset_index()
    st.plotly_chart(px.bar(Order_Country_count, x='Order_Country', y='count'))
    
    st.header('What is the cumulative profit from start date till end date?')
    df_sorted = df.sort_values(by='order_date_(DateOrders)')
    df_sorted['cum_profit'] = df_sorted['Order_Profit_Per_Order'].cumsum().round(2)
    st.plotly_chart(px.line(data_frame=df_sorted, x='order_date_(DateOrders)', y='cum_profit'))

else:
    st.title('Advanced Analysis')
    
    # Get min and max dates
    min_date = df['order_date_(DateOrders)'].min().date()
    max_date = df['order_date_(DateOrders)'].max().date()
    
    # Advanced filters
    Delivery_Status = st.sidebar.selectbox('Delivery_Status', df['Delivery_Status'].unique())
    Order_Region = st.sidebar.selectbox('Order_Region', df['Order_Region'].unique())
    start_date = st.sidebar.date_input('Start Date', min_value=min_date, max_value=max_date, value=min_date)
    end_date = st.sidebar.date_input('End Date', min_value=min_date, max_value=max_date, value=max_date)
    top_n = st.sidebar.slider('Top N', min_value=1, max_value=df['Product_Name'].nunique(), step=1, value=5)
    
    # Apply filters
    df_filtered = df[
        (df['Delivery_Status'] == Delivery_Status) &
        (df['Order_Region'] == Order_Region) &
        (df['order_date_(DateOrders)'] >= pd.to_datetime(start_date)) &
        (df['order_date_(DateOrders)'] <= pd.to_datetime(end_date))
    ]
    
    # Show filtered data
    st.dataframe(df_filtered)
    
    # Top products analysis
    prod_count = df_filtered['Product_Name'].value_counts().reset_index().head(top_n)
    prod_count.columns = ['Product_Name', 'count']
    
    fig = px.bar(data_frame=prod_count, x='Product_Name', y='count',
                title=f'The Most Popular {top_n} Product Names')
    
    st.plotly_chart(fig)
