# Sea Level Predictor

## Overview
A Python data analysis project that analyzes historical sea level data and generates predictions for future sea levels using linear regression.

## Project Structure
- `sea_level_predictor.py` - Main script that performs data analysis and generates visualizations
- `epa-sea-level.csv` - Historical sea level data from 1880-2013
- `sea_level_plot.png` - Generated visualization showing sea level trends

## How to Run
Run the workflow "Sea Level Predictor" or execute:
```bash
python sea_level_predictor.py
```

## Dependencies
- pandas - Data manipulation
- matplotlib - Visualization
- scipy - Statistical analysis (linear regression)
- numpy - Numerical operations

## Output
The script produces:
1. A plot saved as `sea_level_plot.png` showing:
   - Historical sea level observations
   - Best fit line using all data (1880-2013)
   - Best fit line using recent data (2000-2013)
   - Predictions for 2050
2. Console output with statistical analysis results
