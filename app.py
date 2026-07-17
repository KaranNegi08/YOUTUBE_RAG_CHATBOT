from loaders.youtube_loader import YoutubeLoader
from utils.text_splitter import split_text
from embeddings.embedding_model import get_embedding_model
from vectorstores.faiss_store import VectorStoreManager
from retrievers.retriever import  RetrieverManager
from chains.rag_chain import create_rag_chain
from utils.logger import logger


VIDEO_ID = "TrPEIepZGx8"

def main():

    try:
        logger.info("Application Started..")
        transcript = YoutubeLoader.load_transcript(VIDEO_ID)
        documents = split_text(transcript)
        embeddings = get_embedding_model()
        vectorstore = VectorStoreManager.create_vector_store(
            documents,embeddings
        )
        retriever = RetrieverManager.get_retriever(vectorstore)

        rag_chain = create_rag_chain(retriever)

        print("\n Youtube   Chatbot ready")

        while True:
            query= input("\n Ask question: ")

            if query.lower() == 'exit':
                break

            try:
                response = rag_chain.invoke(query)
                print("\n Answer:\n")
                print(response)
            except Exception as e:
                logger.exception("Query processing failed")

                print(f"\nError: {e}")

    except Exception as e:
        logger.exception("Application startup failed")
        print(f"\nStartup Error: {e}")


if __name__=="__main__":
    main()
