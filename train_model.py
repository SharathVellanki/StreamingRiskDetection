import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from joblib import dump

# Load the credit card fraud dataset 
df = pd.read_csv("data/creditcard.csv").sample(n=10000, random_state=42)


# Separate features and target
X = df.drop("Class", axis=1)
y = df["Class"]

# Split into train/test sets (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train a basic XGBoost classifier
model = xgb.XGBClassifier(
    use_label_encoder=False,
    eval_metric="logloss"
)
model.fit(X_train, y_train)

# Evaluate on the test set
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Accuracy on test set: {accuracy:.4f}")

# Persist the model to disk
dump(model, "model/xgb_model.pkl")
print("✅ Model saved to: model/xgb_model.pkl")
