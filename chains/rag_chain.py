from utils.logger import logger
from prompts.rag_prompts  import rag_prompt
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (RunnableParallel,RunnableLambda,RunnablePassthrough)
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()

def format_docs(docs):
    return "\n\n".join( doc.page_content for doc in docs)

def create_rag_chain(retriever):
    try:
        llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            api_key=os.getenv("GROQ_API_KEY")
        )

        parallel_chain = RunnableParallel({
            "context": retriever | RunnableLambda(format_docs),  #to convert the function into runnable
            "question": RunnablePassthrough()
        })

        chain = parallel_chain | rag_prompt | llm | StrOutputParser()

        logger.info("RAG chain created..")
        return chain
    except Exception as e:
        logger.exception("Chain creation failed")

        raise Exception(f"Chain creation error: {str(e)}")