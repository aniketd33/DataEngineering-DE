import logging

from extract import extract_data
from transform import transform_data
from load import load_data


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():

    logging.info("Pipeline started")

    try:

        data = extract_data()

        logging.info("Data extracted")

        transformed_data = transform_data(data)

        logging.info("Data transformed")

        load_data(transformed_data)

        logging.info("Data loaded")

        logging.info("Pipeline completed")

    except Exception as error:

        logging.error("Pipeline failed: %s", error)


if __name__ == "__main__":
    main()