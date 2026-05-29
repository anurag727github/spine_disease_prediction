from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

from pycaret.classification import load_model, predict_model

app = FastAPI(
    title="Spine Disorder Prediction API",
    version="1.0.0"
)

# Load trained model
model = load_model("models/model")


class PatientData(BaseModel):
    pelvic_incidence: float
    pelvic_tilt: float
    lumbar_lordosis_angle: float
    sacral_slope: float
    pelvic_radius: float
    degree_spondylolisthesis: float


@app.get("/")
def home():
    return {
        "message": "Spine Disorder Prediction API Running"
    }


@app.post("/predict")
def predict(data: PatientData):
    try:

        # IMPORTANT:
        # Use EXACT column names from training dataset
        df = pd.DataFrame([{
            "pelvic_incidence": data.pelvic_incidence,
            "pelvic_tilt numeric": data.pelvic_tilt,
            "lumbar_lordosis_angle": data.lumbar_lordosis_angle,
            "sacral_slope": data.sacral_slope,
            "pelvic_radius": data.pelvic_radius,
            "degree_spondylolisthesis": data.degree_spondylolisthesis
        }])

        result = predict_model(
            model,
            data=df
        )

        print(result)

        if "prediction_label" in result.columns:
            prediction = result["prediction_label"].iloc[0]
        elif "Label" in result.columns:
            prediction = result["Label"].iloc[0]
        else:
            prediction = result.iloc[0, -1]

        return {
            "prediction": str(prediction)
        }

    except Exception as e:
        return {
            "error": str(e)
        }