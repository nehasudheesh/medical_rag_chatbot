import faiss
import pandas as pd
from sentence_transformers import SentenceTransformer

# Load knowledge base
df = pd.read_csv("data/medical_knowledge_base.csv")

# Load FAISS index
index = faiss.read_index("vectorstore/medical_index.faiss")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def retrieve_context(query, k=1):
    """
    Retrieve the most relevant medical information
    """

    query_embedding = model.encode([query]).astype("float32")

    distances, indices = index.search(query_embedding, k)

    return df.iloc[indices[0][0]]["Knowledge"]


# Test independently
if __name__ == "__main__":

    question = input("Enter your medical question: ")

    context = retrieve_context(question)

    print("\nRetrieved Context:\n")

    print(context)