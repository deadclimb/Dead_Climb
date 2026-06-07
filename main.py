import pygame
import sys
import math
import random
import json
import os

# Initialize Pygame & Fullscreen Landscape
pygame.init()
screen_info = pygame.display.Info()
w = screen_info.current_w
h = screen_info.current_h
if w < h:
    SCREEN_WIDTH = h
    SCREEN_HEIGHT = w
else:
    SCREEN_WIDTH = w
    SCREEN_HEIGHT = h

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Dead Climb - Made by Abhishek")

# [Your full game code continues perfectly below this in your notebook cell...]
print("main.py has been written successfully!")

# ==========================================
# STEP 2: INSTALL THE FACTORY TOOLS
# ==========================================
!pip install buildozer cython==0.29.33
!sudo apt-get install -y python3-pip build-essential git python3-dev ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev

# ==========================================
# STEP 3: INITIALIZE & BUILD THE APK
# ==========================================
# Generate the buildozer.spec configuration file automatically
!buildozer init

# Build the Android debug APK package
!buildozer -v android debug
