import torch
import torch.nn as nn

class MultiHeadAttentionSimple(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.d_k = d_model // num_heads
        
        # Projections for Q, K, V
        self.w_q = nn.Linear(d_model, d_model)
        self.w_k = nn.Linear(d_model, d_model)
        self.w_v = nn.Linear(d_model, d_model)
        
        # Final output projection
        self.w_o = nn.Linear(d_model, d_model)

    def forward(self, x):
        batch_size, seq_len, d_model = x.size()
        
        # 1. Linear Projections
        q = self.w_q(x)
        k = self.w_k(x)
        v = self.w_v(x)
        
        # 2. Split into heads 
        # (Batch, Seq, Heads, D_k) -> transpose to (Batch, Heads, Seq, D_k)
        q = q.view(batch_size, seq_len, self.num_heads, self.d_k).transpose(1, 2)
        k = k.view(batch_size, seq_len, self.num_heads, self.d_k).transpose(1, 2)
        v = v.view(batch_size, seq_len, self.num_heads, self.d_k).transpose(1, 2)
        
        # [Pretend Attention Calculation happens here]
        # output shape: (batch_size, num_heads, seq_len, self.d_k)
        attn_output = v 
        
        # --- THE BROKEN SECTION ---
        # 3. Concatenate heads back together
        # We need to get back to (batch_size, seq_len, d_model)
        
        # Logic: Flatten the last two dimensions to "merge" heads
        combined = attn_output.view(batch_size, seq_len, d_model) 
        
        # 4. Final Projection
        return self.w_o(combined)

# Hint: Look closely at the dimensions in step 2 vs step 3. 
# Did we return the data to its original order before view()?