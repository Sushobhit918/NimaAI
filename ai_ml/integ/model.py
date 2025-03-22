import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import pickle
import os

MODEL_PATH = "reinforcement_model.pkl"

class RLAllergenModel:
    def __init__(self):
        self.model = None
        self.label_encoder = None
        self.preprocessor = None
        self.learning_rate = 0.1  # Controls how much feedback updates the model

    def train_initial_model(self):
        dataset = pd.read_csv('Allergen_Status_of_Food_Products.csv')
        print("Columns in dataset:", dataset.columns.tolist())

        # Ensure 'Prediction' exists and handle missing values
        dataset['Prediction'] = dataset['Prediction'].fillna("unknown")
        
        # Separate features (X) and target (y)
        y = dataset['Prediction']
        X = dataset.drop(columns=['Prediction'])  # Ensure 'Prediction' is not in training features

        # Define numeric and categorical feature sets
        numeric_features = ['Price ($)', 'Customer rating (Out of 5)']
        categorical_features = ['Food Product', 'Main Ingredient', 'Sweetener', 'Fat/Oil', 'Seasoning', 'Allergens']

        # Fill missing values appropriately
        X[numeric_features] = X[numeric_features].fillna(X[numeric_features].mean())
        X[categorical_features] = X[categorical_features].fillna("missing")

        # Define preprocessing pipeline
        self.preprocessor = ColumnTransformer(
            transformers=[
                ('num', Pipeline([
                    ('imputer', SimpleImputer(strategy='mean')),
                    ('scaler', StandardScaler())
                ]), numeric_features),
                ('cat', Pipeline([
                    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
                    ('onehot', OneHotEncoder(handle_unknown='ignore'))
                ]), categorical_features)
            ]
        )

        # Process input features
        X_processed = self.preprocessor.fit_transform(X)

        # Encode target labels
        self.label_encoder = LabelEncoder()
        y_encoded = self.label_encoder.fit_transform(y)

        # Train the MLP classifier
        self.model = MLPClassifier(hidden_layer_sizes=(100, 50), activation='relu', solver='adam',
                                   random_state=42, max_iter=300)
        self.model.fit(X_processed, y_encoded)

        self.save_model()
        print("Initial Model Training Completed")

    def save_model(self):
        """ Saves the trained model, label encoder, and preprocessor. """
        with open(MODEL_PATH, "wb") as f:
            pickle.dump({
                "model": self.model,
                "label_encoder": self.label_encoder,
                "preprocessor": self.preprocessor
            }, f)

    def load_model(self):
        """ Loads the model if available, else retrains it. Ensures feature compatibility. """
        try:
            if not os.path.exists(MODEL_PATH):
                raise FileNotFoundError("Model file not found. Retraining model.")

            with open(MODEL_PATH, "rb") as f:
                data = pickle.load(f)
                self.model = data["model"]
                self.label_encoder = data["label_encoder"]
                self.preprocessor = data["preprocessor"]

            # Verify feature set consistency
            expected_features = ['Food Product', 'Main Ingredient', 'Sweetener', 'Fat/Oil', 'Seasoning', 'Allergens', 'Price ($)', 'Customer rating (Out of 5)']
            preprocessor_features = self.preprocessor.transformers_[1][2]  # Categorical features

            if set(expected_features) != set(preprocessor_features + ['Price ($)', 'Customer rating (Out of 5)']):
                raise ValueError("Feature set mismatch. Retraining model.")

            print("Model loaded successfully.")
        except (FileNotFoundError, KeyError, ValueError) as e:
            print(f"Error loading model: {e}. Training a new model...")
            self.train_initial_model()

    def predict(self, input_data):
        """ Predicts the allergen status for a given food product. """
        processed_input = self.preprocessor.transform(input_data)
        prediction_encoded = self.model.predict(processed_input)[0]
        return self.label_encoder.inverse_transform([prediction_encoded])[0]

    def update_model(self, input_data, correct_label):
        """ Updates the model using reinforcement learning based on user feedback. """
        processed_input = self.preprocessor.transform(input_data)
        correct_label_encoded = self.label_encoder.transform([correct_label])[0]

        old_weights = self.model.coefs_
        self.model.partial_fit(processed_input, [correct_label_encoded])
        
        # Reinforcement update rule
        self.model.coefs_ = [
            old_weight + self.learning_rate * (new_weight - old_weight)
            for old_weight, new_weight in zip(old_weights, self.model.coefs_)
        ]
        
        self.save_model()
        print("Model updated with reinforcement learning.")

def load_and_train_model():
    """ Loads an existing model or trains a new one if needed. """
    rl_model = RLAllergenModel()
    rl_model.load_model()
    return rl_model
