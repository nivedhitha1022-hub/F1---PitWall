"""
data_generator.py
─────────────────
Loads the real PitWall_Analytics_Cleaned.xlsx dataset and returns three
clean, typed DataFrames.

Expected repo structure
  app.py
  data_generator.py
  data/
    PitWall_Analytics_Cleaned.xlsx

Sheets used
  • Subscribers
  • Engagement Sessions
  • Revenue MRR
"""

import io
from pathlib import Path
import pandas as pd
import numpy as np

# ── Paths ─────────────────────────────────────────
_HERE = Path(__file__).parent
LOCAL_XLSX = _HERE / "data" / "PitWall_Analytics_Cleaned.xlsx"

GITHUB_URL = (
    "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/"
    "data/PitWall_Analytics_Cleaned.xlsx"
)

_HEADER_ROW = 0


# ── Excel Loader ──────────────────────────────────
def _open_excel():
    if LOCAL_XLSX.exists():
        return pd.read_excel(
            LOCAL_XLSX,
            sheet_name=None,
            header=_HEADER_ROW,
            engine="openpyxl"
        )

    import urllib.request
    with urllib.request.urlopen(GITHUB_URL) as resp:
        return pd.read_excel(
            io.BytesIO(resp.read()),
            sheet_name=None,
            header=_HEADER_ROW,
            engine="openpyxl"
        )


# ── Public Loader ─────────────────────────────────
def load_data():
    """
    Returns
    -------
    subs  : subscriber-level DataFrame
    sess  : session-level DataFrame
    mrr   : monthly MRR summary
    """

    xl = _open_excel()

    required_sheets = [
        "Subscribers",
        "Engagement Sessions",
        "Revenue MRR"
    ]

    missing = [s for s in required_sheets if s not in xl]

    if missing:
        raise ValueError(
            f"Missing expected sheet(s): {missing}. Found: {list(xl.keys())}"
        )

    subs = _clean_subscribers(xl["Subscribers"].copy())
    sess = _clean_sessions(xl["Engagement Sessions"].copy())
    mrr = _clean_mrr(xl["Revenue MRR"].copy())

    return subs, sess, mrr


# ── Cleaning Functions ────────────────────────────
def _clean_subscribers(df):
    df.columns = [str(c).strip() for c in df.columns]

    df["Signup Date"] = pd.to_datetime(df["Signup Date"], errors="coerce")
    df["Churn Date"] = pd.to_datetime(df["Churn Date"], errors="coerce")

    df["Churn Reason"] = df["Churn Reason"].fillna("Not Churned")

    df["churn_flag"] = (df["Churned"] == "Yes").astype(int)

    return df


def _clean_sessions(df):
    df.columns = [str(c).strip() for c in df.columns]

    df["Session Date"] = pd.to_datetime(df["Session Date"], errors="coerce")

    df["Is Weekend"] = (
        df["Is Weekend"]
        .astype(str)
        .str.strip()
        .str.lower()
        .map({
            "true": True,
            "false": False,
            "yes": True,
            "no": False,
            "1": True,
            "0": False
        })
    )

    df["Engagement Score"] = pd.to_numeric(
        df["Engagement Score"], errors="coerce"
    )

    df["Session Duration Min"] = pd.to_numeric(
        df["Session Duration Min"], errors="coerce"
    )

    return df


def _clean_mrr(df):
    df.columns = [str(c).strip() for c in df.columns]

    df["Month"] = pd.to_datetime(
        df["Month"],
        format="%Y-%m",
        errors="coerce"
    )

    return df
