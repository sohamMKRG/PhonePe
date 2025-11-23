import pandas as pd
from pathlib import Path

# -----------------------------
# CONFIGURATION
# -----------------------------
RAW_DATA_DIR = Path("data/raw")           # Put all your CSV files here
OUTPUT_DIR   = Path("data/processed")     # Merged files will be saved here
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------
# STEP 1 — READ ALL CSV FILES
# -----------------------------
csv_files = sorted(RAW_DATA_DIR.glob("*.csv"))

dfs = {}
for f in csv_files:
    df = pd.read_csv(f)
    
    # Remove unnamed index columns
    df = df.loc[:, ~df.columns.str.contains("Unnamed")]
    
    # Standardize column names
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    
    # Store in dictionary
    dfs[f.stem] = df

print("Loaded files:", list(dfs.keys()))

# -----------------------------
# STEP 2 — MERGE EACH CATEGORY
# -----------------------------

# Merge user-related datasets
user_dfs = [
    dfs.get("aggregated_user", pd.DataFrame()),
    dfs.get("map_user", pd.DataFrame()),
    dfs.get("top_user", pd.DataFrame())
]

merged_users = pd.concat(user_dfs, ignore_index=True, sort=False)
merged_users.to_csv(OUTPUT_DIR / "master_users.csv", index=False)
print("Saved master_users.csv with", merged_users.shape[0], "rows")

# Merge transaction-related datasets
transaction_dfs = [
    dfs.get("aggregated_transaction", pd.DataFrame()),
    dfs.get("map_transaction", pd.DataFrame()),
    dfs.get("top_transaction", pd.DataFrame())
]

merged_transactions = pd.concat(transaction_dfs, ignore_index=True, sort=False)
merged_transactions.to_csv(OUTPUT_DIR / "master_transactions.csv", index=False)
print("Saved master_transactions.csv with", merged_transactions.shape[0], "rows")

# -----------------------------
# OPTIONAL: FULL MERGE
# -----------------------------
try:
    full = pd.concat([merged_users, merged_transactions], ignore_index=True, sort=False)
    full.to_csv(OUTPUT_DIR / "master_full.csv", index=False)
    print("Saved master_full.csv with", full.shape[0], "rows")
except:
    print("Full merge skipped (schema mismatch between users and transactions).")
