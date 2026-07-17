from langchain_community.vectorstores import FAISS
from utils.logger import logger

class VectorStoreManager:

    @staticmethod
    def create_vector_store(documents, embeddings):

        try:
            if not documents:
                raise ValueError("No documents available")
            
            vectorstore = FAISS.from_documents(
                documents, embeddings
            )
            logger.info("FAISS vector store created")

            return vectorstore
        except Exception as e:
            logger.exception("Vector store creation failed")

            raise Exception(f"Vector store error: {str(e)}")