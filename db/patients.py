from google.cloud import bigquery

client = bigquery.Client()


def get_all_patients():
    result = []
    try:
        max_rows = 10
        QUERY = (
            f'SELECT subject_id, anchor_age, anchor_year, dod, gender FROM `physionet-data.mimiciv_hosp.patients` LIMIT {max_rows}'
        )
        query_job = client.query(QUERY)  # API request
        result = query_job.result()
    except Exception as e:
        print(f"Couldn't fetch info. Error: {e}")
    return result


def get_patient_data(subject_id):
    result = []
    try:
        max_rows = 1
        QUERY = (
            f'SELECT patients.subject_id, patients.anchor_age, patients.anchor_year, patients.dod, patients.gender, admissions.insurance, admissions.marital_status, admissions.race, admissions.hadm_id, admissions.admission_location FROM `physionet-data.mimiciv_hosp.patients` as patients left join `physionet-data.mimiciv_hosp.admissions` as admissions on patients.subject_id=admissions.subject_id WHERE patients.subject_id={subject_id} LIMIT {max_rows}'
        )
        query_job = client.query(QUERY)  # API request
        result = query_job.result()
    except Exception as e:
        print(f"Couldn't fetch info. Error: {e}")
    return result
