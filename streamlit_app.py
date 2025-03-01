# Import Libraries
import streamlit as st
import pandas as pd


# -- CONFIGS --
YEAR = 2023
CITIES = ["Tokyo", "Osaka", "Yokohama"]
DATA_URL = "https://raw.githubusercontent.com/Sven-Bo/datasets/master/store_sales_2022-2023.csv"


# --- PAGE SETUP ---
st.set_page_config(page_title="Sales Dashboard", page_icon="📈")
st.title("Sales Dashboard")


# --- HIDE STREAMLIT BRANDING ---
hide_st_style = """
    <style>
    #MainMenu {visibility:hidden;}
    header {visibility:hidden;}
    </style>
    """
st.markdown(hide_st_style, unsafe_allow_html=True)
    

# --- LOAD DATA ---
@st.cache_data
def load_data(data_url):
    data = pd.read_csv(data_url)
    data["date_of_sale"] = pd.to_datetime(data["date_of_sale"])
    data["month"] = data["date_of_sale"].dt.month
    data["year"] = data["date_of_sale"].dt.year

    return data

data = load_data(DATA_URL)
# st.dataframe(data)

# Calculate total revenue for each city and year then calculate percentage change
city_revenue = (
    data.groupby(["city", "year"])["sales_amount"]
    .sum()
    .unstack()
    .assign(change=lambda x: x.pct_change(axis=1)[YEAR] *100)
)
# st.dataframe(city_revenue)

# --- KEY METRICS ---
# Display each city's data in separate columns
left_col, middle_col, right_col = st.columns(3)

with left_col:
    st.metric(
        label=CITIES[0],
        value=f"$ {city_revenue.loc[CITIES[0], YEAR]:.2f}",
        delta=f"{city_revenue.loc[CITIES[0], 'change']:.2f}% vs. Last Year",
    )

# City 2 in the middle column
with middle_col:
    st.metric(
        label=CITIES[1],
        value=f"$ {city_revenue.loc[CITIES[1], YEAR]:.2f}",
        delta=f"{city_revenue.loc[CITIES[1], 'change']:.2f}% vs. Last Year",
    )

# City 3 in the right column
with right_col:
    st.metric(
        label=CITIES[2],
        value=f"$ {city_revenue.loc[CITIES[2], YEAR]:.2f}",
        delta=f"{city_revenue.loc[CITIES[2], 'change']:.2f}% vs. Last Year",
    )



# --- SELCETION FIELDS ---
selected_city = st.selectbox("Select a city:", CITIES)
show_previous_year = st.toggle("Show previous year")
if show_previous_year:
    visualization_year = YEAR -1
else:
    visualization_year = YEAR
st.write(f"Sales for {visualization_year}")

# Tabs for analysis type
tab_month, tab_category = st.tabs(["Monthly Analysis", "Category Analysis"])

# -- FILTER & VISUALIZE DATA ---
with tab_month:
    filtered_data = (
        data.query("city == @selected_city & year == @visualization_year")
        .groupby("month", dropna=False, as_index=False)["sales_amount"]
        .sum()
    )
    st.bar_chart(
        data=filtered_data.set_index("month")["sales_amount"],
    )

with tab_category:
    filtered_data = (
        data.query("city == @selected_city & year == @visualization_year")
        .groupby("product_category", dropna=False, as_index=False)["sales_amount"]
        .sum()
    )
    st.bar_chart(
        data=filtered_data.set_index("product_category")["sales_amount"],
    )
