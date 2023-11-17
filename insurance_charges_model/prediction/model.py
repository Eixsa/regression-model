import os
import joblib
import pandas as pd
from ml_base import MLModel
from typing import List, Optional
from ml_base.decorator import MLModelDecorator
from ml_base.ml_model import MLModelSchemaValidationException
from insurance_charges_model import __version__
from insurance_charges_model.prediction.schemas import InsuranceChargesModelInput, \
    InsuranceChargesModelOutput
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from time import time
import json  # Import json module for serialization


class InsuranceChargesModel(MLModel):
    """Prediction functionality of the Insurance Charges Model."""

    @property
    def display_name(self) -> str:
        """Return display name of model."""
        return "Insurance Charges Model"

    @property
    def qualified_name(self) -> str:
        """Return qualified name of model."""
        return "insurance_charges_model"

    @property
    def description(self) -> str:
        """Return description of model."""
        return "Model to predict the insurance charges of a customer."

    @property
    def version(self) -> str:
        """Return version of model."""
        return __version__

    @property
    def input_schema(self):
        """Return input schema of model."""
        return InsuranceChargesModelInput

    @property
    def output_schema(self):
        """Return output schema of model."""
        return InsuranceChargesModelOutput

    def __init__(self):
        """Class constructor that loads and deserializes the model parameters.

        .. note::
            The trained model parameters are loaded from the "model_files" directory.

        """
        dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        with open(os.path.join(dir_path, "model_files", "1", "model.joblib"), 'rb') as file:
            self._svm_model = joblib.load(file)
            

    def predict(self, data: InsuranceChargesModelInput) -> InsuranceChargesModelOutput:
        

        """Make a prediction with the model."""

        # converting the incoming dictionary into a pandas dataframe that can be accepted by the model
        X = pd.DataFrame([[data.age, data.sex.value, data.bmi, data.children, data.smoker, data.region.value]],
                         columns=["age", "sex", "bmi", "children", "smoker", "region"])

        # making the prediction and extracting the result from the array
        y_hat = round(float(self._svm_model.predict(X)[0]), 2)

        return InsuranceChargesModelOutput(charges=y_hat)
