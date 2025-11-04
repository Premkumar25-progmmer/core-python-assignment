def search_by_disease(patients, disease_name):
    # store matching patients
    result = []
    for p in patients:
        if p["Disease"].lower() == disease_name.lower():
            result.append(p["Name"])
    return result

patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]

search_disease = "Flu"

matched_patients = search_by_disease(patients, search_disease)

print("Patients with", search_disease + ":", matched_patients)
