from google.cloud import bigquery

client = bigquery.Client()


def get_db_tables(db_name):
    QUERY = (
        f'SELECT TABLE_NAME FROM `physionet-data.{db_name}.INFORMATION_SCHEMA.TABLES`'
    )
    query_job = client.query(QUERY)  # API request
    rows = query_job.result()
    return rows


def get_columns_and_type(db_name, table_name):
    QUERY = (
        f'SELECT column_name, data_type FROM `physionet-data.{db_name}.INFORMATION_SCHEMA.COLUMNS` WHERE table_name="{table_name}"')
    query_job = client.query(QUERY)  # API request
    rows = query_job.result()
    return rows
