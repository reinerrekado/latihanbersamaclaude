"""
DEMO 1: Why We Need Modular Programming
=============================================================
Goal: see the problem first - a single, growing file that mixes
every responsibility together - before we learn the fix (splitting
code into modules) in the rest of this folder.
"""

# -------------------------------------------------
# 1. The "monolith": everything crammed into one file
# -------------------------------------------------
# Imagine a machine learning script that keeps growing. Every new
# feature just gets added as another function in the SAME file.
def clean_text(text):
    return text.strip().lower()

def preprocess_text(text):
    return clean_text(text).split()

def train_model(tokens):
    print(f"Training on {len(tokens)} tokens...")
    return {"trained": True}

def evaluate_model(model):
    print("Evaluating model...")
    return {"accuracy": 0.9}

def plot_result(metrics):
    print(f"Plotting accuracy = {metrics['accuracy']}")

# ... and in a real project, imagine 500 more lines / functions here:
# load_data(), save_model(), tune_hyperparameters(), send_report(), ...

# -------------------------------------------------
# 2. It still "works"...
# -------------------------------------------------
tokens = preprocess_text("  Machine Learning is FUN  ")
model = train_model(tokens)
metrics = evaluate_model(model)
plot_result(metrics)

print("-" * 40)

# -------------------------------------------------
# 3. ...but it doesn't SCALE. As this file grows past a few
#    hundred lines, it becomes:
# -------------------------------------------------
print("""
Problems with one giant file:
  - Difficult to read       (where is the text-cleaning logic??)
  - Difficult to maintain   (one typo can break unrelated features)
  - Difficult to debug      (everything shares the same namespace)
  - Difficult to reuse      (can't reuse train_model() elsewhere
                              without dragging the whole file along)
  - Difficult to collaborate (everyone edits the same file -> merge
                              conflicts)
""")

# -------------------------------------------------
# 4. The fix: modular programming
# -------------------------------------------------
# Instead of ONE file with everything, we divide the program into
# smaller, reusable files (modules), each with ONE responsibility:
#   preprocessing.py -> clean_text(), preprocess_text()
#   model.py          -> train_model()
#   evaluation.py     -> evaluate_model()
#   visualization.py  -> plot_result()
#   main.py           -> imports all of the above and runs them
#
# See 02_first_module/ for how creating and importing a module
# actually works.
print("See 02_first_module/ next.")
