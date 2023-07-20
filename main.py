import os
import assemblyai as aai
from tkinter import filedialog
import tkinter as tk

def get_api_key():
    api_key = input("Enter your AssemblyAI API key: ")
    return api_key.strip()

def transcribe_and_show_text(api_key, audio_file_path):
    try:
        aai.settings.api_key = api_key
        transcriber = aai.Transcriber()
        transcript = transcriber.transcribe(audio_file_path)
        text = transcript.text
        print("Transcription Result:")
        print(text)
        return text
    except Exception as e:
        print("Transcription failed. Error:", e)
        return None

def save_transcript(transcribed_text):
    if transcribed_text:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt", filetypes=[("Text files", "*.txt")]
        )
        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write(transcribed_text)
                print("Transcript saved successfully.")
            except Exception as e:
                print("Failed to save transcript. Error:", e)
    else:
        print("There is no text to save.")

def main():
    print("Speech-to-Text Transcriber")
    api_key = get_api_key()

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        filetypes=[("Audio files", "*.ogg;*.wav")]
    )
    if not file_path:
        print("No file selected. Exiting.")
        return

    print("Selected Audio File:", file_path)

    transcribed_text = transcribe_and_show_text(api_key, file_path)

    save_choice = input("Do you want to save the transcript? (yes/no): ").lower()
    if save_choice == "yes":
        save_transcript(transcribed_text)
    else:
        print("Transcript not saved.")

if __name__ == "__main__":
    main()
