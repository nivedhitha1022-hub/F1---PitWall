# 🏎 PitWall Analytics Dashboard

**B2C F1 Performance Data Platform — Subscriber Retention Intelligence**

A full-stack Streamlit analytics dashboard answering: *"Is this business operationally efficient enough to be sustainable?"* Built on the real PitWall subscriber dataset — 800 subscribers, 29,240 sessions, Jan 2023 – Dec 2024.

---

## 📊 Dashboard Overview

| Tab | Question answered | Key visuals |
|-----|------------------|-------------|
| 📋 **Descriptive** | Who are our subscribers? | KPI cards · MRR trend · Plan retention · NPS · Acquisition channels |
| 🔍 **Diagnostic** | Why are they churning? | Churn violins · Region heatmap · Churn reason treemap · Correlation matrix |
| 🔮 **Predictive** | Who will churn next? | Random Forest · ROC curve · Feature importance · KMeans segmentation · Risk watchlist |
| 🎯 **Prescriptive** | What should we do? | Uplift model · A/B test simulator · CLV forecast · 6 strategic recommendations |

---

## 🚀 Run Locally

```bash
# 1. Unzip / clone the project
cd pitwall-dashboard

# 2. Install dependencies  (Python 3.10+ recommended)
pip install -r requirements.txt

# 3. Start the dashboard
streamlit run app.py
```

The app loads `data/PitWall_Analytics_Cleaned.xlsx` automatically.

---

## ☁️ Deploy on Streamlit Cloud

1. Push this folder to a **GitHub repository** (keep folder structure intact)
2. Open `data_generator.py` and update `GITHUB_URL` with the raw file URL:
   ```python
   GITHUB_URL = "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/data/PitWall_Analytics_Cleaned.xlsx"
   ```
3. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**
4. Connect your repo · set **Main file path** → `app.py`
5. Click **Deploy** — done.

---

## 📁 Project Structure

```
pitwall-dashboard/
├── app.py                     ← Entry point  (streamlit run app.py)
├── data_generator.py          ← Data loading & cleaning
├── model_utils.py             ← Feature engineering · RF model · KMeans
├── theme.py                   ← F1 colour palette · CSS · Plotly helpers
├── tab1_descriptive.py        ← Tab 1: KPIs · plan retention · MRR · NPS
├── tab2_diagnostic.py         ← Tab 2: Churn drivers · heatmaps · correlations
├── tab3_predictive.py         ← Tab 3: ML model · risk scoring · segmentation
├── tab4_prescriptive.py       ← Tab 4: Uplift · A/B sim · CLV · recommendations
├── requirements.txt
├── README.md
├── .streamlit/
│   └── config.toml            ← Dark F1 theme
└── data/
    └── PitWall_Analytics_Cleaned.xlsx
```

---

## 🔬 Methods Summary

| Method | Where | Purpose |
|--------|-------|---------|
| Pearson Correlation Matrix | Diagnostic | Identify strongest churn drivers |
| Random Forest Classifier | Predictive | Predict churn probability per subscriber |
| Gini Feature Importance | Predictive | Rank what drives churn most |
| ROC / Confusion Matrix | Predictive | Model performance evaluation |
| KMeans Segmentation (k=4) | Predictive | Behavioural clustering |
| Uplift Modelling | Prescriptive | Identify Persuadables vs Sure Things |
| Chi-squared A/B Test | Prescriptive | Statistical significance of campaigns |
| 6-Month CLV Forecast | Prescriptive | Revenue-at-risk prioritisation |

---

## 📋 Dataset Columns

**Subscribers** (800 rows) — `Subscriber Id`, `Plan`, `Monthly Price Usd`, `Region`, `Age`, `Age Group`, `Acquisition Channel`, `Churned`, `Churn Reason`, `Tenure Months`, `Renewal Count`, `Lifetime Revenue Usd`, `Nps Score`, `Nps Category`, `Plan Upgrade`

**Engagement Sessions** (29,240 rows) — `Subscriber Id`, `Session Date`, `Session Weekday`, `Is Weekend`, `Content Type`, `Engagement Score`, `Engagement Tier`, `Session Duration Min`, `Device`

**Revenue MRR** (72 rows) — `Month`, `Plan`, `Active Subscribers`, `Mrr Usd`, `Arpu Usd`, `Churn Rate Pct`, `Mrr Mom Growth Pct`

---

*Synthetic dataset · PitWall Analytics Individual Assignment*
