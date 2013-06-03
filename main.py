
import pygame
import os
import time

pygame.mixer.init()
char_time = .75
word_time = 1.5

sound = pygame.mixer.Sound('beep.wav')

def longbeep():
    len = .75
    sound.play()
    time.sleep(len)
    sound.stop()
    
def shortbeep():
    len = .25
    sound.play()
    time.sleep(len)
    sound.stop()

dot = lambda:shortbeep()
dash = lambda:longbeep()

morse_code = {
    'a':[dot, dash],
    'b':[dash, dot, dot, dot],
    'c':[dash, dot, dash, dot],
    'd':[dash, dot, dot],
    'e':[dot],
    'f':[dot, dot, dash, dot],
    'g':[dash, dash, dot],
    'h':[dot, dot, dot, dot],
    'i':[dot, dot],
    'j':[dot, dash, dash, dash],
    'k':[dash, dot, dash],
    'l':[dot, dash, dot, dot],
    'm':[dash, dash],
    'n':[dash, dot],
    'o':[dash, dash, dash],
    'p':[dot, dash, dash, dot],
    'q':[dash, dash, dot, dash],
    'r':[dot, dash, dot],
    's':[dot, dot, dot],
    't':[dash],
    'u':[dot, dot, dash],
    'v':[dot, dot, dot, dash],
    'w':[dot, dash, dash],
    'x':[dash, dot, dot, dash],
    'y':[dash, dot, dash, dash],
    'z':[dash, dash, dot, dot],
    
    '1':[dot, dash, dash, dash, dash],
    '2':[dot, dot, dash, dash, dash],
    '3':[dot, dot, dot, dash, dash],
    '4':[dot, dot, dot, dot, dash],
    '5':[dot, dot, dot, dot, dot],
    '6':[dash, dot, dot, dot, dot],
    '7':[dash, dash, dot, dot, dot],
    '8':[dash, dash, dash, dot, dot],
    '9':[dash, dash, dash, dash, dot],
    '0':[dash, dash, dash, dash, dash]
    
}

user = input('Convert this to morse code: ')
for char in user:
    char = char.lower()
    if char == ' ':
        time.sleep(word_time) #space between words
        continue
    try:
        if morse_code[char]:
            #print(char)
            for ch in morse_code[char]:
                ch()
                time.sleep(.25) #space between dots and dashs in one char
            time.sleep(char_time) #space between chars
    except KeyError:
        pass

