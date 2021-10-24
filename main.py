from time import sleep
from os import system
from sys import argv

try:
    print(f'running {argv[1]} with {argv[2]} clear command')
except:
    print(f'\nUSAGE:\npython3 {argv[0]} [filename] [clear command for your os (cls/clear)]')
    quit()

def load_slides(filename):
    file = open(filename)
    lines = file.readlines()
    slides = lines[1:]
    info = lines[0].split()
    return info, slides

def print_slide(slides):
    for line in slides:
        if line.startswith('{(-END-)}'):
            sleep(DELAY)
            system(argv[2])
        else:
            print(line)

def get_info(info):
    global DELAY
    global SLIDES
    for setting in info:
        if setting.startswith('delay:'):
            DELAY = float(setting[6:])

info, slides = load_slides(argv[1])
get_info(info)

while True:
    print_slide(slides)
