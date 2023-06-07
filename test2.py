
from pygame import mixer
import time
mixer.init() #Initialzing pyamge mixer

mixer.music.load('TheWorthyMusic.mp3') #Loading Music File

mixer.music.play() #Playing Music with Pygame

time.sleep(5)