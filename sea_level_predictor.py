import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
from typing import cast


def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # ===============================
    # Line of best fit (1880–2050)
    # ===============================
    result = cast(object, linregress(df["Year"],
                                     df["CSIRO Adjusted Sea Level"]))

    years_extended = range(1880, 2051)
    slope = result.slope  # type: ignore
    intercept = result.intercept  # type: ignore
    sea_level_predicted = [slope * year + intercept for year in years_extended]

    plt.plot(years_extended, sea_level_predicted)

    # ==========================================
    # Line of best fit (2000–2050 recent trend)
    # ==========================================
    df_recent = df[df["Year"] >= 2000]
    recent_result = cast(
        object,
        linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"]))

    recent_years = range(2000, 2051)
    recent_slope = recent_result.slope  # type: ignore
    recent_intercept = recent_result.intercept  # type: ignore
    recent_predicted = [
        recent_slope * year + recent_intercept for year in recent_years
    ]

    plt.plot(recent_years, recent_predicted)

    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save and return plot
    plt.savefig("sea_level_plot.png")
    return plt.gca()
