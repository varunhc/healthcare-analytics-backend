from db.patients import *
# from bll.helpers import *  # uncomment for plots

def get_patients() -> dict:
    patient_rows = get_all_patients()
    patient_dict = {"data": []}
    for row in patient_rows:
        patient_dict["data"].append(dict(zip(row.keys(), row.values())))
    return patient_dict


def get_freq_patients() -> dict:
    patient_rows = get_frequent_patients()
    patient_dict = {"data": []}
    for row in patient_rows:
        patient_dict["data"].append(dict(zip(row.keys(), row.values())))
    return patient_dict


def get_patient(subject_id) -> dict:
    patient_rows = get_patient_data(subject_id)
    patient_dict = {"data": []}
    for row in patient_rows:
        patient_dict["data"] = dict(zip(row.keys(), row.values()))
    return patient_dict


def get_patients_stats(subject_id) -> dict:
    results = get_patient_statistics(subject_id).to_dataframe()
    results.dropna(subset="valuenum", inplace=True)
    results.sort_values(by="charttime", inplace=True)
    unique_count_label = results.groupby(['label'], as_index=False).count()
    unique_count_label.sort_values(by="valuenum", ascending=False, inplace=True)
    stats_dict = {
        "data": []
    }
    for label in unique_count_label["label"][:25]:
        y = results.loc[results['label'] == label]
        unit = [unit for unit in y["unitname"][:1]][0]
        y = y["valuenum"].to_list()
        stats_dict["data"].append(
            {
                "label": label,
                "unit": unit,
                "values": y
            }
        )

    # plot the patient reading history
    # plot_patient_history(results)
    return stats_dict
