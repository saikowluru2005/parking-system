import streamlit as st
import cv2
import numpy as np
import tempfile
import time

st.title("Real-Time Parking Slot Detection")

uploaded_video = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

if uploaded_video:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_video.read())
    video_path = tfile.name
    
    cap = cv2.VideoCapture(video_path)
    
    stframe = st.empty()
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Placeholder for parking slot detection (You need to implement or train a model for detection)
        vacant_slots = np.random.randint(5, 15)  # Example random count for demo purposes
        occupied_slots = np.random.randint(5, 15)
        
        # Display counts on frame
        cv2.putText(frame, f"Vacant: {vacant_slots}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f"Occupied: {occupied_slots}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        # Convert color from BGR to RGB for Streamlit
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Display the frame in the Streamlit app
        stframe.image(frame, channels="RGB")
        
        time.sleep(0.05)  # Adjust frame rate for smoothness
    
    cap.release()
    st.success("Video processing completed!")