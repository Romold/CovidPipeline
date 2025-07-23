import logging
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

logging.basicConfig(filename="logs/pipeline.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def run():
    try:
        logging.info("Pipeline started.")

        raw_file = extract_data()
        logging.info(f"Extracted data to {raw_file}")

        clean_file = transform_data(raw_file)
        logging.info(f"Transformed data to {clean_file}")

        load_data(clean_file)
        logging.info("Data loaded into database.")

        logging.info("Pipeline completed successfully.")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")

if __name__ == "__main__":
    run()
