from sqlalchemy import BOOLEAN, NUMERIC, DATE, Float, Integer, String, DATETIME


DB_NAMES = {
    "mimiciv_ecg": {
        "pk": {
            "record_list": "study_id"
            }
    },
    "mimiciv_hosp": {
        "pk":
            {
            }
    },
    "mimiciv_icu": {
        "pk":
            {
            "caregiver": "caregiver_id",
            "icustays": "stay_id",
            "d_items": "itemid"
            }
    },
    "mimiciv_derived": {
        "pk":
            {
            }
    }
}

TYPE_MAP = {
    "INT64": Integer,
    "STRING": String,
    "DATETIME": DATETIME,
    "FLOAT64": Float,
    "DATE": DATE,
    "NUMERIC": NUMERIC,
    "BOOL": BOOLEAN
}
