from src.data_loader import load_data
from src.preprocessing import clean_data

def main():
    df = load_data("data/raw/insurance_data.csv")

    cleaned_df = clean_data(df)

    cleaned_df.to_csv(
        "data/processed/cleaned_insurance_data.csv",
        index=False
    )

    print("Cleaned data saved successfully!")

if __name__ == "__main__":
    main()