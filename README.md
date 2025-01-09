# Japanese Sales Dashboard

## Introduction
The **Japanese Sales Dashboard** is a dynamic data visualization tool developed using Streamlit. It allows users to analyze sales data from Tokyo, Osaka, and Yokohama for the years 2022 and 2023. This dashboard is simple yet powerful, enabling users to toggle between current and previous year data and explore sales trends by month or product category. The dashboard can be accessed through this [LINK](https://japan-sales-dashboard.streamlit.app/)

## Table of Contents
1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Configuration](#configuration)
6. [Data Source](#data-source)
7. [Examples](#examples)

## Features
- **City-based Analysis**: Toggle between sales data for Tokyo, Osaka, and Yokohama.
- **Year Comparison**: View sales data for the current year (2023) or the previous year (2022).
- **Sales by Month**: Visualize monthly sales trends for a selected city.
- **Sales by Product Category**: Explore product-wise sales distribution for a selected city.
- **Key Metrics**: Display total revenue and percentage change for each city compared to the previous year.

## Technologies Used
- **Streamlit**: For building the interactive dashboard.
- **Pandas**: For data manipulation and aggregation.
- **Python**: As the core programming language.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/The-alpha-male/japan-sales-streamlit-dashboard.git
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the Streamlit app:
    ```bash
    streamlit run streamlit_app.py
    ```
2. Open the app in your browser using the URL displayed in the terminal.

## Configuration
- **Year**: Default is set to `2023`. Modify in the `streamlit_app.py` file if needed.
- **Cities**: The dashboard analyzes data for Tokyo, Osaka, and Yokohama.
- **Data Source**: Data is fetched from a CSV file hosted [here](https://raw.githubusercontent.com/Sven-Bo/datasets/master/store_sales_2022-2023.csv). The URL can be updated in the `DATA_URL` variable.

## Data Source
The data is sourced from:
[store_sales_2022-2023.csv](https://raw.githubusercontent.com/Sven-Bo/datasets/master/store_sales_2022-2023.csv)

## Examples
### Sales by Month
![image](https://github.com/user-attachments/assets/eea2ecee-9b3c-4c75-bb4b-9378ebf20a9f)

### Sales by Product Category
![image](https://github.com/user-attachments/assets/0475e7f9-3497-4554-903a-a5233af4663b)
