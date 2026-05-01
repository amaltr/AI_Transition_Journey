import torch
import torch.nn as nn

class PreLNResidualBlock(nn.Module):
    def __init__(self, d_model):
        super().__init__()
        self.ln = nn.LayerNorm(d_model)
        
        # The 'Engine': We want this initialized with standard variance
        self.feature_extractor = nn.Linear(d_model, d_model)
        
        # The 'Gatekeeper': This is what we zero-initialize
        self.output_projection = nn.Linear(d_model, d_model)
        
        self.init_weights()

    def init_weights(self):
        """
        Initializes weights using the Pre-LN 'Identity' strategy.
        We use Xavier/Glorot for the internal logic to maintain signal 
        variance, but zero the projection to ensure an identity start.
        """
        # 1. Initialize the internal layer normally to allow 'latent' learning
        nn.init.xavier_uniform_(self.feature_extractor.weight)
        nn.init.zeros_(self.feature_extractor.bias)
        
        # 2. Zero-initialize the gatekeeper (Weight and Bias)
        # This ensures: x_out = x + 0 * f(x) = x
        nn.init.zeros_(self.output_projection.weight)
        nn.init.zeros_(self.output_projection.bias)

    def forward(self, x):
        # Pre-LN Architecture: LayerNorm -> Sublayer -> Add Residual
        residual = x
        x = self.ln(x)
        x = self.feature_extractor(x)
        x = self.output_projection(x)
        return x + residual

# --- Verification ---
d_model = 128
model = PreLNResidualBlock(d_model)
x = torch.randn(1, d_model)
output = model(x)

# Verification check: The variance of the output should match the input
print(f"✅ Identity Verified: {torch.allclose(x, output, atol=1e-5)}")