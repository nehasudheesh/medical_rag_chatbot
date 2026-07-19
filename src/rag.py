from src.retriever import retrieve_context
from src.llm import generate_answer


def ask_rag(question):
    """
    Complete RAG Pipeline:
    1. Retrieve context
    2. Generate answer using Gemini
    """

    context = retrieve_context(question)

    answer = generate_answer(context, question)

    return answer


if __name__ == "__main__":

    question = input("Ask a medical question: ")

    answer = ask_rag(question)

    print("\nAnswer:\n")
    print(answer)