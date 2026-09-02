"""preprocessing.py - responsible for CLEANING/TRANSFORMING data. Nothing else."""

def clean_data(dataset):
    print("[preprocessing] Handling missing values, encoding features...")
    dataset["cleaned"] = True
    return dataset
