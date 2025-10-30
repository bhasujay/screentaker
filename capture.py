import threading
from time import sleep
from PIL import ImageGrab
import hashlib
    

class ScreenShot:
    
    id = 0

    def __init__(self, image):
        self.image = image
        self.top_match_line = -1
        self.bottom_match_line = -1
        self.rendered = False
        self.id = ScreenShot.id
        
        ScreenShot.id += 1
        
    def top_match(self, top):
        self.top_match_line = top
        
    def bottom_match(self, bottom):
        self.bottom_match_line = bottom
        
    @classmethod
    def reset_id(cls):
        cls.id = 0
        
    def __del__(self):
        self.image = None


class CaptureManager:

    def __init__(self):

        self.shot_list = []
        self.shot_count = 0
        self.thread = None
        self.capturing = False
        self.last_image = None  

    def listen_to_clipboard(self):
        if self.capturing:
            return
        self.capturing = True
        self.thread = threading.Thread(target=self._clipboard_listener)
        self.thread.start()
        
    def _clipboard_listener(self):
        while self.capturing:
            shot = ScreenShot(ImageGrab.grabclipboard())
            if isinstance(shot.image, ImageGrab.Image.Image):
                if self.last_image is None or not self._images_are_equal(shot.image, self.last_image):
                    self.shot_list.append(shot)
                    self.shot_count += 1
                    self.last_image = shot.image
            sleep(0.5)

    def _images_are_equal(self, img1, img2):
        hash1 = hashlib.md5(img1.tobytes()).hexdigest()
        hash2 = hashlib.md5(img2.tobytes()).hexdigest()
        return hash1 == hash2

    def close_clipboard_listener(self):
        self.capturing = False
        sleep(0.5) # give some time for the thread to finish
        if self.thread is not None:
            self.thread.join()
            self.thread = None

    def __del__(self):
        self.shot_list = []
        self.last_image = None