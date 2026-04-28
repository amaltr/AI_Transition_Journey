import torch
import torch.nn.functional as F
import math

def scaled_dot_product_attention(query, key, value):
    # 1. Calculate the raw dot product scores
    # Shape: (Batch, Words, Words)
    scores = torch.matmul(query, key.transpose(-2, -1))
    
    # 2. THE FIX: The Scaling Factor 🛑
    # Without this, scores get too large, and Softmax "saturates"
    d_k = query.size(-1)
    scaled_scores = scores / math.sqrt(d_k)
    
    # 3. Apply Softmax to get weights
    # dim=-1 means we normalize across the columns (each word's attention)
    weights = F.softmax(scaled_scores, dim=-1)
    
    # 4. Multiply weights by values
    output = torch.matmul(weights, value)
    
    return output, weights