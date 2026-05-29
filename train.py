import pandas as pd

from pycaret.classification import (
    setup,
    compare_models,
    finalize_model,
    save_model
)

print("Loading dataset...")

df = pd.read_csv("data/column_2C_weka.csv")

print("Training started...")

setup(
    data=df,
    target="class",
    session_id=123,
    verbose=False
)

best_model = compare_models()

final_model = finalize_model(best_model)

save_model(
    final_model,
    "models/model"
)

print("Model Saved Successfully")