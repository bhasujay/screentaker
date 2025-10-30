from capture import ScreenShot

# states
NOT_ORDERED = -1
NOT_MATCHED = 0
MATCHED = 1

class RenderManager:
    
    def __init__(self):
        self.shot_list = []
        self.master_image = None
        self.master_height = 0
        self.current_count = 0
        
    def add_to_render_queue(self, shot):
        self.shot_list.append(shot)
        self.current_count += 1
        
        # from the second shot onwards, we need to find matches
        if self.current_count > 1:
            if self.shot_list[-1].id > self.shot_list[-2].id:
                return self._update_match(self.shot_list[-2], self.shot_list[-1])
            else:
                return NOT_ORDERED
        else:
            self.master_height = shot.image.height
            return MATCHED
        
    def _update_match(self, top, bottom):
        pass
    
    def __del__ (self):
        self.shot_list = []
        self.master_image = None
        ScreenShot.reset_id()