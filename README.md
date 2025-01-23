# PDF to Audiobook Converter

## Description
This Python script converts PDF text into audio using `PyPDF2` to extract text and `pyttsx3` for text-to-speech. Users select a PDF via a file dialog, and the program reads it aloud page by page. Simple and effective for creating audiobooks from PDFs.

## Requirements
- Python 3.6 or later
- Libraries: `pyttsx3`, `PyPDF2`, `tkinter`

## Installation
1. Install Python 3.x from [Python's official website](https://www.python.org/).
2. Install the required libraries by running:
   ```bash
   pip install pyttsx3 PyPDF2
   
## Key Features:
- Pop-Up for File Selection: When you run the script, a pop-up window will appear for selecting a PDF file.
- Audio Conversion: The program reads the selected PDF aloud, page by page.
- Error Handling: If no file is selected or an error occurs, the program will print the appropriate message.

## How to Save the Audio File:
1. Save the script to a file, e.g., pdf_to_audio.py.
2. Open your terminal or IDE and run the script:
```bash
   python pdf_to_audio.py
```
3. A pop-up window will appear asking you to select the PDF file you want to convert.
4. Once you select the file, the program will read the PDF aloud, page by page.

