from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled, NoTranscriptFound
from utils.logger import logger

class YoutubeLoader:

    @staticmethod
    def load_transcript(video_id:str):

        try:
            logger.info(f"Loading transcript for video {video_id}")
            api = YouTubeTranscriptApi()
            transcript_list = api.list(video_id)
            transcript = transcript_list.find_generated_transcript(['en', 'hi'])

            data = transcript.fetch()
            text = ' '.join( chunk.text for chunk in data)
            logger.info( "Transcript loaded successfully")

            return text
        except TranscriptsDisabled:

            logger.error("Transcript disabled")
            raise Exception(f"Transcript disabled for video {video_id}")

        except NoTranscriptFound:

            logger.error("Transcript not found")
            raise Exception(f"No transcript found for video {video_id}")

        except Exception as e:

            logger.exception("Error loading transcript")
            raise Exception(f"Transcript loading failed: {str(e)}")
            

# from youtube_transcript_api import YouTubeTranscriptApi

# ytt_api = YouTubeTranscriptApi()

# transcript_list = ytt_api.list("J5_-l7WIO_w")

# for transcript in transcript_list:
#     print(transcript)