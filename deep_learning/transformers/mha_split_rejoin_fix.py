import torch
import torch.nn as nn

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        assert d_model % num_heads == 0, "d_model must be divisible by num_heads"
        
        self.num_heads = num_heads
        self.d_k = d_model // num_heads
        
        # Projections
        self.w_q = nn.Linear(d_model, d_model)
        self.w_k = nn.Linear(d_model, d_model)
        self.w_v = nn.Linear(d_model, d_model)
        self.w_o = nn.Linear(d_model, d_model)

    def forward(self, x):
        batch_size, seq_len, d_model = x.size()
        
        # 1. Linear Projections & Split into Heads
        # Shape: (Batch, Seq, Heads, D_k) -> (Batch, Heads, Seq, D_k)
        q = self.w_q(x).view(batch_size, seq_len, self.num_heads, self.d_k).transpose(1, 2)
        k = self.w_k(x).view(batch_size, seq_len, self.num_heads, self.d_k).transpose(1, 2)
        v = self.w_v(x).view(batch_size, seq_len, self.num_heads, self.d_k).transpose(1, 2)
        
        # 2. Parallel Attention (Simulated here)
        # Output shape is (Batch, Heads, Seq, D_k)
        attn_output = v 
        
        # 3. THE FIX: Transpose back BEFORE merging
        # Move 'Seq' back to dim 1: (Batch, Seq, Heads, D_k)
        combined = attn_output.transpose(1, 2).contiguous()
        
        # 4. Merge Heads: (Batch, Seq, d_model)
        # Since Heads * D_k = d_model, this "flattens" the last two dims correctly
        combined = combined.view(batch_size, seq_len, d_model)
        
        # 5. Final Projection
        return self.w_o(combined)