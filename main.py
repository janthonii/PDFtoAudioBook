import pyttsx3
import PyPDF2
from tkinder.filedialog import *

# Check if a file was selected
if not book:
    print("No file selected. Exiting the program.")
else:
    try:
        # Initialize the PDF reader
        pdfreader = PyPDF2.PdfFileReader(book)
        pages = pdfreader.numPages
        print(f"Reading the PDF... Total pages: {pages}")

        # Initialize the text-to-speech engine
        player = pyttsx3.init()

        # Loop through each page and convert to audio
        for num in range(pages):
            page = pdfreader.getPage(num)
            text = page.extractText()
            print(f"Reading page {num + 1}...")
            player.say(text)
            player.runAndWait()

        print("Finished reading the PDF!")
    except Exception as e:
        print(f"An error occurred: {e}")