# 🇮🇳 India FinTech Capital Intelligence Dashboard (2016–2022)

A data-intensive Power BI dashboard analyzing over **$15 billion** in capital deployed across **3,912 funding rounds**, **512 unique investors**, and **61 Indian cities** between 2016 and 2022. This project transforms raw public data into actionable insight — quantifying capital concentration, sector efficiency, investor conviction, and the ecosystem’s post-peak behavior. Designed as an operator-grade lens for analysts, early-stage VCs, and founders.

---

## 📌 Project Scope

- 📊 **$15B+ capital** across 7 years  
- 🧾 **3,912 deals** refined into **580 high-quality entries** (from 5,047 raw rows)  
- 👥 **512 investors**, including repeat behavior analysis  
- 🌆 **61 cities** across India mapped and normalized  
- 🧠 **11 advanced charts**, **10 card KPIs**, **3 pages**, **4 slicers**  
- 🧪 **9 custom metrics** coded via DAX  
- 🎯 Built entirely in **Power BI**, with preprocessing in **Jupyter + Pandas**

---

## 🗂 Repository Structure
India-FinTech-Capital-Intelligence/
- data_raw/ # Original Kaggle datasets
- data_cleaned/ # Final cleaned CSV + Excel datasets
- notebooks/ # Python scripts for data prep
- dashboard/ # Power BI .pbix + exported PDF
- visuals/ # Screenshots from the dashboard
- README.md
- LICENSE


---

## 🔄 Workflow Summary

1. **Raw data acquisition**  
   - Kaggle datasets (links below)  
   - Converted `.csv` to `.xlsx` using Pandas

2. **Data cleaning & validation**  
   - Merged files and created a unified data model  
   - Filtered non-FinTech companies via manual checks  
   - Standardized investor names, city names, and sector tags  
   - Resolved **2,200+ missing fields manually** (dates, cities, investor roles)

3. **Derived metric creation**  
   - Created 9 custom metrics in Power BI using DAX:
     - `Capital Velocity` = Total Funding / Startup Age
     - `Investor Loyalty Score` = Repeat Investments / Total Investments
     - `Sector Efficiency Index` = Avg. Capital per Deal per Sector
     - YoY % growth in deal count and capital
     - Capital Concentration Ratio
     - Top funded sectors / investors
     - Repeat investor behavior

4. **Dashboard creation**  
   - Designed using uniform color themes and layouts  
   - All visuals filtered with global slicers:
     - Year range  
     - Sector  
     - City  
     - Investor

---

## 📊 Dashboard Breakdown

### 📘 Page 1: Market Overview
- **Line chart:** Annual capital deployed (2016–2022)
- **Bar chart:** Annual deal volume
- **Combo chart:** YoY growth % in capital & deals
- **Donut chart:** Capital Concentration Ratio
- **KPI Cards:** Total capital, Avg. deal size, Peak annual capital year

### 🧭 Page 2: Sector + Geography Lens
- **Treemap:** Capital allocation by sector
- **Donut chart:** Sector-wise deal activity
- **Map:** City-wise capital flow
- **Horizontal bar:** Avg. ticket size per sector
- **KPI Cards:** Top funded sector, Most efficient sector, Fastest growing YoY

### 🧠 Page 3: Investor Behavior Analysis
- **Line area:** Capital Velocity by startup age
- **Ribbon chart:** Investor Repeat Rate
- **Bar chart:** Investors by Capital Deployed
- **KPI Cards:** Top investor, Capital by top investor, Highest repeat rate, Startup with highest velocity

> 🧮 Total: **11 visual charts** + **10 KPI cards** across 3 pages

---

## 📂 Files

| Folder        | Contents                                   |
|---------------|--------------------------------------------|
| `data_raw/`     | Original Kaggle datasets (CSV)             |
| `data_cleaned/` | Final cleaned data (CSV & XLSX)            |
| `notebooks/`    | Python scripts used for preprocessing      |
| `dashboard/`    | `.pbix` file + exportable dashboard PDF    |
| `visuals/`      | Full-resolution screenshots of each page   |

---

## 📈 Live Dashboard (Power BI)

> 🚀 Click to explore the full interactive dashboard on Power BI Service:

🔗 [**Launch India FinTech Capital Intelligence Dashboard**](https://app.powerbi.com/view?r=eyJrIjoiYTQyNjdlZTItODIyZC00MDlhLTgyNDMtMDExMTY0NzEyZjEyIiwidCI6ImUxMGQ5NTc4LWRlNTgtNDUyZC1iMmJiLTY1NGFjZGM5ZmZiNyJ9&embedImagePlaceholder=true)

> *(Best viewed on desktop)*

---

You can still browse screenshots from each page in the [`/visuals`](./visuals) folder if you're offline.

---

## 📎 Data Source Credits

- [Startup Funding Dataset by Arpan129](https://www.kaggle.com/datasets/arpan129/startups-funding-dataset?resource=download)
- [Indian Startup Funding Jan–May 2022 by Omkar Gowda](https://www.kaggle.com/datasets/omkargowda/indian-startups-funding-data-januarymay-2022)

All credit to original authors. Dataset used under fair academic use and cleaned significantly.

---

## 🧪 Tools & Stack

| Tool        | Use Case                            |
|-------------|-------------------------------------|
| **Python (Pandas)** | Cleaning, merging, Excel generation  |
| **Jupyter Notebooks** | Manual exploration and transformation |
| **Power BI** | Dashboard creation, DAX metrics     |
| **Excel** | Data enrichment & formatting checks   |

---

## 👨‍💻 Author

**Sumer Pandey**  
GitHub: [@being-sumer](https://github.com/being-sumer)

---

## 🪪 License

This project is under the **MIT License** — free to use, remix, and build upon with attribution.

---

> ✳️ Designed to expose not just where the capital flowed in India’s FinTech decade — but why. Built for analyst-grade navigation of a $15B+ venture landscape.
=======
