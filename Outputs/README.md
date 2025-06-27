# 📂 Outputs

This directory contains auto-generated output artifacts created by agent workflows defined in the notebooks under `/Agents/`.

Each subfolder corresponds to a specific agentic notebook and includes any generated `.py`, `.png`, or other intermediate files.

## Overview

### `Coding-Financial Analysis/`

Contains outputs from `Agentic-Coding-FinancialAnalysis.ipynb`, a multi-agent workflow that:
- Retrieves YTD stock data for NVDA and TSLA
- Plots financial trends
- Saves both code and image outputs automatically

**Files include:**
- `functions.py`  
- `Get the current date`  
- `plot_ytd_stock_gains.py`  
- `stock_prices_YTD_plot.png`  
- `tmp_code_8d25e8e03369296cea541b9cc6072fa4.py`  
- `tmp_code_bebc51d0b530ac09dd1c62bdee846e49.sh`  
- `ytd_stock_gains.png`  

---

### `Financial Report Generator/`

Contains outputs from `Agentic-Financial-Analysis-ReportGenerator.ipynb`, a workflow that:
- Gathers recent news articles about selected stocks (e.g., NVDA)
- Summarizes findings into a financial narrative

**Files include:**
- `fetch_nvidia_news.py`