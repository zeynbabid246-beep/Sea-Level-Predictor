# Sea Level Predictor 🌊📈

Data Analysis & Forecasting: Predicting Global Sea Level Rise (1880–2050)

--Project Overview :

Dive into the rising tide of climate change with Sea Level Predictor – a data science journey that transforms 134 years of global sea level measurements (1880–2014) into crystal-clear forecasts through 2050. Using the precision of statistical linear regression, this project doesn't just analyze data – it unveils the ocean's urgent story, revealing accelerating trends that demand attention.

From scattered historical data points to publication-ready visualizations, witness how Python, Pandas, and SciPy turn raw climate observations into actionable insights about our planet's future. This isn't just code – it's data-driven climate storytelling at its most compelling.

--Objectives :

Analyze 134 years of global sea level measurements

Visualize long-term climate trends

Predict sea level rise to 2050 using statistical modeling

Compare historical vs accelerated recent trends

Generate reproducible, high-quality data visualizations

--Skills Demonstrated :

| Category      | Technologies/Tools                       |
| ------------- | ---------------------------------------- |
| Programming   | Python 3.8+                              |
| Data Analysis | Pandas, NumPy                            |
| Statistics    | SciPy (Linear Regression)                |
| Visualization | Matplotlib, Seaborn                      |
| Testing       | unittest                                 |
| Data Science  | EDA, trend forecasting, model comparison |

📊 Dataset :

| Source         | Period    | Unit   | Key Column               |
| -------------- | --------- | ------ | ------------------------ |
| EPA/CSIRO/NOAA | 1880–2014 | Inches | CSIRO Adjusted Sea Level |

134 years of global average absolute sea level change measurements.

📊 Dataset Description :

Source: U.S. Environmental Protection Agency (EPA)
Period: 1880 – 2014
Unit: Inches
Key Column Used: CSIRO Adjusted Sea Level
This dataset represents the global average absolute sea level change.

--Methodology

1️⃣ Data Loading
Import CSV data using Pandas
Validate column structure

2️⃣ Visualization
Scatter plot of raw sea level data
Identify long-term upward trends

3️⃣ Statistical Modeling
Linear regression using all available data (1880–2014)
Extended prediction to 2050
Second regression using recent data only (2000–2014)

4️⃣ Prediction & Comparison
Compare long-term vs accelerated recent trends
Visualize both prediction lines on the same chart

📈 Output Visualization
Sea Level Rise Prediction

Legend Explanation:

| Legend   | Description             | Time Period |
| ------------- | ----------------------- | ----------- |
| 🔵 Blue dots  | Historical measurements | 1880–2014   |
| 🔴 Red line   | Long-term trend         | 1880–2050   |
| 🟢 Green line | Recent acceleration     | 2000–2050   |

--Testing

Unit tests provided by freeCodeCamp
Ensures:
Correct plot generation
Correct labels and title
Function output validation

✔️ All tests pass successfully.

--Conclusion

The analysis confirms:
A clear upward trend in global sea levels
A faster rate of increase in recent decades
If current trends continue, sea levels will rise significantly by 2050
This highlights the real-world impact of climate change and the importance of data-driven forecasting.
