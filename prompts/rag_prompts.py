from utils.logger import logger
from langchain_core.prompts import PromptTemplate

rag_prompt = PromptTemplate(
    template="""
    You are a helpful assistant.
    Answer ONLY from the provided context.
    If context is insufficient,
    say "I don't know".
    Context:
    {context}
    Question:
    {question}
""",
    input_variables=['context','question']
)