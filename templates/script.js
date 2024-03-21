document.getElementById('microphone').addEventListener('click', startRecording);

function startRecording() {
    // Simulate recording by waiting for 7 seconds
    setTimeout(processAudio, 7000);
}

function processAudio() {
    // Get audio data from user's microphone (not implemented here)
    // For now, let's assume we have the audio data
    var audioData = "dummy_audio_data";

    // Send audio data to the Flask backend for processing
    fetch('/process_audio', {
        method: 'POST',
        body: audioData,
    })
    .then(response => response.json())
    .then(data => displayRecognizedSpeaker(data.recognized_speaker))
    .catch(error => console.error('Error:', error));
}

function displayRecognizedSpeaker(name) {
    var recognizedSpeakerElement = document.getElementById('recognizedSpeaker');
    recognizedSpeakerElement.innerHTML = "<p>Recognized Speaker: " + name + "</p>";
}
