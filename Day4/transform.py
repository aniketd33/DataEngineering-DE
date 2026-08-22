import pandas as pd


def transform_data(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    # Clean column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
    )

    # Clean text columns
    df["name"] = (
        df["name"]
        .str.strip()
        .str.title()
    )

    df["department"] = (
        df["department"]
        .str.strip()
        .str.title()
    )

    df["city"] = (
        df["city"]
        .str.strip()
        .str.title()
    )

    # Convert salary to numeric
    df["salary"] = pd.to_numeric(
        df["salary"],
        errors="coerce"
    )

    # Convert experience
    df["experience"] = pd.to_numeric(
        df["experience"],
        errors="coerce"
    )

    # Convert date
    df["joining_date"] = pd.to_datetime(
        df["joining_date"],
        errors="coerce"
    )

    # Handle missing values
    df["department"] = df["department"].fillna("Unknown")
    df["salary"] = df["salary"].fillna(
        df["salary"].median()
    )

    # Remove duplicates
    df = df.drop_duplicates()

    # Create new columns
    df["annual_salary"] = df["salary"] * 12

    df["joining_year"] = (
        df["joining_date"].dt.year
    )

    # Experience level
    df["experience_level"] = df["experience"].apply(
        lambda x:
        "Senior" if x >= 4
        else "Mid-Level" if x >= 2
        else "Junior"
    )

    return df