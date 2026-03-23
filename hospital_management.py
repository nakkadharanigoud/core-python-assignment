
def search_by_disease(patients, disease):
    """Return list of patient names with the given disease."""
    result = [p["Name"] for p in patients if p["Disease"].lower() == disease.lower()]
    return result if result else ["No patients found."]


if __name__ == "__main__":
    patients = [
        {"Name": "Alice", "Age": 30, "Disease": "Flu"},
        {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
        {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
    ]
    search_disease = "Flu"
    result = search_by_disease(patients, search_disease)
    print(f"Patients with {search_disease}: {result}")
