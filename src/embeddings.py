import pandas as pd
from sentence_transformers import SentenceTransformer

print("Loading knowledge base...")

# Load the processed knowledge base
df = pd.read_csv("data/medical_knowledge_base.csv")

print("Loading embedding model...")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Generating embeddings...")

# Generate embeddings
embeddings = model.encode(
    df["Knowledge"].tolist(),
    show_progress_bar=True
)

print("\nEmbedding generation completed!")

print(f"Number of embeddings: {len(embeddings)}")

print(f"Dimension of one embedding: {len(embeddings[0])}")