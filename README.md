# Valuation of Industry Peers — FMCG Sector (India)

Relative valuation and 3-statement financial model for Britannia Industries Ltd, benchmarked against six listed FMCG peers: Hindustan Unilever, ITC, Nestlé India, Dabur India, Godrej Consumer Products, and Marico.

**Model file:** [Britannia_FMCG_Peer_Valuation_Model.xlsx](./Britannia_FMCG_Peer_Valuation_Model.xlsx)

## Objective

Assess whether Britannia Industries is fairly valued relative to (i) its FMCG peer group and (ii) its own intrinsic cash-flow-based value, using two independent valuation approaches.

## Methodology

| Step | Description |
|---|---|
| 1. Peer selection | Six listed Indian FMCG companies spanning diversified FMCG, packaged foods, and personal care |
| 2. Comparable Company Analysis | EV/EBITDA, P/E, and P/B multiples calculated and benchmarked against peer averages and medians |
| 3. Three-statement model | Income statement, simplified balance sheet, and cash flow statement for Britannia — FY2024A–FY2026A actuals, FY2027E–FY2031E projections |
| 4. DCF valuation | Five-year unlevered free cash flow projection and Gordon Growth terminal value, discounted at WACC |
| 5. Sensitivity analysis | Implied share price across a range of WACC and terminal growth rate assumptions |

## Key Findings

- Britannia trades at approximately 34.8x EV/EBITDA and 49.1x P/E (FY2026A), versus peer averages of approximately 33.5x and 47.7x respectively — broadly in line, with a modest premium.
- A base-case DCF (WACC of 11%, terminal growth rate of 5%) implies a fair value of approximately ₹2,250 per share, against a market price of approximately ₹5,171 per share.
- Approximately 76% of the DCF's enterprise value is attributable to the terminal value; the valuation gap narrows materially only under more optimistic long-run assumptions (lower WACC, higher terminal growth).
- Conclusion: Britannia appears fairly valued to modestly overvalued on relative multiples, and overvalued relative to a conservative intrinsic (DCF) estimate — consistent with the market pricing in growth durability beyond the explicit five-year forecast period.

## Tools and Methods

Excel, Comparable Company Analysis, Three-Statement Financial Modeling, Discounted Cash Flow Analysis, Sensitivity Analysis

## Repository Structure

```
├── Britannia_FMCG_Peer_Valuation_Model.xlsx
└── README.md
```

**Workbook contents:**

1. `Cover` — scope, peer set, and data sources
2. `Comps` — comparable company analysis
3. `3-Statement Model` — historical actuals and five-year projections, with editable assumptions
4. `DCF Valuation` — free cash flow discounting and terminal value
5. `Sensitivity` — WACC and terminal growth rate sensitivity grid
6. `Valuation Summary` — consolidated findings and conclusion

## Data Sources

Company financials sourced from Screener.in, compiled from audited consolidated financial statements filed with the BSE/NSE, for FY2026 (year ended March 2026). Market data as of early June 2026. Full source references and assumptions are documented in-cell within the workbook.

## Limitations

This model uses simplified balance sheet and cash flow assumptions (e.g., non-core investments and other liabilities held flat or estimated) appropriate for a peer benchmarking exercise, not a full sell-side model. Two peer companies (Godrej Consumer, Marico) use estimated EBITDA margins where precise disclosure was not available; these are flagged in the workbook. All projections are illustrative and based on the stated assumptions, which can be adjusted in the model.

