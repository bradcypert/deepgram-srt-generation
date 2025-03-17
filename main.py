import sys
import httpx
import os
from datetime import datetime
from deepgram import DeepgramClient, PrerecordedOptions
from deepgram_captions import DeepgramConverter, srt
from moviepy.video.io.VideoFileClip import VideoFileClip

def main():
    try:
        deepgram = DeepgramClient(os.getenv("DEEPGRAM_API_KEY"))

        filepath = sys.argv[1]
        print(filepath)
        audio_filepath = f"{filepath}-audio.mp3"

        try:
            with VideoFileClip(filepath) as video_clip:
                audio_clip = video_clip.audio
                audio_clip.write_audiofile(audio_filepath)
        except Exception as e:
            print(f"An error occurred: {e}")
            return

        with open(audio_filepath, "rb") as file:
            buffer_data = file.read()

        payload = {"buffer": buffer_data}

        options = PrerecordedOptions(
            model="nova-3",
            smart_format=True,
            utterances=True,
            punctuate=True,
            diarize=True,
        )

        print("Making request to deepgram")

        before = datetime.now()
        response = deepgram.listen.rest.v("1").transcribe_file(
            payload, options, timeout=httpx.Timeout(30000.0, connect=10.0)
        )
        after = datetime.now()
        print("Got response from deepgram")

        print(response.to_json(indent=4))

        transcription = DeepgramConverter(response)
        captions = srt(transcription)
        
        with open(f"{filepath}-captions.srt", "a") as f:
            f.write(captions)

        os.remove(audio_filepath)

    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    main()