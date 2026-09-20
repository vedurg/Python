# 📈 Stock Market Analysis

> **A simple, menu-driven Python project for exploring stock market
> data, analyzing prices, calculating moving averages, and visualizing
> market trends.**

------------------------------------------------------------------------

## 🚀 Project Overview

**Stock Market Analysis** is a beginner-friendly data analysis project
built with Python.

The project loads stock market data from a CSV file and provides an
interactive menu to:

-   📂 Load and inspect stock data
-   👀 View dataset records and structure
-   📊 Perform basic stock analysis
-   📈 Calculate 20-day and 50-day moving averages
-   🔎 Analyze market price trends
-   📉 Visualize stock prices, volume, and distributions

The project is designed as a **single Python file** with a simple
menu-driven interface.

------------------------------------------------------------------------

## ✨ Key Features

  -----------------------------------------------------------------------
  Feature                             Description
  ----------------------------------- -----------------------------------
  📂 Load Stock Data                  Load stock data directly from a CSV
                                      file

  🔍 Dataset Information              View rows, columns, data types and
                                      dataset details

  👀 View Data                        Display first/last records, shape
                                      and column names

  📊 Basic Analysis                   Find highest, lowest and average
                                      prices

  📈 Moving Average                   Calculate 20-day and 50-day moving
                                      averages

  📉 Market Trend                     Analyze daily price changes and
                                      price levels

  📊 Visualization                    Generate multiple charts for better
                                      understanding

  🧭 Menu Driven                      Easy-to-use interactive console
                                      menu
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 🧠 Project Menu

``` text
=========== STOCK MARKET ANALYSIS ============

1. Load Stock Data
2. View Data
3. Basic Stock Analysis
4. Moving Average Analysis
5. Market Trend Analysis
6. Visualization
7. Exit
```

------------------------------------------------------------------------

## 📂 Project Structure

``` text
Stock-Market-Analysis/
│
├── Final_Project.py
├── GoogleStockPrices.csv
└── README.md
```

------------------------------------------------------------------------

## 📊 Analysis Modules

### 1. Load Stock Data

Load the stock dataset and check its information.

``` text
1. Load CSV File
2. Check Dataset Information
3. Go Back
```

### 2. View Data

Explore the dataset structure.

``` text
1. Display First 5 Rows
2. Display Last 5 Rows
3. Display Dataset Shape
4. Display Column Names
5. Go Back
```

### 3. Basic Stock Analysis

Perform basic statistical analysis such as:

-   Highest Closing Price
-   Lowest Closing Price
-   Average Closing Price
-   Highest Trading Volume
-   Lowest Trading Volume
-   Statistical Summary

### 4. Moving Average Analysis

Calculate:

-   📈 20-Day Moving Average
-   📈 50-Day Moving Average

Moving averages help smooth short-term price fluctuations and make
longer-term trends easier to observe.

### 5. Market Trend Analysis

Analyze:

-   Daily Price Change
-   Highest Price
-   Lowest Price
-   Average Opening Price
-   Trend Data

### 6. Visualization

The project generates different types of charts:

#### 📈 Closing Price Line Chart

Shows how the closing price changes over time.

#### 🔵 High-Low Price Scatter Chart

Shows the relationship between high and low prices.

#### 📊 Trading Volume Bar Chart

Shows trading volume across dates.

#### 📉 Closing Price Distribution

Uses a histogram with KDE to understand the distribution of closing
prices.

------------------------------------------------------------------------

## 🛠️ Technologies Used

-   🐍 **Python**
-   🐼 **Pandas** --- Data loading and DataFrame operations
-   🔢 **NumPy** --- Numerical calculations
-   📊 **Matplotlib** --- Data visualization
-   🎨 **Seaborn** --- Statistical visualization

------------------------------------------------------------------------

## ▶️ How to Run

Keep these files in the same folder:

``` text
Final_Project.py
GoogleStockPrices.csv
```

Then run:

``` bash
python Final_Project.py
```

The interactive menu will appear in the terminal.

------------------------------------------------------------------------

## 📁 Dataset

The project uses:

``` text
GoogleStockPrices.csv
```

The dataset contains stock market information such as:

``` text
Date
Open
High
Low
Close
Volume
```

------------------------------------------------------------------------

## 💡 Example Workflow

``` text
Start
  ↓
Load Stock Data
  ↓
View Dataset
  ↓
Perform Basic Analysis
  ↓
Calculate Moving Averages
  ↓
Analyze Market Trends
  ↓
Generate Visualizations
  ↓
Exit
```

------------------------------------------------------------------------

## 🎯 Learning Objectives

This project demonstrates practical use of:

-   Classes and objects
-   Constructors
-   Menu-driven programming
-   Pandas DataFrames
-   NumPy calculations
-   Data filtering and analysis
-   Moving averages
-   Matplotlib charts
-   Seaborn visualization
-   CSV data handling
-   Object-oriented Python structure

------------------------------------------------------------------------

## 🌟 Why This Project?

Stock market data contains a large amount of numerical information. Raw
numbers can be difficult to understand, so this project converts that
data into:

**Data → Analysis → Trends → Visual Insights**

The goal is to make stock data easier to explore while practicing
real-world Python data analysis concepts.

------------------------------------------------------------------------

## ⚠️ Disclaimer

This project is created for **educational and data-analysis purposes
only**.

The analysis and visualizations should not be considered financial or
investment advice.

------------------------------------------------------------------------

---

> **Built with Python 🐍 \| Data 📊 \| Analysis 🔎 \| Visualization 📈**
