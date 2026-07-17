from utils.logger import logger
from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_text(text):
    try:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        docs = splitter.create_documents([text])
        logger.info(f"{len(docs)} chunks created...")

        return docs
    except Exception as e:
        logger.exception("Text splitting failed")

        raise Exception(f"Text splitting error: {str(e)}")