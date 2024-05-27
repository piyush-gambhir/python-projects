import cv2
import numpy as np
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Define the path to the input encrypted video file
encrypted_video_file_path = "C:\\Users\\mainp\\OneDrive\\Desktop\\Test Document Video.mp4"

# Define the path to the input key file
key_file_path = "C:\\Users\\mainp\\OneDrive\\Desktop\\Test Document Key.txt"

# Read in the encrypted video file as a numpy array using OpenCV
encrypted_data = cv2.VideoCapture(encrypted_video_file_path).read()[1].flatten()

# Read in the encryption key and initialization vector (IV) from the key file
with open(key_file_path, "r") as f:
    key = bytes.fromhex(f.readline().split(": ")[1].strip())
    iv = bytes.fromhex(f.readline().split(": ")[1].strip())

# Create an AES cipher object with the key and IV
cipher = AES.new(key, AES.MODE_CBC, iv)

# Decrypt the video data using the AES cipher
decrypted_data = cipher.decrypt(encrypted_data)

# Remove the padding from the decrypted data
plaintext = unpad(decrypted_data, AES.block_size)

# Save the decrypted data to a new file
with open("C:\\Users\\mainp\\OneDrive\\Desktop\\Decrypted Test Document.docx", "wb") as f:
    f.write(plaintext)
