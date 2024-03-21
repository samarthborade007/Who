<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style> .center {display: block;margin-left: auto;margin-right: auto;width: 50%; }</style>
</head>
<body>
    <h1>Who! - Deep Residual Network (ResNet) based Speaker Recognition System</h1>
    <img src="logo.png" alt="Who! Logo" class="center" style="width: 600px; height: auto;">
    <h2>Overview</h2>
    <p>Who! is a speaker recognition system based on Deep Residual Network (ResNet) architecture. It utilizes Fast Fourier Transform (FFT) to extract frequency domain features from speech recordings and employs a 1D convolutional neural network (CNN) with residual connections for speaker classification.</p>
    <h2>Features</h2>
    <ul>
        <li>Classification of speakers from speech recordings</li>
        <li>Preprocessing of audio data, including resampling, noise addition, and FFT transformation</li>
        <li>Implementation of ResNet architecture for robust feature extraction and classification</li>
        <li>Evaluation metrics include accuracy and loss</li>
        <li>Model checkpointing and early stopping for efficient training</li>
        <li>Visualization of class distribution and ratios</li>
    </ul>
    <h2>Requirements</h2>
    <ul>
        <li>Python 3</li>
        <li>TensorFlow 2.x</li>
        <li>NumPy</li>
        <li>Keras</li>
        <li>Matplotlib</li>
    </ul>
    <h2>Dataset</h2>
    <p>The dataset used for training and validation should be organized into two main categories:</p>
    <ol>
        <li><strong>Speech Samples:</strong> Contains folders for different speakers, each with audio files sampled at 16,000 Hz.</li>
        <li><strong>Background Noise Samples:</strong> Includes longer noise files, resampled to 16,000 Hz, for augmentation.</li>
    </ol>
    <h2>Usage</h2>
    <ol>
        <li><strong>Prepare the Dataset:</strong>
            <ul>
                <li>Organize speech and noise samples into the appropriate folders.</li>
                <li>Ensure all noise samples are resampled to 16,000 Hz.</li>
            </ul>
        </li>
        <li><strong>Run the Code:</strong>
            <ul>
                <li>Adjust the configuration parameters in the code as needed (e.g., data directory, batch size, number of epochs).</li>
                <li>Execute the code to preprocess the data, build the ResNet model, train, and evaluate it.</li>
            </ul>
        </li>
        <li><strong>Evaluation:</strong>
            <ul>
                <li>Evaluate the trained model using validation data and analyze performance metrics.</li>
                <li>Save the model and class names for future use.</li>
            </ul>
        </li>
        <li><strong>Prediction:</strong>
            <ul>
                <li>Use the trained model to predict speakers from new speech recordings.</li>
                <li>Visualize class distribution and ratios for insights into the dataset.</li>
            </ul>
        </li>
    </ol>
</body>
</html>
