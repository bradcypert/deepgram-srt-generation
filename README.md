# Deepgram SRT Generation

This project extracts audio from a video file, sends it to Deepgram for transcription, and generates an SRT file with captions.

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/bradcypert/deepgram-srt-generation.git
    cd deepgram-srt-generation
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Set your Deepgram API key as an environment variable:
    ```sh
    export DEEPGRAM_API_KEY=your_deepgram_api_key
    ```

## Usage

Run the script with the path to your video file as an argument:
```sh
python main.py path/to/your/video.mp4
```

This will generate an SRT file with captions in the same directory as your video file.

## Dependencies

- `httpx`
- `moviepy`
- `deepgram`
- `deepgram_captions`

Make sure to install these dependencies using `pip` if they are not already installed.

## License

This project is licensed under the MIT License.
