import pandas as pd

from src.transform import transform_data


def test_transform_data():

    data = {
        "id": [1, 2],
        "name": [" Aniket ", "Rahul"],
        "department": [
            "data engineering",
            "Data Analytics"
        ],
        "salary": [50000, 60000],
        "experience": [1, 3],
        "joining_date": [
            "2025-01-01",
            "2024-01-01"
        ],
        "city": ["Pune", "Mumbai"]
    }

    df = pd.DataFrame(data)

    result = transform_data(df)

    assert "annual_salary" in result.columns
    assert "joining_year" in result.columns
    assert "experience_level" in result.columns

    assert result["name"].iloc[0] == "Aniket"