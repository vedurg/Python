#Final Project.....................

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class StockMarketAnalysis:

    def __init__(self):
        self.data = None
        self.file_name = "GoogleStockPrices.csv"

    def main_menu(self):

        while True:
            print("\n=========== STOCK MARKET ANALYSIS ============")
            print("1. Load Stock Data")
            print("2. View Data")
            print("3. Basic Stock Analysis")
            print("4. Moving Average Analysis")
            print("5. Market Trend Analysis")
            print("6. Visualization")
            print("7. Exit")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.load_stock_data()

            elif choice == "2":
                self.view_data()

            elif choice == "3":
                self.stock_analysis()

            elif choice == "4":
                self.moving_average()

            elif choice == "5":
                self.market_trend_analysis()

            elif choice == "6":
                self.visualization()

            elif choice == "7":
                print("\nThank you for using Stock Market Analysis!\n")
                break

            else:
                print("\nInvalid choice! Please try again")

# Load Data................

    def load_stock_data(self):

        while True:
            print("\n---------- LOAD STOCK DATA ----------")
            print("1. Load CSV File")
            print("2. Check Dataset Information")
            print("3. Go Back")

            choice = input("\nEnter your choice: ")

            if choice == "1":

                self.data = pd.read_csv(self.file_name)

                print("\nData loaded successfully!")
                print(f"Total Rows: {len(self.data)}")
                print(f"Total Column: {len(self.data.columns)}")

            elif choice == "2":

                if self.data is None:
                    print("\nPlease load the data first")

                else:
                    print("\n------ DATA INFORMATION ------")
                    self.data.info()

            elif choice == "3":
                break

            else:
                print("\nInvalid choice! Please try again")

# View Data...................

    def view_data(self):

        while True:
            print("\n------ VIEW DATA ------")
            print("1. Display First 5 Rows")
            print("2. Display Last 5 Rows")
            print("3. Display Dataset Shape")
            print("4. Display Column Names")
            print("5. Go Back")

            choice = input("\nEnter your choice: ")

            if choice == "1":

                if self.data is None:
                    print("\nPlease load the data first")

                else:
                    print("\n------ FIRST 5 ROWS ------")
                    print(self.data.head())

            elif choice == "2":

                if self.data is None:
                    print("\nPlease load the data first")

                else:
                    print("\n------ LAST 5 ROWS ------")
                    print(self.data.tail())

            elif choice == "3":

                if self.data is None:
                    print("\nPlease load the data first")

                else:
                    print("\n------ DATASET SHAPE ------")
                    print("Rows:", self.data.shape[0])
                    print("Columns:", self.data.shape[1])

            elif choice == "4":

                if self.data is None:
                    print("\nPlease load the data first")

                else:
                    print("\n------ COLUMN NAMES ------")
                    print(self.data.columns)

            elif choice == "5":
                break

            else:
                print("\nInvalid choice! Please try again")

# Basic Stock Analysis.............

    def stock_analysis(self):

        while True:

            print("\n------ BASIC STOCK ANALYSIS ------")
            print("1. Highest Closing Price")
            print("2. Lowest Closing Price")
            print("3. Average Closing Price")
            print("4. Highest Trading Volume")
            print("5. Lowest Trading Volume")
            print("6. Statistical Summary")
            print("7. Go Back")

            choice = input("\nEnter your choice: ")

            if choice == "1":

                if self.data is None:
                    print("\nPlease load the data first")

                else:
                    highest = np.max(self.data["Close"])
                    print("\nHighest Closing Price:", highest)

            elif choice == "2":
            
                if self.data is None:
                    print("\nPlease load the data first")

                else:
                    lowest = np.min(self.data["Close"])
                    print("\nLowest Closing Price:", lowest)

            elif choice == "3":

                if self.data is None:
                    print("\nPlease load the data first")

                else:
                    average = np.mean(self.data["Close"])
                    print("\nAverage Closing Price:", average)

            elif choice == "4":

                if self.data is None:
                    print("\nPlease load the data first")

                else:
                    highest_volume = np.max(self.data["Volume"])
                    print("\nHighest Trading Volume:", highest_volume)

            elif choice == "5":
            
                if self.data is None:
                    print("\nPlease load the data first")

                else:
                    lowest_volume = np.min(self.data["Volume"])
                    print("\nLowest Trading Volume:", lowest_volume)

            elif choice == "6":

                if self.data is None:
                    print("\nPlease load the data first")

                else:
                    print("\nStatistical Summary")
                    print(self.data.describe())

            elif choice == "7":
                break

            else:
                print("\nInvalid choice! Please try again")

