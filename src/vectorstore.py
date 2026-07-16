import faiss
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

print("Loading knowledge base...")

# Load processed data
df = pd.read_csv("data/medical_knowledge_base.csv")

print("Loading embedding model...")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Generating embeddings...")

embeddings = model.encode(
    df["Knowledge"].tolist(),
    show_progress_bar=True
)

# Convert embeddings to NumPy array
embeddings = np.array(embeddings).astype("float32")

print("Creating FAISS index...")

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

# Add embeddings
index.add(embeddings)

print(f"Total vectors stored: {index.ntotal}")

# Save index
faiss.write_index(index, "vectorstore/medical_index.faiss")

print("\nFAISS index saved successfully!")