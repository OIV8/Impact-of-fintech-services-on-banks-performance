
# FinTech and Bank Profitability: An Empirical Analysis

This project investigates the impact of FinTech services on the profitability of Italian banks using econometric methods. It combines rigorous statistical analysis with an interactive web interface to communicate results effectively.

## 📘 Overview

The study employs an **unbalanced panel data approach with fixed effects** to evaluate how FinTech development affects the financial performance of banks in Italy. 

The project consists of the following components:

1. **`fintech.py`** – Performs the data analysis and econometric modeling.
2. **`stream.py`** – Builds an interactive web app using [Streamlit](https://streamlit.io/) to visualize the results.
3. **`fintech_listed.xlsx`** – Contains raw and processed data on Italian banks, sourced from BankFocus and supplemented with manually collected financial statement data.

## 🧠 Methodology

- **Data**: The dataset comprises panel data from Italian banks over multiple years, with variables capturing profitability (e.g., ROA, ROE) and FinTech activity.
- **Sources**: 
  - **BankFocus** – for standardized financial and banking data.
  - **Manual Collection** – for missing or complementary data from financial statements.
- **Model**: An **unbalanced panel regression with fixed effects** is applied to control for time-invariant heterogeneity among banks.
- **Software**: Python with libraries like `pandas`, `statsmodels`, and `streamlit`.

## 📊 Results Summary

The regression results from `fintech.py` suggest statistically significant relationships between FinTech engagement and profitability measures. These results are automatically exported and used in the web application.

## 🌐 Web App

`stream.py` contains a Streamlit app that allows users to:

- View regression output tables.
- Understand the relationship between FinTech metrics and bank profitability.
- Interact with and explore the data in a user-friendly interface.

To run the app:

```bash
streamlit run stream.py
```

## 📁 File Structure

- `fintech.py` – Performs data preprocessing, model estimation, and outputs results.
- `stream.py` – Streamlit-based dashboard for exploring the econometric findings.
- `dataset.xlsx` – Panel dataset on Italian banks, combining BankFocus and manually collected data.
- `README.md` – Project documentation.

