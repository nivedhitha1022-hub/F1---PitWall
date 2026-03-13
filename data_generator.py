"""
data_generator.py
─────────────────
Loads the real PitWall_Analytics_Cleaned.xlsx dataset and returns three
clean, typed DataFrames.  Falls back to a GitHub raw URL when running on
Streamlit Cloud (update GITHUB_URL before deploying).

Sheets used
  • Subscribers        800 rows × 18 cols
  • Engagement Sessions 29,240 rows × 10 cols
  • Revenue MRR         72 rows × 9 cols
"""

from __future__ import annotations
import io
from pathlib import Path
import pandas as pd
import numpy as np

# ── Paths ─────────────────────────────────────────────────────────────────────
_HERE       = Path(__file__).parent
LOCAL_XLSX  = _HERE / "data" / "PitWall_Analytics_Cleaned.xlsx"

# !! Replace with your actual GitHub raw URL before deploying to Streamlit Cloud !!
GITHUB_URL = (
    "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main"
    "/data/PitWall_Analytics_Cleaned.xlsx"
)

_HEADER_ROW = 2     # The Excel file has the real headers on row 3 (0-indexed = 2)


def _open_excel() -> dict[str, pd.DataFrame]:
    if LOCAL_XLSX.exists():
        return pd.read_excel(LOCAL_XLSX, sheet_name=None, header=_HEADER_ROW)
    import urllib.request
    with urllib.request.urlopen(GITHUB_URL) as resp:
        return pd.read_excel(io.BytesIO(resp.read()), sheet_name=None,
                             header=_HEADER_ROW)


def load_data() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Returns
    -------
    subs  : subscriber-level DataFrame   (800 rows)
    sess  : session-level DataFrame      (29 240 rows)
    mrr   : monthly MRR summary          (72 rows)
    """
    xl   = _open_excel()
    subs = _clean_subscribers(xl["Subscribers"].copy())
    sess = _clean_sessions(xl["Engagement Sessions"].copy())
    mrr  = _clean_mrr(xl["Revenue MRR"].copy())
    return subs, sess, mrr


# ── Private cleaners ──────────────────────────────────────────────────────────

def _clean_subscribers(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [c.strip() for c in df.columns]
    df["Signup Date"] = pd.to_datetime(df["Signup Date"], errors="coerce")
    df["Churn Date"]  = pd.to_datetime(df["Churn Date"],  errors="coerce")
    df["Churn Reason"] = df["Churn Reason"].fillna("Not Churned")
    df["churn_flag"]  = (df["Churned"] == "Yes").astype(int)
    return df


def _clean_sessions(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [c.strip() for c in df.columns]
    df["Session Date"] = pd.to_datetime(df["Session Date"], errors="coerce")
    df["Is Weekend"]   = df["Is Weekend"].astype(bool)
    df["Engagement Score"]    = pd.to_numeric(df["Engagement Score"],    errors="coerce")
    df["Session Duration Min"]= pd.to_numeric(df["Session Duration Min"],errors="coerce")
    return df


def _clean_mrr(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [c.strip() for c in df.columns]
    df["Month"] = pd.to_datetime(df["Month"], format="%Y-%m", errors="coerce")
    return df