# Moving Average Analysis

    def moving_average(self):

        while True:

            print("\n------ MOVING AVERAGE ANALYSIS ------")
            print("1. Calculate 20-Day Moving Average")
            print("2. Calculate 50-Day Moving Average")
            print("3. Display Moving Average Data")
            print("4. Go Back")

            choice = input("\nEnter your choice: ")

            if choice == "1":

                if self.data is None:
                    print("\nPlease load the data first")

                else:
                    self.data["MA20"] = self.data["Close"].rolling(20).mean()
                    print("\n20-Day Moving Average calculated successfully!\n")
                    print(self.data[["Date","Close","MA20"]].tail())

            elif choice == "2":
                
                if self.data is None:
                    print("\nPlease load the data first")

                else:
                    self.data["MA50"] = self.data["Close"].rolling(50).mean()
                    print("\n50-Day Moving Average calculated successfully!\n")
                    print(self.data[["Date","Close","MA50"]].tail())

            elif choice == "3":

                if self.data is None:
                    print("\nPlease load the data first")

                else:
                    print("\nMoving Average Data\n")
                    print(self.data.tail())

            elif choice == "4":
                break

            else:
                print("\nInvalid choice! Please try again")

# Market Trend Analysis...............

    def market_trend_analysis(self):

        while True:

            print("\n------ MARKET TREND ANALYSIS ------")
            print("1. Daily Price Change")
            print("2. Highest Price")
            print("3. Lowest Price")
            print("4. Average Opening Price")
            print("5. Display Trend Data")
            print("6. Go Back")

            choice = input("\nEnter your choice: ")

            if choice == "1":

                if self.data is None:
                    print("\nPlease load the data first")

                else:
                    self.data["Price Change"] = self.data["Close"] - self.data["Open"]
                    print("\nDaily Price Change calculated successfully!\n")
                    print(self.data[["Date", "Open", "Close", "Price Change"]].tail())

            elif choice == "2":

                if self.data is None:
                    print("\nPlease load the data first")

                else:
                    highest_price = np.max(self.data["High"])
                    print("\nHighest Price:", highest_price)

            elif choice == "3":

                if self.data is None:
                    print("\nPlease load the data first")

                else:
                    lowest_price = np.min(self.data["Low"])
                    print("\nLowest Price:", lowest_price)

            elif choice == "4":

                if self.data is None:
                    print("\nPlease load the data first")

                else:
                    average_open = np.mean(self.data["Open"])
                    print("\nAverage Opening Price:", average_open)

            elif choice == "5":

                if self.data is None:
                    print("\nPlease load the data first")

                else:
                    print("\nTrend Data\n")
                    print(self.data[["Date", "Open", "High", "Low", "Close"]].tail())

            elif choice == "6":
                break

            else:
                print("\nInvalid choice! Please try again")

# Visualization...................

    def visualization(self):

        while True:

            print("\n------ VISUALIZATION ------")
            print("1. Closing Price with Line Chart")
            print("2. High-Low Price with Scatter Plot")
            print("3. Trading Volume with Bar Chart")
            print("4. Closing Price Distribution with Histogram")
            print("5. Go Back")

            choice = input("\nEnter your choice: ")

            if choice == "1":

                if self.data is None:
                    print("\nPlease load the data first")

                else:
                    self.data["Date"] = pd.to_datetime(self.data["Date"])

                    plt.figure(figsize=(10,5))
                    plt.plot(self.data["Date"], self.data["Close"])
                    plt.title("Closing Price")
                    plt.xlabel("Date")
                    plt.ylabel("Closing Price")
                    plt.xticks(rotation=45)
                    plt.tight_layout()
                    plt.locator_params(axis="x",nbins=10)
                    plt.show() 

            elif choice == "2":

                if self.data is None:
                    print("\nPlease load the data first")

                else:
                    plt.figure(figsize=(10,5))
                    plt.scatter(self.data["High"], self.data["Low"])
                    plt.title("High-Low Price Analysis")
                    plt.xlabel("High Price")
                    plt.ylabel("Low Price")
                    plt.tight_layout()
                    plt.show()

            elif choice == "3":

                if self.data is None:
                    print("\nPlease load the data first")

                else:
                    plt.figure(figsize=(10,5))
                    plt.bar(self.data["Date"].tail(30),
                            self.data["Volume"].tail(30))

                    plt.title("Trading Volume")
                    plt.xlabel("Date")
                    plt.ylabel("Volume")
                    plt.xticks(rotation=45)
                    plt.tight_layout()
                    plt.show()

            elif choice == "4":

                if self.data is None:
                    print("\nPlease load the data first")

                else:
                    plt.figure(figsize=(8,5))
                    sns.histplot(self.data["Close"], kde=True)
                    plt.title("Closing Price Distribution")
                    plt.xlabel("Closing Price")
                    plt.ylabel("Frequency")
                    plt.tight_layout()
                    plt.show()

            elif choice == "5":
                break

            else:
                print("\nInvalid choice! Please try again")

# Object...............

analyzer = StockMarketAnalysis()
analyzer.main_menu()