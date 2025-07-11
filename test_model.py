from app.model import predict_risk

# Sample 30-feature input: [Time] + [V1–V28] + [Amount]
sample_input = [
    0.0,  # Time
    -1.359807, -0.072781, 2.536347, 1.378155, -0.338321,
    0.462388, 0.239599, 0.098698, 0.363787, 0.090794,
    -0.551600, -0.617801, -0.991390, -0.311169, 1.468177,
    -0.470401, 0.207971, 0.025791, 0.403993, 0.251412,
    -0.018307, 0.277838, -0.110474, 0.066928, 0.128539,
    -0.189115, 0.133558, -0.021053, 149.62  # Amount
]

result = predict_risk(sample_input)
label = "RISKY" if result == 1 else "SAFE"

print(f" Prediction: {result} → {label}")
