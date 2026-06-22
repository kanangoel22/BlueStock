import pandas as pd
import os

folder = "data/raw"

files = [
    f for f in os.listdir(folder)
    if f.endswith(".csv")
]

for file in files:

    print("\n" + "="*60)
    print("FILE:", file)

    path = os.path.join(folder, file)

    try:

        df = pd.read_csv(path)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nAnomalies:")

        if df.isnull().sum().sum() > 0:
            print("Missing values present")

        if df.duplicated().sum() > 0:
            print("Duplicate rows present")

        if (
            df.isnull().sum().sum()==0
            and
            df.duplicated().sum()==0
        ):
            print("No obvious issues")


    except Exception as e:

        print("Error:", e)

        print("\n")
print("="*60)

fund_master = pd.read_csv(
"data/raw/01_fund_master.csv"
)

print(
"\nUnique Fund Houses:"
)

print(
fund_master[
"fund_house"
].unique()
)

print(
"\nUnique Categories:"
)

print(
fund_master[
"category"
].unique()
)

print(
"\nUnique Sub Categories:"
)

print(
fund_master[
"sub_category"
].unique()
)

print(
"\nUnique Risk Grades:"
)

print(
fund_master[
"risk_category"
].unique()
)


print("\n")
print("="*60)

master_codes = set(
    fund_master["amfi_code"]
)

nav_history = pd.read_csv(
    "data/raw/02_nav_history.csv"
)

nav_codes = set(
    nav_history["amfi_code"]
)

missing_codes = (
    master_codes
    -
    nav_codes
)

print(
"\nTotal Master Codes:",
len(master_codes)
)

print(
"Present in NAV:",
len(master_codes)-len(missing_codes)
)

print(
"Missing:",
len(missing_codes)
)

print(
"\nMissing Codes:"
)

print(
missing_codes
)