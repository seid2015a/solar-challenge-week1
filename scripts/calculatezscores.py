import os
import pandas as pd
# Function to calculate Z-scores
def calculate_z_scores(data, columns):
    z_scores = pd.DataFrame()
    
    for col in columns:
        # Calculate Z-scores for each variable
        z_scores[col] = (data[col] - data[col].mean()) / data[col].std()
    
    return z_scores