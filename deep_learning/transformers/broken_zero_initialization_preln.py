import torch
import torch.nn as nn

class PreLNResidualBlock(nn.Module):
    def __init__(self, d_model):
        super().__init__()
        self.ln = nn.LayerNorm(d_model)
        # The 'Service Station' (Simplified Linear layer)
        self.feature_extractor = nn.Linear(d_model, d_model)
        # The 'Gatekeeper' (Output Projection)
        self.output_projection = nn.Linear(d_model, d_model)
        
        self.init_weights()

    def init_weights(self):
        # Standard init for the internal features
        nn.init.xavier_uniform_(self.feature_extractor.weight)
        
        # BROKEN LOGIC: The engineer tried to zero-init the input to 
        # the sublayer to make the branch 'silent'.
        nn.init.zeros_(self.feature_extractor.weight) 
        nn.init.zeros_(self.feature_extractor.bias)
        
        # Standard init for the projection
        nn.init.xavier_uniform_(self.output_projection.weight)

    def forward(self, x):
        # x_out = x + Projection(Sublayer(LN(x)))
        residual = x
        x = self.ln(x)
        x = self.feature_extractor(x)
        x = self.output_projection(x)
        return x + residual

# Testing the identity property
d_model = 128
model = PreLNResidualBlock(d_model)
sample_input = torch.randn(1, d_model)
output = model(sample_input)

print(f"Is output identical to input? {torch.allclose(sample_input, output, atol=1e-5)}")