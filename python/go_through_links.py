from subprocess import Popen

import keyboard
import pyperclip
import time


links = pyperclip.paste().split('\n')

finish = []
for i, link in enumerate(links):
    print(f'{i+1}/{len(links)}')
    try:
        _ = Popen(['start', 'chrome', link], shell=True)
    except:
        pass
    keyboard.wait('ctrl+i')
    time.sleep(0.3)
    keyboard.press_and_release('ctrl+w')
    finish.append(link)


not_finished = set(links).difference(finish)
pyperclip.copy('\n'.join(not_finished))