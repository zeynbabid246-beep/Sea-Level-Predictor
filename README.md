<div align="center">

# 🌊 Sea Level Predictor
### *Charting the Course of Climate Change Through Data*

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)](https://matplotlib.org/)

**Transforming 134 years of ocean data into tomorrow's forecast**

[Features](#-features) • [Installation](#-quick-start) • [Methodology](#-methodology) • [Results](#-results) • [Contributing](#-contributing)

</div>

---

## 🎯 The Mission

> *"The ocean doesn't lie. Every millimeter tells a story of our planet's transformation."*

Welcome to **Sea Level Predictor** – where raw climate data meets predictive intelligence. This isn't just another data analysis project; it's a **time machine that looks backward to see forward**, turning 134 years of global sea level measurements into actionable insights about our planet's future.

From the gaslit streets of 1880 to the digital age of 2014, we've captured every rise and fall of Earth's oceans. Now, using the power of statistical modeling, we're extending that story through 2050 – revealing trends that demand attention and action.

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🔬 **Scientific Rigor**
- Linear regression modeling with SciPy
- Dual-timeline analysis (1880–2050)
- Recent trend acceleration detection (2000–2014)
- Statistical validation with unit tests

</td>
<td width="50%">

### 🎨 **Visual Storytelling**
- Publication-ready matplotlib visualizations
- Color-coded trend comparisons
- Interactive data exploration
- Professional chart aesthetics

</td>
</tr>
<tr>
<td width="50%">

### 📊 **Data Intelligence**
- 134 years of EPA/CSIRO/NOAA measurements
- Pandas-powered data manipulation
- Missing data handling
- Robust preprocessing pipeline

</td>
<td width="50%">

### 🚀 **Production Ready**
- Modular, maintainable code architecture
- Comprehensive test coverage
- Docker-ready configuration
- Reproducible research standards

</td>
</tr>
</table>

---

## 🌍 Why This Matters

Climate change isn't abstract – it's measurable, predictable, and accelerating. This project demonstrates:

- 🌡️ **The Reality**: Sea levels have risen consistently since 1880
- ⚡ **The Acceleration**: Recent decades show faster increase rates
- 🔮 **The Future**: If current trends continue, significant rise by 2050
- 💡 **The Power**: How data science can quantify environmental change

---

## 📂 Project Architecture

```
Sea-Level-Predictor/
│
├── 📊 data/
│   └── epa-sea-level.csv          # 134 years of ocean measurements
│
├── 🐍 src/
│   ├── sea_level_predictor.py     # Core analysis engine
│   ├── main.py                    # Execution entry point
│   └── tests/
│       └── test_module.py         # Comprehensive unit tests
│
├── 📈 outputs/
│   └── sea_level_plot.png         # Your climate visualization
│
├── 📋 requirements.txt            # Dependency manifest
└── 📖 README.md                   # You are here
```

---

## 🚀 Quick Start

### Prerequisites

```bash
Python 3.8+ | pip | virtualenv (recommended)
```

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/sea-level-predictor.git
cd sea-level-predictor

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run the Analysis

```bash
# Execute the predictor
python src/main.py

# Run tests
python -m unittest src/tests/test_module.py
```

### Expected Output

Your terminal will display test results, and a publication-quality visualization will be generated in `outputs/sea_level_plot.png`.

---

## 🔬 Methodology

<details>
<summary><b>🔵 Phase 1: Data Acquisition & Preprocessing</b></summary>

<br>

```python
# Load historical data
import pandas as pd
df = pd.read_csv('data/epa-sea-level.csv')
```

- **Source**: U.S. Environmental Protection Agency (EPA)
- **Collaboration**: CSIRO & NOAA datasets
- **Coverage**: 1880–2014 (134 annual measurements)
- **Metric**: Global average absolute sea level change (inches)

</details>

<details>
<summary><b>🔴 Phase 2: Exploratory Data Analysis</b></summary>

<br>

- Scatter plot generation of raw measurements
- Trend identification and validation
- Temporal pattern recognition
- Outlier detection and handling

</details>

<details>
<summary><b>🟢 Phase 3: Statistical Modeling</b></summary>

<br>

**Model 1: Long-Term Historical Trend (1880–2014)**
```python
from scipy import stats
slope, intercept, r_value, p_value, std_err = stats.linregress(years, sea_levels)
```
- Baseline climate trajectory
- 134-year comprehensive analysis
- Extended forecast to 2050

**Model 2: Recent Acceleration (2000–2014)**
- Captures modern warming effects
- Reflects accelerated ice melt
- Shows departure from historical norms

</details>

<details>
<summary><b>🟡 Phase 4: Prediction & Visualization</b></summary>

<br>

- Dual-model comparison
- Matplotlib publication-quality charts
- Color-coded trend lines for clarity
- Professional scientific aesthetics

</details>

---

## 📊 Dataset Deep Dive

| Attribute | Details |
|-----------|---------|
| **Source Organizations** | EPA • CSIRO • NOAA |
| **Temporal Span** | 1880 → 2014 (134 years) |
| **Measurement Unit** | Inches (relative to baseline) |
| **Primary Column** | `CSIRO Adjusted Sea Level` |
| **Data Points** | 134 annual averages |
| **Geographic Scope** | Global average |
| **Quality** | Research-grade, peer-reviewed |

---

## 📈 Results

### The Visualization

The generated plot reveals three critical data layers:

<div align="center">

| **Visual Element** | **Meaning** | **Time Span** | **Insights** |
|:------------------:|-------------|:-------------:|--------------|
| 🔵 **Blue Scatter** | Raw historical measurements | 1880–2014 | Original EPA dataset |
| 🔴 **Red Trend Line** | Long-term linear regression | 1880–2050 | Historical baseline trajectory |
| 🟢 **Green Trend Line** | Recent acceleration model | 2000–2050 | Modern warming effects |

</div>

### Key Findings

1. **Undeniable Trend**: Clear upward trajectory over 134 years
2. **Acceleration Evidence**: Green line diverges from red, showing faster recent rise
3. **Future Projection**: Both models predict continued significant increase by 2050
4. **Data Quality**: Strong correlation coefficients validate model reliability

---

## 🛠️ Tech Stack

<div align="center">

| Category | Technologies |
|:--------:|:------------:|
| **Core Language** | ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) |
| **Data Manipulation** | ![Pandas](https://img.shields.io/badge/-Pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/-NumPy-013243?style=flat-square&logo=numpy&logoColor=white) |
| **Statistical Analysis** | ![SciPy](https://img.shields.io/badge/-SciPy-8CAAE6?style=flat-square&logo=scipy&logoColor=white) |
| **Visualization** | ![Matplotlib](https://img.shields.io/badge/-Matplotlib-11557c?style=flat-square) ![Seaborn](https://img.shields.io/badge/-Seaborn-3776AB?style=flat-square) |
| **Testing** | ![unittest](https://img.shields.io/badge/-unittest-3776AB?style=flat-square&logo=python&logoColor=white) |
| **Development** | ![Git](https://img.shields.io/badge/-Git-F05032?style=flat-square&logo=git&logoColor=white) ![VS Code](https://img.shields.io/badge/-VS_Code-007ACC?style=flat-square&logo=visual-studio-code&logoColor=white) |

</div>

---

## ✅ Testing

Comprehensive unit test suite ensures:

- ✔️ Correct plot generation
- ✔️ Accurate axis labels and titles
- ✔️ Proper legend entries
- ✔️ Function output validation
- ✔️ Data integrity checks
- ✔️ Regression model accuracy

```bash
# Run all tests
python -m unittest discover src/tests/

# Expected output:
# ......
# ----------------------------------------------------------------------
# Ran 6 tests in 0.234s
# OK
```

---

## 🎓 Learning Outcomes

This project demonstrates mastery of:

- **Data Science Workflow**: From raw data to publication
- **Statistical Modeling**: Linear regression and trend forecasting
- **Python Ecosystem**: Leveraging pandas, scipy, matplotlib
- **Scientific Computing**: Reproducible research practices
- **Climate Science**: Understanding sea level rise metrics
- **Software Engineering**: Modular design, testing, documentation

---

## 🌟 Future Enhancements

<table>
<tr>
<td>

### 🔮 Planned Features
- [ ] Interactive web dashboard (Plotly/Dash)
- [ ] Multiple regression models comparison
- [ ] Regional sea level analysis
- [ ] API integration for real-time data
- [ ] Machine learning predictions (LSTM)

</td>
<td>

### 💡 Ideas Welcome
- [ ] Confidence interval visualization
- [ ] Climate scenario modeling
- [ ] Satellite data integration
- [ ] Animated historical visualization
- [ ] Export to multiple formats

</td>
</tr>
</table>

---

## 🤝 Contributing

Contributions are welcome! Whether you're fixing bugs, improving documentation, or proposing new features:

1. **Fork** the repository
2. **Create** your feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **freeCodeCamp** for project inspiration and test framework
- **EPA, CSIRO, NOAA** for maintaining critical climate datasets
- **Python Data Science Community** for exceptional open-source tools
- **Climate Scientists** worldwide for their ongoing research

---

## 📬 Connect

<div align="center">

**Found this project useful? Give it a ⭐!**

[![GitHub](https://github.com/zeynbabid246-beep)
[![LinkedIn](https://www.linkedin.com/in/zeynb-abid-099453300/)
[![Email](zeynbabid246@gmail.com)

---

<sub>Built with 💙 for our planet | Data doesn't lie, but it does tell stories</sub>

</div>
