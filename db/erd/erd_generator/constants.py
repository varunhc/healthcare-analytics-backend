from sqlalchemy import BOOLEAN, NUMERIC, DATE, Float, Integer, String, DATETIME


DB_NAMES = {
    "mimiciv_ecg": {
        "pk": {
            "record_list": ["study_id"]
            }
    },
    "mimiciv_hosp": {
        "pk":
            {
                "patients": ["subject_id"],
                "admissions": ["hadm_id"],
                "provider": ["provider_id", "admit_provider_id", "enter_provider_id", "order_provider_id"],
                "d_hcpcs": ["code", "hcpcs_cd"],
                "d_labitems": ["itemid"],
                "emar": ["emar_id"],
                "microbiologyevents": ["microevent_id"],
                "pharmacy": ["pharmacy_id"],
                "poe": ["poe_id"],
            }
    },
    "mimiciv_icu": {
        "pk":
            {
            "caregiver": ["caregiver_id"],
            "icustays": ["stay_id"],
            "d_items": ["itemid"]
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
