from PyPDF2 import PdfReader
from gtts import gTTS
import pygame

with open ("resume.pdf", "rb") as file:
    reader = PdfReader(file)
    first_page = reader.pages[0]
    text = first_page.extract_text()
print(text)   

tts = gTTS(text)
tts.save("first_page.mp3")

print("First page MP3 created")

pygame.mixer.init()
pygame.mixer.music.load("first_page.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pass