"""
DEMO 3: Organizing a Project
=============================================================
Goal: see a realistic example (a Customer Churn Prediction
project) split into modules, each with ONE clear responsibility:
    data.py           -> load the data
    preprocessing.py  -> clean/transform the data
    model.py          -> train the model
    evaluation.py     -> evaluate the model
    main.py (here)    -> orchestrate everything

Run this file:
    python main.py
"""

import data
import preprocessing
import model as model_module   # renamed to avoid shadowing the `model` variable below
import evaluation

if __name__ == "__main__":
    raw_data = data.load_data()
    clean_data = preprocessing.clean_data(raw_data)
    model = model_module.train(clean_data)
    evaluation.evaluate(model)

    # Compare this short, readable flow to the "without modular
    # programming" version on slide 14, where every step
    # (load_data, clean_data, remove_missing_values,
    # encode_features, train_model, predict, calculate_accuracy,
    # plot_confusion_matrix, ...) was crammed into one flat script.
