import logging

from src.extract import extract_data
from src.transform import transform_data
from src.validate import validate_data
from src.load import load_data


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():

    logging.info("ETL Pipeline Started")

    try:

        # Extract
        df = extract_data()

        logging.info(
            "Data extracted: %s rows",
            len(df)
        )

        # Transform
        df = transform_data(df)

        logging.info(
            "Data transformation completed"
        )

        # Validate
        validate_data(df)

        logging.info(
            "Data validation completed"
        )

        # Load
        load_data(df)

        logging.info(
            "Data loading completed"
        )

        logging.info(
            "ETL Pipeline Completed Successfully"
        )

    except Exception as error:

        logging.error(
            "Pipeline failed: %s",
            error
        )

        raise


if __name__ == "__main__":
    main()