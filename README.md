# Valuation of Industry Peers — FMCG Sector

![Finance Banner](https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&q=80&w=1000)

## 📌 Project Overview
This project presents a comprehensive relative valuation of 7 leading companies within the Fast-Moving Consumer Goods (FMCG) sector (conducted between May 2026 - July 2026). The analysis benchmarks key performance and valuation metrics against industry averages to identify overvalued and undervalued assets. 

Additionally, it features an in-depth 3-statement financial model for **Britannia Industries**, projecting revenue, margins, and free cash flows over a 5-year horizon to conduct a Discounted Cash Flow (DCF) analysis.

## 🎯 Key Findings
*   **Relative Valuation**: Assessed peers using **EV/EBITDA**, **P/E**, and **P/B** multiples. Concluded that Britannia Industries is fairly valued on relative multiples compared to its closest competitors.
*   **Intrinsic Valuation (DCF)**: Based on base-case assumptions, Britannia Industries appears **overvalued** on a standalone DCF basis.
*   **Validation**: Conclusions are supported by rigorous historical ratio analysis and multi-variable sensitivity testing (adjusting WACC and Terminal Growth Rates).

## 🧰 Tools & Methodologies Used
*   **Financial Modeling**: Built dynamic 3-statement models projecting 5-year horizons.
*   **Valuation Methods**: Comparable Company Analysis (Comps), Discounted Cash Flow (DCF).
*   **Tools**: Microsoft Excel (Core Model), Python (Pandas, yfinance for automated Comps analysis).

## 📁 Repository Structure
```text
├── data/                       # Historical financial data and industry averages
├── models/                     # Excel-based 3-statement financial model and DCF
├── scripts/                    # Python scripts for data fetching and relative valuation
│   ├── fetch_data.py           # Uses yfinance to pull historical ticker data
│   └── relative_valuation.ipynb# Jupyter Notebook for automated peer comparison
└── README.md
```

## 🚀 Getting Started

### Prerequisites
To run the automated Python valuation scripts, ensure you have the following installed:
```bash
pip install pandas yfinance matplotlib seaborn jupyter
```

### Running the Python Scripts
1. Navigate to the `scripts/` directory.
2. Run the data fetching script to pull the latest financials:
   ```bash
   python fetch_data.py
   ```
3. Open and run all cells in `relative_valuation.ipynb` to view the Comparable Company Analysis.

### Viewing the Excel Model
Navigate to the `models/` directory and place your `.xlsx` 3-statement model there. Open it in Microsoft Excel to review the detailed financial projections, DCF, and sensitivity analysis.
