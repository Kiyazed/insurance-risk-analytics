import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(df, column):
    plt.figure(figsize=(8,5))
    sns.histplot(df[column], kde=True)
    plt.title(f"Distribution of {column}")
    plt.show()

def plot_boxplot(df, column):
    plt.figure(figsize=(8,5))
    sns.boxplot(x=df[column])
    plt.title(f"Boxplot of {column}")
    plt.show()

def calculate_loss_ratio(df):
    df["LossRatio"] = df["TotalClaims"] / df["TotalPremium"]
    return df

def calculate_margin(df):
    df["Margin"] = df["TotalPremium"] - df["TotalClaims"]
    return df