import cv2
import numpy as np
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import secrets

# Define the path to your input word file
word_file_path = "C:\\Users\\mainp\\OneDrive\\Desktop\\Test Document.docx"

# Define the path to your output video file
video_file_path = "C:\\Users\\mainp\\OneDrive\\Desktop\\Test Document Video.mp4"

# Define the path to your output key file
key_file_path = "C:\\Users\\mainp\\OneDrive\\Desktop\\Test Document Key.txt"

# Define your encryption key and initialization vector (IV)
key = secrets.token_bytes(32) 
iv = secrets.token_bytes(16)

# Create an AES cipher object with your key and IV
cipher = AES.new(key, AES.MODE_CBC, iv)

# Read in the word file and encrypt it using the AES cipher
with open(word_file_path, "rb") as f:
    plaintext = f.read()
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

# Convert the encrypted data into a numpy array
encrypted_data = np.frombuffer(ciphertext, dtype=np.uint8)

# Encode the encrypted data into a video file using OpenCV
video_writer = cv2.VideoWriter(video_file_path, cv2.VideoWriter_fourcc(
    *"mp4v"), 1, (len(encrypted_data), 1))
video_writer.write(encrypted_data)

# Release the video writer object
video_writer.release()

# Save the encryption key and IV into a text file
with open(key_file_path, "w") as f:
    f.write("Encryption Key: " + str(key) + "\n")
    f.write("Initialization Vector (IV): " + str(iv))

