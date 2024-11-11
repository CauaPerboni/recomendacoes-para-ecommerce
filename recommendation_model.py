import pandas as pd
from scipy.sparse import lil_matrix
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def create_interaction_matrix(df):
    df = df[df['visitorid'].isin(df['visitorid'].value_counts().head(1000).index)]
    df = df[df['itemid'].isin(df['itemid'].value_counts().head(1000).index)]

    visitor_mapping = {visitor: idx for idx, visitor in enumerate(df['visitorid'].unique())}
    item_mapping = {item: idx for idx, item in enumerate(df['itemid'].unique())}

    interaction_matrix = lil_matrix((len(visitor_mapping), len(item_mapping)), dtype=np.int8)

    for _, row in df.iterrows():
        visitor_idx = visitor_mapping[row['visitorid']]
        item_idx = item_mapping[row['itemid']]
        interaction_matrix[visitor_idx, item_idx] = 1 

    return interaction_matrix, visitor_mapping, item_mapping

def get_recommendations(user_id, interaction_matrix_sparse, visitor_mapping, item_mapping):
    if user_id not in visitor_mapping:
        raise ValueError(f"User ID {user_id} not found in the interaction matrix.")
    
    user_index_position = visitor_mapping[user_id]
    
    user_vector = interaction_matrix_sparse[user_index_position, :].toarray().flatten()
    
    similarity_scores = cosine_similarity(user_vector.reshape(1, -1), interaction_matrix_sparse).flatten()

    recommended_indices = similarity_scores.argsort()[-10:][::-1]

    recommended_items = [item for item, idx in item_mapping.items() if idx in recommended_indices]

    return recommended_items
