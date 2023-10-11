import face_recognition
import cv2
import webbrowser
import pyttsx3
import getpass
import os
import datetime

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Function to speak text using the text-to-speech engine
def speak(text):
    engine.say(text)
    engine.runAndWait()

def cam_using():
    
    Time = datetime.datetime.now().strftime("%H %M")
    cam = cv2.VideoCapture(0)
    ret , frame = cam.read()
    if not ret:
        print("failed to grab frame")
        quit()
    cv2.imshow('',frame)
    img_name = "opencv_frame_{}.png".format(Time)
    cv2.imwrite(img_name, frame)
    speak('shuting down computer')
    # os.system("shutdown /s /t 0")
    quit()
    
def password():
    speak("Face Authentication failed")
    print("Face Authentication failed")

    # Allow three chances to enter the correct password

    print('Please enter your password:')
    speak('Please enter your password:')
    code = getpass.getpass(prompt="Password: ")
    if code == '9441':
        speak("Authentication successful")
        speak("Activating assistant")
        webbrowser.open("C:\\Users\\91630\\Desktop\\Project-V\\PROJECT_V.PY") # Exit the loop after successful authentication
    else:
        speak("Authentication failed")
        print('Authentication failed')
        cam_using()
    
        # os.system("shutdown /s /t 0")
# Function to perform face recognition from the webcam
def face_recognition_from_webcam(known_faces):
    # Initialize variables
    face_locations = []
    face_encodings = []
    face_names = []

    # Open the webcam
    video_capture = cv2.VideoCapture(0)

    frame_counter = 0  # Counter to keep track of frames processed

    while True:
        # Capture a frame from the webcam
        ret, frame = video_capture.read()

        # Find all face locations and encodings in the frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        # Clear the list of face names for the current frame
        face_names = []

        for face_encoding in face_encodings:
            # Compare the face encoding with the known faces
            matches = face_recognition.compare_faces(known_faces["encodings"], face_encoding)

            name = "Unknown"

            # If a match is found, use the name of the known face
            if True in matches:
                first_match_index = matches.index(True)
                name = known_faces["names"][first_match_index]

            face_names.append(name)

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Draw a rectangle around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with the name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        # Display the frame with recognized faces
        cv2.imshow("Webcam Face Recognition", frame)

        # Print the output of each frame
        print("Frame:", frame_counter)
        print("Detected Faces:", face_names)

        # Increment the frame counter
        frame_counter += 1

        # Automatically close the video window after processing a certain number of frames (e.g., 100 frames)
        if frame_counter >= 3:
            break

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the OpenCV window
    video_capture.release()
    cv2.destroyAllWindows()

    # Return the list of recognized face names
    return face_names

# Load the known faces and their names
known_face_encodings = []
known_face_names = []

# Load and encode the known faces
# Replace these paths with the paths to your known faces
image_path1 = "C:\\Users\\91630\\Desktop\\Project-V\\face1.jpg"  # Replace with the path to the first known face image
image_path2 = "C:\\Users\\91630\\Desktop\\Project-V\\face2.jpg"  # Replace with the path to the second known face image

charan = face_recognition.load_image_file(image_path1)
Akhil = face_recognition.load_image_file(image_path2)

# Check if faces are detected in the images
if len(face_recognition.face_encodings(charan)) > 0:
    known_face_encoding1 = face_recognition.face_encodings(charan)[0]
    known_face_encodings.append(known_face_encoding1)
    known_face_names.append("Charan")
else:
    print("No face detected in the first image.")

if len(face_recognition.face_encodings(Akhil)) > 0:
    known_face_encoding2 = face_recognition.face_encodings(Akhil)[0]
    known_face_encodings.append(known_face_encoding2)
    known_face_names.append("Akhil")
else:
    print("No face detected in the second image.")

# Create a dictionary to hold known faces and their names
known_faces_dict = {
    "encodings": known_face_encodings,
    "names": known_face_names
}

# Call the face recognition function with the known faces
recognized_faces = face_recognition_from_webcam(known_faces_dict)

# Print all recognized face names in a list
if not recognized_faces:
    print("Can't detect any faces from the webcam.")
else:
    print("Recognized Faces:", recognized_faces)

# List of predefined face names to check against
faces_to_check = ['Charan', 'Akhil', 'Jashu']

# Check if any recognized face is in the predefined list
for name in recognized_faces:
    if name in faces_to_check:
        speak("Authentication successful")
        speak("Activating assistant")
        #b=print(name)
        #speak("welcome",b)
        webbrowser.open("C:\\Users\\91630\\Desktop\\Project-V\\PROJECT_V.PY")
        quit()
        break
    

password()
# Function for password authentication

        

# Call the password function for authentication

