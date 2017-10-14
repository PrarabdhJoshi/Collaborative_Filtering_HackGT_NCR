import pandas as pd
import numpy as np

raw_df = pd.read_csv('product_popularity.csv')
ratings_df = pd.pivot_table(raw_df,index = 'product_id',columns='location')