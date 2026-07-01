import pandas as pd

# Load cleaned performance dataset
performance = pd.read_csv("data/processed/scheme_performance_clean.csv")

# Take user input
risk = input("Enter risk appetite (Low / Moderate / High): ")

# Filter based on risk grade
if risk == "Low":
    data = performance[
        performance["risk_grade"] == "Low"
    ]

elif risk == "Moderate":
    data = performance[
        performance["risk_grade"] == "Moderate"
    ]

else:
    data = performance[
        performance["risk_grade"] == "High"
    ]

# Sort by sharpe ratio
top = data.sort_values(
    "sharpe_ratio",
    ascending=False
).head(3)

# Print recommendations
print("\nTop Recommended Funds\n")

print(
    top[
        [
            "scheme_name",
            "risk_grade",
            "sharpe_ratio"
        ]
    ]
)