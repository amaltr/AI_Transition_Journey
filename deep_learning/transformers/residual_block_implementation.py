import torch
import torch.nn as nn

class ResidualBlock(nn.Module):
    def __init__(self, d_model):
        super().__init__()
        self.ln = nn.LayerNorm(d_model)
        self.sublayer = nn.Linear(d_model, d_model) # Simplified sublayer

    def forward(self, x):
        # OPTION A: Post-LN (The Original)
        # return self.ln(x + self.sublayer(x))
        
        # OPTION B: Pre-LN (The Modern Choice)
        return x + self.sublayer(self.ln(x))