import torch
import torch.nn.functional as F

def basic_attention(Q, K, V):
    """
    Q, K, V shapes: (batch, seq_len, head_dim)
    Example: (1, 5, 64)
    """
    # 1. Calculate raw scores (Dot Product of Q and K)
    # We transpose K so the "features" align for the math
    scores = torch.matmul(Q, K.transpose(-2, -1)) 
    
    # --- POTENTIAL ERROR ZONE ---
    # In the paper, they divide 'scores' by the square root of the dimension (8 for 64-dim).
    # Without it, the Softmax becomes too "extreme" (all 0s and one 1).
    # -----------------------------

    # 2. Convert scores to weights (0.0 to 1.0)
    weights = F.softmax(scores, dim=-1)
    
    # 3. Multiply weights by Values to get the final "Context"
    output = torch.matmul(weights, V)
    
    return output, weights

# Let's simulate: 1 sentence, 3 words, each word is a 4-dim vector
query = torch.randn(1, 3, 4)
key = torch.randn(1, 3, 4)
value = torch.randn(1, 3, 4)

context, attn_weights = basic_attention(query, key, value)