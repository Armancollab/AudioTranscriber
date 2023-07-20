## Speech-to-Text Transcriber

This is a simple Python script that allows you to transcribe speech from an audio file using the AssemblyAI API. The script uses the `assemblyai` library to perform the speech-to-text conversion.

### Requirements

- Python 3.x
- AssemblyAI Python library (`assemblyai`)

### Installation

1. Make sure you have Python 3.x installed on your system.
2. Install the AssemblyAI library using pip:
   ```
   pip install assemblyai
   ```

### How to Use

1. Clone or download the repository from GitHub.

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the script using Python:
   ```
   python main.py
   ```

4. The script will prompt you to select an audio file (in `.ogg` or `.wav` format) using a file dialog window.

5. After selecting the audio file, the script will transcribe the speech and display the result in the terminal.

6. You will then be asked if you want to save the transcript to a text file. If you choose to save, another file dialog window will appear, allowing you to choose the location to save the transcript.

### Note

- The script uses the AssemblyAI API to perform speech-to-text transcription. You need to have an API key from AssemblyAI.

### License

This project is licensed under the [MIT License](LICENSE).

### Contributions

Contributions and suggestions are welcome! Feel free to submit issues or pull requests.

### Acknowledgments

- This project uses the AssemblyAI API to perform speech-to-text transcription. More information about the API can be found on the [AssemblyAI website](https://www.assemblyai.com/).
