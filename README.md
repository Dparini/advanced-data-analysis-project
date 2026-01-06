<div align="center" style="margin: 0 auto; max-width: 80%;">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="src/logo_white.jpg">
    <source media="(prefers-color-scheme: light)" srcset="src/logo_black.jpg">
    <img alt="Logo del progetto" src="./src/logo_black.jpg">
  </picture>
</div>

<div align="center">

# Survival Analysis of VC-Backed Startups

</div>

<div align="center">

![Data Science](https://img.shields.io/badge/Data_Science-Advanced_Data_Analytics-blue)
![Python](https://img.shields.io/badge/Python-3.13%2B-green)
![Status](https://img.shields.io/badge/Status-Capstone_Project-success)
![Institution](https://img.shields.io/badge/Institution-HEC--Lausanne-blue)
![License](https://img.shields.io/badge/License-MIT-green)

**Predicting IPO and Acquisition Timing for Venture Capital-Backed Startups**

[Quick Start](#-quick-start) • [Results](#-key-results) • [Methodology](#-methodology) • [Citation](#-academic-context)

</div>

---

## Project Overview

This project implements a **comprehensive survival analysis framework** to predict the probability and timing of exit events (IPO or acquisition) for VC-backed startups. Employing a **competing risks methodology** where IPO and M&A are treated as mutually exclusive terminal events, this research combines Crunchbase and Jay Ritter datasets to provide deep insights into startup lifecycle dynamics.

### Research Question
*How do various factors,  including funding characteristics, market conditions, network effects, and angel investment, influence the timing and probability of exit events for venture capital-backed startups in the United States?*

---

## Project Structure

```
advanced-data-analysis-project/
├── data/                               # Data directory
│   ├── raw/                           # Raw datasets
│   ├── processed/                     # Intermediate data
│   └── final/
│       └── finale_usa_cleaned.csv    # Main dataset (15,305 startups)
│
├── models/                            # Model outputs
│   ├── model_results.json            # Performance metrics
│   ├── tree.dot & tree.png           # Visualizations
│
├── data_wrangling_eda.ipynb          # EDA and preparation
├── feature_engineering.ipynb         # Feature engineering
├── modeling.ipynb                    # Survival modeling
│
├── src/ 
├── config.py                         # Configuration
├── helper.py                         # Utility functions
├── plotting.py                       # Visualization utilities
├── pyproject.toml                    # Dependencies
├── uv.lock
├── stripout.sh
└── README.md
```

---

## Quick Start

### Prerequisites
- Python 3.13+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

### Installation
```bash
# Clone repository
git clone https://github.com/danieleparini/advanced-data-analysis-project.git
cd advanced-data-analysis-project

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install .               # Basic
pip install ".[dev]"        # With dev tools
# Or with uv:
uv sync                     # Basic
uv sync --extra dev         # With dev tools
```

### Run Analysis Pipeline
```bash
jupyter notebook data_wrangling_eda.ipynb      # 1. Data prep
jupyter notebook feature_engineering.ipynb     # 2. Features
jupyter notebook modeling.ipynb                # 3. Models
```

---

## Key Results

### Dataset Overview

<div align="center">

| Metric | Value | Interpretation |
|--------|-------|----------------|
| **Total Startups** | 15,304 | Final sample |
| **IPO Events** | 125 (0.8%) | Primary success |
| **M&A Events** | 1,513 (9.9%) | Secondary success |
| **Failure Events** | 870 (5.7%) | Competing risk |
| **Median Time-to-IPO** | 4.9 years | From first funding |
| **Success Rate** | 10.7% | IPO + M&A |

</div>

### Model Performance

<div align="center">

| Model | C-Index | Calibration |
|-------|---------|-------------|
| **Cox PH** | **0.648** | 0.048 |
| **Random Survival Forest** | 0.693 | 0.051 |
| **Competing Risks (IPO)** | 0.764 | - |
| **Competing Risks (M&A)** | 0.692 | - |

</div>

### Top 5 Predictors

1. **log_fund_tot** - Log total funding (HR=1.32)
2. **market_heat** - Market conditions
3. **funding_rounds** - Number of rounds
4. **relationships** - Network connections
5. **macro_settore** - Industry sector

---

## Methodology

### 1. Data Integration
- **Crunchbase**: 196,499 companies (1970-2013)
- **Jay Ritter IPO**: 15,697 IPOs (1975-2025)
- **Final Sample**: 15,304 USA startups

### 2. Feature Engineering
```python
# Key transformations:
- Log-transformed funding amounts
- Market cycle classification (Boom/Bust/Normal)
- Macro-sector consolidation (42 → 11 categories)
- Network connectivity scores
```

### 3. Survival Models

| Model | Purpose | Key Metric |
|-------|---------|------------|
| **Kaplan-Meier** | Survival estimation | Median survival time |
| **Cox PH** | Hazards regression | Hazard ratios |
| **Competing Risks** | IPO vs M&A | Cumulative incidence |
| **Random Survival Forest** | ML approach | C-index, Brier score |

---

## Business Insights

### For VCs
-  Boom markets increase IPO probability by **42%**
-  Hardware startups have highest IPO rates (**5.4%**)
-  Series B/C rounds reduce time-to-exit significantly

### For Entrepreneurs
-  Log funding is strongest predictor
-  Strong network connectivity reduces failure hazard by **18%**
-  Market timing matters for outcomes

### For Policymakers
-  Geographic clustering (CA, MA, NY) drives success
-  Network connectivity correlates with regional success
-  IPO activity predicts economic trends

---

## Technical Stack

```python
# Core Dependencies
lifelines >= 0.30.0          # Survival analysis
scikit-survival >= 0.26.0    # Random Survival Forest
pandas >= 2.0.0              # Data processing
matplotlib >= 3.7.0          # Visualization
```

See [`pyproject.toml`](pyproject.toml) for complete list.

---

## Academic Context

### Citation
```
Parini, D. (2025). Survival Analysis of VC-Backed Startups: 
A Competing Risks Approach Using Crunchbase and Jay Ritter Data. 
HEC Lausanne, University of Lausanne.
```

### Acknowledgments
- **Institution**: HEC Lausanne
- **Course**: Advanced Data Analytics (Fall 2025)
- **TAs**: Maria-Pia Lombardo, Anna Smirnova
- **Data**: Crunchbase (via Kaggle), Jay Ritter IPO Database

### Novel Contributions
1. Conservative IPO imputation strategy
2. Macro-sector balanced consolidation
3. Competing risks framework for exits
4. Comprehensive bootstrap validation

---

<div align="center">

### From Data to Decisions

*Advanced survival analysis bridging academic rigor with business applications*

**Daniele Parini** · HEC Lausanne · 2025

[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github)](https://github.com/Dparini/advanced-data-analysis-project)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/daniele-parini-852645259)

</div>

---

## Contact

**Daniele Parini**  
HEC Lausanne, University of Lausanne  
📧 Email: daniele.parini@unil.ch

**Teaching Assistants:**
- Maria-Pia Lombardo (mariapia.lombardo@unil.ch)
- Anna Smirnova (anna.smirnova@unil.ch)

---

## License

MIT License - see [LICENSE](LICENSE) file.

**Note**: External datasets used under respective licenses.

---

<div align="center">
<sub>This README reflects comprehensive analysis from Jupyter notebooks. All results are reproducible.</sub>
</div>
