def _open_excel() -> dict[str, pd.DataFrame]:
    if LOCAL_XLSX.exists():
        return pd.read_excel(
            LOCAL_XLSX,
            sheet_name=None,
            header=_HEADER_ROW,
            engine="openpyxl"
        )

    # Optional GitHub fallback
    if "YOUR_USERNAME" not in GITHUB_URL and "YOUR_REPO" not in GITHUB_URL:
        import urllib.request
        with urllib.request.urlopen(GITHUB_URL) as resp:
            return pd.read_excel(
                io.BytesIO(resp.read()),
                sheet_name=None,
                header=_HEADER_ROW,
                engine="openpyxl"
            )

    raise FileNotFoundError(
        f"Dataset not found at {LOCAL_XLSX}. "
        "Place 'PitWall_Analytics_Cleaned.xlsx' inside the 'data' folder "
        "or update GITHUB_URL with the correct raw GitHub file link."
    )
