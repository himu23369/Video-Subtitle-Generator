import moviepy.editor
from moviepy.editor import AudioFileClip
import speech_recognition as sr
import subprocess
from pydub import AudioSegment
from pydub.silence import split_on_silence
import os
import datetime

video = moviepy.editor.VideoFileClip("Eng_speech.mp4")

#Extract the Audio
audio = video.audio

#Export the Audio
audio.write_audiofile("Audio.mp3")

input_file = "Audio.mp3"
output_file = "Audio.wav"

# load the MP3 file
audio_clip = AudioFileClip(input_file)
subprocess.call(['ffmpeg', '-i', 'Audio.mp3', 'Audio.wav'])

# Load the audio file
audio_file = sr.AudioFile('Audio.wav')

# **************************************

# Initialize the recognizer with the sphinx engine
r = sr.Recognizer()
# This line initializes a speech recognition engine called "Recognizer" from the speech_recognition library.

r.energy_threshold = 500
r.pause_threshold = 0.5
r.dynamic_energy_threshold = True
r.dynamic_energy_adjustment_damping = 0.15
r.dynamic_energy_ratio = 1.5
r.operation_timeout = None
r.phrase_threshold = 0.3
r.non_speaking_duration = 0.2
r.pause_threshold = 0.8
r.phrase_threshold = 0.1
r.buffer_size = 1
r.dynamic_energy_adjustment_ratio = 1.5

# **************************************

# Create a subtitle file
subtitle_file = open('output.srt', 'w')

# Get the duration of the audio clip
with AudioFileClip('Audio.wav') as audio:
    duration = audio.duration
# Initialize subtitle counter and timestamps
subtitle_num = 1
start_time = 0
end_time = 0

# Process each audio segment and generate subtitle
with audio_file as source:
    sound = AudioSegment.from_wav("Audio.wav")
    chunks = split_on_silence(sound,
        min_silence_len=500,
        silence_thresh=sound.dBFS-14,
        keep_silence=500
        )   
    
    # Transcribe each chunk
    recognizer = sr.Recognizer()
    subtitles = []
    for i, chunk in enumerate(chunks):
        chunk_path = f"chunk{i}.wav"
        chunk.export(chunk_path, format="wav")
    # while start_time < audio_file.DURATION:
        with sr.AudioFile(chunk_path) as source:
          audio = recognizer.record(source)
          try:
              text = r.recognize_sphinx(audio)
          except sr.UnknownValueError:
              text = ""

        # Calculate the end time of the subtitle
          start_time = (i * 500) / 100.0
          end_time = ((i+1) * 500) / 100.0
          # end_time = start_time + audio_duration
          print(end_time)

          #Write the subtitle to the subtitle file
          subtitle_file.write(str(subtitle_num) + '\n')
          start_time_str = '{:0>8}'.format(str(datetime.timedelta(seconds=start_time)))[:8]
          end_time_str = '{:0>8}'.format(str(datetime.timedelta(seconds=end_time)))[:8]

          subtitle_file.write(start_time_str + ' --> ' + end_time_str + '\n')
          subtitle_file.write(text + '\n\n')

          # Move to the next audio segment
          start_time = end_time
          subtitle_num += 1

# Close the subtitle file
subtitle_file.close()

# **************************************

# Remove all the chunk files
for filename in os.listdir("."):
    if filename.startswith("chunk") and filename.endswith(".wav"):
        os.remove(filename)

# **************************************

