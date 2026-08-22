def validate_data(df):

    required_columns = [
        "id",
        "name",
        "department",
        "salary",
        "experience",
        "joining_date",
        "city"
    ]

    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    if df.empty:
        raise ValueError(
            "Dataset is empty"
        )

    if df["id"].duplicated().any():
        raise ValueError(
            "Duplicate employee IDs found"
        )

    if (df["salary"] <= 0).any():
        raise ValueError(
            "Invalid salary found"
        )

    print("Data validation successful")

    return True