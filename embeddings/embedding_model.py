from langchain_huggingface import HuggingFaceEmbeddings
from utils.logger import logger



def get_embedding_model():
    try:
        logger.info("Initializing embedding model")
        return HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

    except Exception as e:
        logger.exception("Embedding initialization failed")

        raise Exception(f"Embedding model error: {str(e)}")