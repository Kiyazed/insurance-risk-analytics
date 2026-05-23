import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.data_loader import load_data
from src.eda_utils import plot_histogram, plot_boxplot

df = load_data("../data/raw/insurance_data.csv")

print(df.head())

print(df.describe())

plot_histogram(df, "TotalPremium")

plot_boxplot(df, "TotalClaims")