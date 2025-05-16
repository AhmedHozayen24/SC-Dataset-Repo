
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout= 'wide', page_title= 'scproject')

df = pd.read_csv('cleaned_SC_project_df.csv', index_col= 0)

st.title('What is the percentage of each Shipping_Mode?')
st.plotly_chart(px.pie(df, names= 'Shipping_Mode'))

st.title('What is the total number of orders per Country?')
Order_Country_count = df.Order_Country.value_counts().reset_index()
st.plotly_chart(px.bar(Order_Country_count, x= 'Order_Country', y= 'count'))

st.title('What is the cumulative profit from start date till end date ?')
df_sorted = df.sort_values(by= 'order_date_(DateOrders)')
df_sorted['cum_profit'] = df_sorted['Order_Profit_Per_Order'].cumsum().round(2)
st.plotly_chart(px.line(data_frame= df_sorted, x= 'order_date_(DateOrders)', y= 'cum_profit'))
