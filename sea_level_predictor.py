import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], 
               alpha=0.7, label='Observed Data', color='blue', s=30)
    
    slope, intercept, r_value, p_value, std_err = linregress(
        df['Year'], df['CSIRO Adjusted Sea Level']
    )
    
    years_extended = np.arange(df['Year'].min(), 2051, 1)
    line_of_best_fit = slope * years_extended + intercept
    ax.plot(years_extended, line_of_best_fit, 'r-', 
            label=f'Best Fit (all data): y = {slope:.4f}x + {intercept:.2f}', 
            linewidth=2)
    
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(
        df_recent['Year'], df_recent['CSIRO Adjusted Sea Level']
    )
    
    years_recent = np.arange(2000, 2051, 1)
    line_recent = slope_recent * years_recent + intercept_recent
    ax.plot(years_recent, line_recent, 'g-', 
            label=f'Best Fit (2000+): y = {slope_recent:.4f}x + {intercept_recent:.2f}', 
            linewidth=2)
    
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Sea Level (inches)', fontsize=12)
    ax.set_title('Rise in Sea Level', fontsize=14, fontweight='bold')
    ax.legend(loc='upper left')
    ax.grid(True, alpha=0.3)
    
    prediction_2050_all = slope * 2050 + intercept
    prediction_2050_recent = slope_recent * 2050 + intercept_recent
    
    ax.axhline(y=prediction_2050_all, color='red', linestyle='--', alpha=0.5)
    ax.axhline(y=prediction_2050_recent, color='green', linestyle='--', alpha=0.5)
    
    textstr = f'2050 Predictions:\nAll data: {prediction_2050_all:.2f} inches\nFrom 2000: {prediction_2050_recent:.2f} inches'
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
    ax.text(0.98, 0.02, textstr, transform=ax.transAxes, fontsize=10,
            verticalalignment='bottom', horizontalalignment='right', bbox=props)
    
    plt.tight_layout()
    
    fig.savefig('sea_level_plot.png', dpi=150, bbox_inches='tight')
    print("Plot saved as 'sea_level_plot.png'")
    
    print("\n=== Sea Level Analysis Results ===")
    print(f"Data range: {df['Year'].min()} - {df['Year'].max()}")
    print(f"\nLinear regression (all data):")
    print(f"  Rate of rise: {slope:.4f} inches/year")
    print(f"  R-squared: {r_value**2:.4f}")
    print(f"  2050 prediction: {prediction_2050_all:.2f} inches")
    print(f"\nLinear regression (2000 onwards):")
    print(f"  Rate of rise: {slope_recent:.4f} inches/year")
    print(f"  R-squared: {r_value_recent**2:.4f}")
    print(f"  2050 prediction: {prediction_2050_recent:.2f} inches")
    
    return fig

if __name__ == "__main__":
    draw_plot()
    plt.show()
