# test_rag.py

from app.core.rag_chain import get_rag_answer

query = "Who is the Fintech VC powerhouse stepping down from QED Investors"
answer = get_rag_answer(query)
print("Gemini Response:\n", answer)
