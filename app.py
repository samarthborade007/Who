from flask import Flask, render_template, request
import os
import wave
import numpy as np
from scipy.signal import resample
from keras.models import load_model

import json

# Load class_names from the JSON file
with open("backend/class_names.json", "r") as f:
    class_names = json.load(f)


app = Flask(__name__, static_folder='static')

# Define the sampling rate
SAMPLING_RATE = 16000

# Load the saved model
model = load_model("backend/speaker_recognition_model.h5")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save-audio', methods=['POST'])
def save_audio():
    if 'audio' in request.files:
        audio = request.files['audio']
        audio_path = os.path.join('audio_files', audio.filename)
        audio.save(audio_path)
        
        # Convert the saved audio file to WAV
        wav_output_file = os.path.join('audio_files', os.path.splitext(audio.filename)[0] + '.wav')
        convert_to_wav(audio_path, wav_output_file)
        
        # Preprocess the audio file
        preprocessed_input = preprocess_audio(wav_output_file)
        
        # Predict the speaker label
        predicted_label_index = np.argmax(model.predict(np.expand_dims(preprocessed_input, axis=0)))
        predicted_speaker = class_names[predicted_label_index]  # Assuming `class_names` is defined
        
        return f'Predicted Speaker: {predicted_speaker}'
    
    return 'No audio file received', 400

def convert_to_wav(input_file, output_file):
    os.system(f"ffmpeg -i {input_file} -ar 16000 {output_file}")

# Function to preprocess input audio
def preprocess_audio(audio_file_path):
    # Open the WAV file
    wav_file = wave.open(audio_file_path, 'r')
    # Get the information about the WAV file
    frames = wav_file.getnframes()
    # Read the frames from the WAV file
    frames = wav_file.readframes(frames)
    wav_file.close()
    # Convert the frames to a NumPy array
    frames = np.frombuffer(frames, dtype=np.int16)
    # Resample the audio to match the model's input sampling rate and length
    target_length = SAMPLING_RATE // 2  # Model expects input of length 8000
    resampled_frames = resample(frames, target_length)

    # Expand the dimensions to match the model's input shape
    audio_input = np.expand_dims(resampled_frames, axis=-1)

    return audio_input

if __name__ == "__main__":
    app.run(debug=True)
