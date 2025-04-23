import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)
    
    # Drop customerID and handle missing values
    df.drop("customerID", axis=1, inplace=True)
    df.dropna(inplace=True)
    
    # Convert TotalCharges to numeric
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df.dropna(subset=["TotalCharges"], inplace=True)

    # Encode target column
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

    return df
