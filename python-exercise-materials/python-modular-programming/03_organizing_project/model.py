"""model.py - responsible for TRAINING the model. Nothing else."""

def train(dataset):
    print(f"[model] Training on {dataset['rows']} rows...")
    return {"trained_on_rows": dataset["rows"], "accuracy": None}
