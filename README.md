# Flask AI Web Application

This repository contains the source code for an AI web application developed using the Flask framework. This project was created as the final capstone for the IBM Full Stack Software Developer Professional Certificate course, "Developing AI Applications with Python and Flask."

The core functionality is to perform emotion detection from text input.

## Key Features

- **Emotion Detection**: Extends sentiment analysis by extracting more nuanced emotions such as joy, sadness, anger, and others from text. This is achieved by using the Watson NLP library.

- **Web-based Interface**: A user-friendly front end built with HTML, CSS, and JavaScript for seamless user interaction.

- **API Endpoint**: The backend Flask server provides an API endpoint to handle text analysis requests and return the emotion detection results.

- **Unit Testing**: Includes unit tests to validate the application's core logic.

## Technologies Used
- **Python**: The primary programming language for the back end.

- **Flask**: A Python micro-framework used to build the web application.

- **Watson NLP Library**: The AI library used for emotion detection.

- **HTML, CSS, JavaScript**: Used for the front end of the web application.

## Getting Started
These instructions will get a copy of the project up and running on your local machine for development and testing.

## Prerequisites
To run this application, you will need Python 3.x and pip installed.

## Installation
### 1. Clone the repository:

`git clone https://github.com/DoodlesHuman/final-project-flask.git`
`cd final-project-flask`

### 2. Install the required packages:

`pip install -r requirements.txt`

## Usage

### 1. Run the Flask server:

`python server.py`

### 2. Access the application:

Open your web browser and navigate to `http://127.0.0.1:5000`. Enter text into the field and press the button to get an emotion analysis.

## Testing

The repository includes a test file to verify the functionality.

### Run the tests:

`python test_emotion_detection.py`

## Credits and Acknowledgments

- **Amos Ram Rehum**: The repository owner and primary contributor.

- **IBM Developer Skills Network**: For providing the foundational course material and initial project structure that this repository is forked from.
