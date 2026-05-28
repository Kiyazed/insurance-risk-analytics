from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency
import pandas as pd

# Independent T-Test
def perform_ttest(group1, group2):

    stat, p_value = ttest_ind(
        group1,
        group2,
        nan_policy='omit'
    )

    return stat, p_value


# Chi-Square Test
def perform_chi_square(contingency_table):

    chi2, p_value, dof, expected = chi2_contingency(
        contingency_table
    )

    return chi2, p_value