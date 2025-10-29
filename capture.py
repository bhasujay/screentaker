import threading
import time
from PIL import ImageGrab
import hashlib


class CaptureManager:

    def __init__(self):
        self.image_list = []
        self.image_count = 0
        self.thread = None
        self.capturing = False
        self.lock = threading.Lock()
        self.last_image = None  

    def listen_to_clipboard(self):
        if self.capturing:
            return
        self.capturing = True
        self.thread = threading.Thread(target=self._clipboard_listener)
        self.thread.start()
        
    def _clipboard_listener(self):
        while self.capturing:
            img = ImageGrab.grabclipboard()
            if isinstance(img, ImageGrab.Image.Image):
                if self.last_image is None or not self._images_are_equal(self.last_image, img):
                    self.image_list.append(img)
                    self.image_count += 1
                    self.last_image = img
            time.sleep(1)

    def _images_are_equal(self, img1, img2):
        hash1 = hashlib.md5(img1.tobytes()).hexdigest()
        hash2 = hashlib.md5(img2.tobytes()).hexdigest()
        return hash1 == hash2


    def close_clipboard_listener(self):
        self.capturing = False
        if self.thread is not None:
            self.thread.join()
            self.thread = None

    def __del__(self):
        self.image_list = []

