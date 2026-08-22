from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]


def load_data(df):

    output_dir = BASE_DIR / "output"

    output_dir.mkdir(
        exist_ok=True
    )

    output_file = (
        output_dir / "clean_employees.csv"
    )

    df.to_csv(
        output_file,
        index=False
    )

    print(
        f"Clean data saved to: {output_file}"
    )