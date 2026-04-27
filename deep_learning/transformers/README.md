# Transformers

This folder contains exercises, fixes, and diagrams related to Transformer architectures in Deep Learning.

## Positional Encoding
Transformers lack an inherent sense of sequential order (unlike RNNs). To inject positional information, we use Positional Encodings which are added to the input embeddings.

### Files
- `broken_positional_encoding.py`: Example of a problematic implementation of positional encoding.
- `positional_encoding_fix.py`: A corrected implementation demonstrating proper broadcasting of positional encodings over a batch of sequences.
- `positional_encoding.mmd`: A Mermaid diagram visualizing the concept of Positional Encoding.
