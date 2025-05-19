🗂 Project Overview with Step-by-Step Actions & Insights

🎯 Objective

To analyze a large, unclean e-commerce dataset and extract actionable insights regarding logistics, delivery efficiency, profitability, and customer behavior using Python and Streamlit.

🧭 Workflow Breakdown & Actions

1. Data Understanding

   Action: Reviewed the dataset’s structure, types, and summary statistics.

   Insight: Found over 180,000 rows and a mix of categorical and numerical features — satisfying project criteria.

2. Data Cleaning

   Action: Handled null values, corrected data types (especially dates), and standardized column names.

   Insight: Issues like encoding inconsistencies and incorrect date formatting were resolved, enabling valid time-series and categorical analysis.

3. Exploratory Data Analysis (EDA)

   Action: Performed univariate and bivariate visualizations using Plotly (e.g., pie charts, bar graphs, line plots).

   Insight: Identified key metrics such as most used shipping mode, high-volume countries, and cumulative profit over time.

4. Feature Engineering
   
   Action: Created new metrics like:

      cum_profit: Cumulative profit across time.

      shipping_efficiency: Ratio of scheduled vs. actual shipping days.

      Late_delivery_risk: Binary flag for delivery delays.

      is_profitable: Flag for order-level profit or loss.

   Insight: These engineered features enabled deeper insights into operational bottlenecks and performance trends.

5. Advanced Filtering & Interactivity (Streamlit)
   
   Action: Built a dashboard with filters for region, delivery status, time range, and product count.

   Insight: Allowed dynamic analysis — e.g., finding which products are top sellers in delayed regions or during certain months.

6. Smart Analysis (Root Cause & Trend Analysis)
   
   Action: Visualized advanced metrics across dimensions:

   Shipping delays by region, segment, and delivery status.

   Loss-making products and profitability by segment.

   Monthly trends in efficiency and profitability.

Insight:

Central & Oceania regions show higher late delivery risk.

Some customer segments (e.g., Consumer) suffer more delays than others.

A small group of products consistently generate losses and should be reviewed.

7. Outcome Visualization
   
Action: Used pie charts, bar plots, and line graphs for interpretability.

Insight: Made trends visually clear for decision-makers — such as segment profitability and shipping performance.

🔍 Key Takeaways

Theme	Insight

📦 Shipping Modes	Standard Class is dominant, but First Class has schedule reliability issues.

🌍 Regions	U.S. & Puerto Rico lead in volume; Central & Oceania require logistic focus.

📉 Delays	Some customer segments face more frequent delays, possibly affecting satisfaction.

💰 Profitability	~15% of orders are loss-making; product-level analysis shows specific issues.

📈 Efficiency	Monthly trends suggest seasonal dips in shipping efficiency needing operational review.

✅ Final Outcomes

Data cleaned, structured, and visualized for executive-level insight.

Streamlit dashboard created for real-time, interactive analysis.

Actionable recommendations for:

Logistics improvements

Product strategy revisions

Segment-targeted marketing
