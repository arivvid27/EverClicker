# Imports
from pynput.mouse import Listener
import pygame
import random
import platform
import os

# Initialization
# pygame.mixer.init()
# fx = pygame.mixer.Sound()
# click = fx.play()
# chiching = fx.play()
# combo = fx.play()
# error = fx.play()

# Title Styles
style1 = """
███████╗██╗░░░██╗███████╗██████╗░░█████╗░██╗░░░░░██╗░█████╗░██╗░░██╗███████╗██████╗░
██╔════╝██║░░░██║██╔════╝██╔══██╗██╔══██╗██║░░░░░██║██╔══██╗██║░██╔╝██╔════╝██╔══██╗
█████╗░░╚██╗░██╔╝█████╗░░██████╔╝██║░░╚═╝██║░░░░░██║██║░░╚═╝█████═╝░█████╗░░██████╔╝
██╔══╝░░░╚████╔╝░██╔══╝░░██╔══██╗██║░░██╗██║░░░░░██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
███████╗░░╚██╔╝░░███████╗██║░░██║╚█████╔╝███████╗██║╚█████╔╝██║░╚██╗███████╗██║░░██║
╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░╚════╝░╚══════╝╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
"""
style2 = """
╭━━━╮╱╱╱╱╱╱╱╭━━━┳╮╱╱╱╱╭╮
┃╭━━╯╱╱╱╱╱╱╱┃╭━╮┃┃╱╱╱╱┃┃
┃╰━━┳╮╭┳━━┳━┫┃╱╰┫┃╭┳━━┫┃╭┳━━┳━╮
┃╭━━┫╰╯┃┃━┫╭┫┃╱╭┫┃┣┫╭━┫╰╯┫┃━┫╭╯
┃╰━━╋╮╭┫┃━┫┃┃╰━╯┃╰┫┃╰━┫╭╮┫┃━┫┃
╰━━━╯╰╯╰━━┻╯╰━━━┻━┻┻━━┻╯╰┻━━┻╯
"""
style3 = """
█▀▀ █░█ █▀▀ █▀█ █▀▀ █░░ █ █▀▀ █▄▀ █▀▀ █▀█
██▄ ▀▄▀ ██▄ █▀▄ █▄▄ █▄▄ █ █▄▄ █░█ ██▄ █▀▄
"""
style4 = """
█▄─▄▄─█▄─█─▄█▄─▄▄─█▄─▄▄▀█─▄▄▄─█▄─▄███▄─▄█─▄▄▄─█▄─█─▄█▄─▄▄─█▄─▄▄▀█
██─▄█▀██▄▀▄███─▄█▀██─▄─▄█─███▀██─██▀██─██─███▀██─▄▀███─▄█▀██─▄─▄█
▀▄▄▄▄▄▀▀▀▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀
"""
style5 = """
░█▀▀▀ ▀█─█▀ █▀▀ █▀▀█ ░█▀▀█ █── ─▀─ █▀▀ █─█ █▀▀ █▀▀█ 
░█▀▀▀ ─█▄█─ █▀▀ █▄▄▀ ░█─── █── ▀█▀ █── █▀▄ █▀▀ █▄▄▀ 
░█▄▄▄ ──▀── ▀▀▀ ▀─▀▀ ░█▄▄█ ▀▀▀ ▀▀▀ ▀▀▀ ▀─▀ ▀▀▀ ▀─▀▀
"""

# Credits
credits = """
ℭ𝔬𝔭𝔶𝔯𝔦𝔤𝔥𝔱 © 2023 𝔈𝔳𝔢𝔯𝔢𝔰𝔱𝔚𝔬𝔯𝔨𝔰® 
𝔄𝔩𝔩 ℜ𝔦𝔤𝔥𝔱𝔰 ℜ𝔢𝔰𝔢𝔯𝔳𝔢𝔡
"""

# Title and Credits
def titleNcredits():
    title_design = [1, 2, 3, 4, 5]
    title = random.randint(1,5)
    if title == 1:
        print(style1)
        print(credits)
    elif title == 2:
        print(style2)
        print(credits)
    elif title == 3:
        print(style3)
        print(credits)
    elif title == 4:
        print(style4)
        print(credits)
    elif title == 5:
        print(style5)
        print(credits)    
    

with Listener() as listener:
    listener.join()

clicks = 0

def on_click(clicked):
    if clicked:
        print("Clicked")

def clear_screen():
    if platform == "windows":
        os.system('cls')
    else:
        os.system('clear')

def main():
    pass

if __name__ == '__main__':
    main()