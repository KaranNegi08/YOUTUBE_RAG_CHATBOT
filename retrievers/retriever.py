from utils.logger import logger

class RetrieverManager:

    @staticmethod
    def get_retriever(vectorstore):

        try:
            retriever = vectorstore.as_retriever(
                search_type="similarity",
                search_kwargs={"k": 4}
            )

            logger.info("Retriever created...")
            return retriever
        except Exception as e:
            logger.exception("Retriever creation failed")

            raise Exception(f"Retriever error: {str(e)}")