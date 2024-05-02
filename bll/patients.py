from db.patients import *


def get_patients():
    patient_rows = get_all_patients()
    patient_dict = {"data": []}
    for row in patient_rows:
        patient_dict["data"].append(dict(zip(row.keys(), row.values())))
    return patient_dict


def get_patient(subject_id):
    patient_rows = get_patient_data(subject_id)
    patient_dict = {"data": []}
    for row in patient_rows:
        patient_dict["data"] = dict(zip(row.keys(), row.values()))
    return patient_dict
