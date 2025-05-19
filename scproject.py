%%writefile scproject.py
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide', page_title='scproject')

df = pd.read_csv('cleaned_SC_project_df.csv', index_col=0, encoding='latin1')
df['order_date_(DateOrders)'] = pd.to_datetime(df['order_date_(DateOrders)'])

# Sidebar selection for page navigation
page = st.sidebar.radio("Select Page", ["Basic Analysis", "Advanced Analysis", "Smart Analysis"])

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

elif page == "Advanced Analysis":
    st.title('Advanced Analysis')
    
    min_date = df['order_date_(DateOrders)'].min().date()
    max_date = df['order_date_(DateOrders)'].max().date()

    Delivery_Status = st.sidebar.selectbox('Delivery_Status', df['Delivery_Status'].unique())
    Order_Region = st.sidebar.selectbox('Order_Region', df['Order_Region'].unique())
    start_date = st.sidebar.date_input('Start Date', min_value=min_date, max_value=max_date, value=min_date)
    end_date = st.sidebar.date_input('End Date', min_value=min_date, max_value=max_date, value=max_date)
    top_n = st.sidebar.slider('Top N', min_value=1, max_value=df['Product_Name'].nunique(), step=1, value=5)

    df_filtered = df[
        (df['Delivery_Status'] == Delivery_Status) &
        (df['Order_Region'] == Order_Region) &
        (df['order_date_(DateOrders)'] >= pd.to_datetime(start_date)) &
        (df['order_date_(DateOrders)'] <= pd.to_datetime(end_date))
    ]

    st.dataframe(df_filtered)

    prod_count = df_filtered['Product_Name'].value_counts().reset_index().head(top_n)
    prod_count.columns = ['Product_Name', 'count']
    fig = px.bar(data_frame=prod_count, x='Product_Name', y='count',
                title=f'The Most Popular {top_n} Product Names')
    st.plotly_chart(fig)

else:
    st.title("Smart Analysis")

    st.header("1. Late Delivery Risk by Region")
    risk_by_region = df.groupby('Order_Region')['Late_delivery_risk'].mean().reset_index()
    fig1 = px.bar(risk_by_region, x='Order_Region', y='Late_delivery_risk', title="Average Late Delivery Risk by Region")
    st.plotly_chart(fig1)

    st.header("2. Actual vs Scheduled Shipping Days by Mode")
    shipping_compare = df[['Shipping_Mode', 'Days_for_shipping_(real)', 'Days_for_shipment_(scheduled)']]
    shipping_melt = shipping_compare.melt(id_vars='Shipping_Mode', var_name='Type', value_name='Days')
    fig2 = px.box(shipping_melt, x='Shipping_Mode', y='Days', color='Type', title="Shipping Days Comparison")
    st.plotly_chart(fig2)

    st.header("3. Monthly Shipping Efficiency")
    df['YearMonth'] = df['order_date_(DateOrders)'].dt.to_period('M')
    monthly_eff = df.groupby('YearMonth')['shipping_efficiency'].mean().reset_index()
    monthly_eff['YearMonth'] = monthly_eff['YearMonth'].astype(str)
    fig3 = px.line(monthly_eff, x='YearMonth', y='shipping_efficiency', title="Monthly Average Shipping Efficiency")
    st.plotly_chart(fig3)

    st.header("4. Profitability Distribution")
    profit_dist = df['is_profitable'].value_counts().reset_index()
    profit_dist.columns = ['is_profitable', 'count']
    fig4 = px.pie(profit_dist, names='is_profitable', values='count', title="Profitability Ratio")
    st.plotly_chart(fig4)

    st.header("5. Delivery Delay by Customer Segment")
    delay_segment = df.groupby('Customer_Segment')['shipping_delay'].mean().reset_index()
    fig5 = px.bar(delay_segment, x='Customer_Segment', y='shipping_delay', title="Average Delivery Delay per Segment")
    st.plotly_chart(fig5)
