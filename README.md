 
 # Video Subtitle Generator

This is a Python script for extracting audio from a video file, converting it to text using automatic speech recognition, and generating subtitle files.

## Dependencies

Make sure you have the following dependencies installed:

- moviepy.editor
- AudioFileClip from moviepy.editor
- speech_recognition
- subprocess
- AudioSegment from pydub
- split_on_silence from pydub.silence
- os
- datetime

You can install these dependencies using pip:
-pip install moviepy
-pip install SpeechRecognition
-pip install pydub


## Usage

1. Place the video file "Eng_speech.mp4" in the same directory as the script.
2. Run the script.
3. The script will extract the audio from the video and save it as "Audio.mp3".
4. The "Audio.mp3" file will be converted to "Audio.wav" using FFmpeg.
5. The script will split the audio into chunks based on silence intervals.
6. Each chunk will be transcribed using the Sphinx speech recognition engine.
7. Subtitles will be generated for each chunk and saved in "output.srt".

## Configuration

The script provides several configuration options that you can adjust according to your needs. These options are set using the `Recognizer` object from the `speech_recognition` library.

- `r.energy_threshold`: Energy threshold for audio recording.
- `r.pause_threshold`: Minimum pause length to consider as a separate phrase.
- `r.dynamic_energy_threshold`: Use dynamic energy threshold instead of a fixed value.
- `r.dynamic_energy_adjustment_damping`: Damping factor for dynamic energy adjustment.
- `r.dynamic_energy_ratio`: Energy ratio for dynamic energy adjustment.
- `r.operation_timeout`: Timeout for audio recording operations.
- `r.phrase_threshold`: Minimum length of a phrase to consider as valid.
- `r.non_speaking_duration`: Minimum duration of non-speaking audio to include in a phrase.
- `r.buffer_size`: Buffer size for audio recording.
- `r.dynamic_energy_adjustment_ratio`: Energy ratio for dynamic energy adjustment.

Feel free to modify these values to achieve better results based on your audio recordings.

## Cleanup

After generating the subtitle file, the script will remove all the temporary chunk files that were created during the process.

Please note that this script assumes the presence of a video file named "Eng_speech.mp4" in the same directory. Adjust the file name accordingly if necessary.

## License

This script is released under the MIT license. Feel free to modify and use it according to your requirements.




<!-- # Video-Subtitle-Generator

This is a Python script for extracting audio from a video file, converting it to text using automatic speech recognition, and generating subtitle files.

# Dependencies
Make sure you have the following dependencies installed:

moviepy.editor
AudioFileClip from moviepy.editor
speech_recognition
subprocess
AudioSegment from pydub
split_on_silence from pydub.silence
os
datetime
You can install these dependencies using pip:

Copy code
pip install moviepy
pip install SpeechRecognition
pip install pydub
Usage
Place the video file "Eng_speech.mp4" in the same directory as the script.
Run the script.
The script will extract the audio from the video and save it as "Audio.mp3".
The "Audio.mp3" file will be converted to "Audio.wav" using FFmpeg.
The script will split the audio into chunks based on silence intervals.
Each chunk will be transcribed using the Sphinx speech recognition engine.
Subtitles will be generated for each chunk and saved in "output.srt".
Configuration
The script provides several configuration options that you can adjust according to your needs. These options are set using the Recognizer object from the speech_recognition library.

r.energy_threshold: Energy threshold for audio recording.
r.pause_threshold: Minimum pause length to consider as a separate phrase.
r.dynamic_energy_threshold: Use dynamic energy threshold instead of a fixed value.
r.dynamic_energy_adjustment_damping: Damping factor for dynamic energy adjustment.
r.dynamic_energy_ratio: Energy ratio for dynamic energy adjustment.
r.operation_timeout: Timeout for audio recording operations.
r.phrase_threshold: Minimum length of a phrase to consider as valid.
r.non_speaking_duration: Minimum duration of non-speaking audio to include in a phrase.
r.buffer_size: Buffer size for audio recording.
r.dynamic_energy_adjustment_ratio: Energy ratio for dynamic energy adjustment.
Feel free to modify these values to achieve better results based on your audio recordings.

Cleanup
After generating the subtitle file, the script will remove all the temporary chunk files that were created during the process.

Please note that this script assumes the presence of a video file named "Eng_speech.mp4" in the same directory. Adjust the file name accordingly if necessary.

License
This script is released under the MIT license. Feel free to modify and use it according to your requirements.
 -->






