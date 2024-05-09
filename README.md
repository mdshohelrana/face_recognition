# Smart Demographic Recognition System

## Overview
The Smart Demographic Recognition System enhances social connectivity by utilizing advanced face recognition technology. This Django-based system captures images, processes them on a server, and displays real-time demographic information including name, age, social activities, and contact details.

## Installation

### Prerequisites
Before you can run the server, you'll need to install the required libraries and dependencies:

### Install essential face recognition libraries
```bash
pip install opencv-python dlib face_recognition
```

### Install other required packages
```bash
pip install -r requirements.txt
```

### Starting the Server
To start the Django server, run the following command, and Navigate to http://127.0.0.1:8000/ in your browser to access the application.

```bash
python manage.py runserver
```

## Usage
### Navigating the Website
1) Identify Faces:
This feature activates the webcam to continuously detect faces. Leave this open in the background for ongoing face detection. To exit, focus on the webcam window and press Q.

2) Detected Faces:
Displays a list of detected employees with options to view records by date.

3) Add Photos:
Use this to capture and train the system with new employee faces. Ensure the employee ID is entered before starting:

Capture 15-20 images by pressing the space bar.
Vary the face angle and distance from the camera for best results.
To exit the webcam, press ESC.
NOTE: If the webcam does not activate, restart the server:

```bash
python manage.py runserver
```

4) Add Employee:
Enter new employee details through this interface.

5) Train Model:
After adding new employee images, retrain the model. Start this process and monitor the training progress via the terminal.

### Technologies Used
Django
SQLite
OpenCV
Facenet Model
LFW Dataset

## Contributing
We welcome contributions to improve accuracy, expand the dataset, and enhance data security. For more information, see CONTRIBUTING.md.

## Challenges
Our ongoing development efforts focus on ensuring user privacy, adapting to diverse conditions, and optimizing performance across different hardware setups.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments
Special thanks to Leonardo Espinosa Leal, Truong An Pham from Arcada University of Applied Sciences and all contributors to the LFW dataset.