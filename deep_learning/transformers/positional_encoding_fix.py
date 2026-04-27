import torch

def apply_positional_encoding(word_embeddings):
    """
    word_embeddings: (batch_size, seq_len, emb_dim) -> (32, 10, 512)
    """
    batch_size, seq_len, emb_dim = word_embeddings.shape
    
    # 1. Create encoding for ONE sentence: Shape (10, 512)
    pos_encoding = torch.randn(seq_len, emb_dim) 
    
    # 2. Add a batch dimension: Shape (1, 10, 512)
    # unsqueeze(0) turns [[row]] into [[[row]]]
    pos_encoding = pos_encoding.unsqueeze(0)
    
    # 3. Add them together!
    # PyTorch sees (32, 10, 512) + (1, 10, 512)
    # It automatically treats the '1' as '32' by repeating the data.
    output = word_embeddings + pos_encoding
    
    return output

# Test
sample_batch = torch.randn(32, 10, 512)
result = apply_positional_encoding(sample_batch)
print(f"Final shape: {result.shape}") # Should be (32, 10, 512)