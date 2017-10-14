import pandas
import matrix_factorization_utilities
import pandas as pd
import numpy as np
df = pd.read_csv("sample_New - sample.csv")
df=df.loc[df['status']=="Finished"]
#, values='Quantity'
popularity_product = pd.pivot_table(df, index=['product_id','status','unit_price'], columns='location', aggfunc=np.sum)

P,L = matrix_factorization_utilities.low_rank_matrix_factorization(popularity_product.as_matrix(),num_features=15,regularization_amount=0.1)
#
predicted_ratings = np.matmul(P,L)

predicted_ratings_df= pd.DataFrame(index=popularity_product.index,
                                   columns=popularity_product.columns,
                                   data=predicted_ratings)

predicted_ratings_df.to_csv("predicted_ratings.csv")


popularity_product.to_csv("product_popularity.csv", na_rep=0)




