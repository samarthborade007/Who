<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Who! - Deep Residual Network (ResNet) based Speaker Recognition System</title>
</head>
<body>
    <h1>Who! - Deep Residual Network (ResNet) based Speaker Recognition System</h1>

    <img src="https://img.shields.io/github/license/yourusername/Who-Deep-ResNet-Speaker-Recognition" alt="License">
    <img src="https://img.shields.io/github/last-commit/yourusername/Who-Deep-ResNet-Speaker-Recognition" alt="Last Commit">
    <img src="https://img.shields.io/github/issues/yourusername/Who-Deep-ResNet-Speaker-Recognition" alt="Issues">

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

    <h2>Contributing</h2>

    <p>Contributions to enhance the system, improve performance, or add new features are welcome. Please follow the <a href="CONTRIBUTING.md">contributing guidelines</a> and <a href="CODE_OF_CONDUCT.md">code of conduct</a>.</p>

    <h2>License</h2>

    <p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>

    <h2>Acknowledgements</h2>

    <p>This project was inspired by the need for accurate speaker recognition systems and leverages the power of deep learning techniques. Special thanks to the contributors and the open-source community for their valuable resources and support.</p>

    <h2>Contact</h2>

    <p>For any inquiries or feedback, please reach out to <a href="https://github.com/yourusername">yourusername</a>.</p>
</body>
</html>
