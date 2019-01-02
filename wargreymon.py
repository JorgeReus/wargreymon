from __future__ import division
from asciimatics.effects import BannerText, Print, Scroll
from asciimatics.renderers import ColourImageFile, FigletText, ImageFile
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
import threading
from deployELD import deployELD
import sys
import time

processing_text = 'PROCESSING'

def animation(screen):
    global processing_text
    scenes = []
    effects = [
        Print(screen,
              ColourImageFile(screen, "wargreymon.gif", screen.height - 15,
                              uni=screen.unicode_aware,
                              dither=screen.unicode_aware),
              0, stop_frame=100),
        Print(screen,
              FigletText(processing_text,
                         font='banner3' if screen.width > 80 else 'banner'),
              screen.height-10,
              colour=7, bg=7 if screen.unicode_aware else 0),
    ]
    scenes.append(Scene(effects))
    screen.play(scenes, stop_on_resize=True, repeat=False)


if __name__ == "__main__":
    t = threading.Thread(target=deployELD)
    t.start()
    while True:
        try:
            if not t.isAlive():
              processing_text = 'FINISHED'
              Screen.wrapper(animation)
              sys.exit(0)
            else:
              Screen.wrapper(animation)
        except ResizeScreenError:
          pass