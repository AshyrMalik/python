import tkinter as tk
from tkinter import messagebox
import pyttsx3

# Initialize text-to-speech
engine = pyttsx3.init()

# Function to process commands
def process_command():
    command = entry.get()
    # Clear the entry box after getting the command
    entry.delete(0, tk.END)
    
    if "open calculator" in command.lower():
        response = "Opening calculator."
        # Add logic to open the calculator (Windows example)
        # os.system('calc')
    elif "play music" in command.lower():
        response = "Playing music from your local files."
        # Logic to play a music file
    else:
        response = "I didn't understand that command."

    # Display and speak response
    output_label.config(text=response)
    engine.say(response)
    engine.runAndWait()

# Initialize GUI
root = tk.Tk()
root.title("Offline Personal Assistant")

# Entry box for commands
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Button to submit commands
submit_btn = tk.Button(root, text="Submit", command=process_command)
submit_btn.pack(pady=10)

# Output label for responses
output_label = tk.Label(root, text="", fg="blue")
output_label.pack(pady=20)

root.mainloop()