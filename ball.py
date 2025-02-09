

class Ball():
    def __init__(self,pos):
        self.pos = list(pos)
        #self.color = 

    def move_down(self,dy):
        self.pos[1] += dy

    def move_up(self,dy):
        self.pos[1]-= dy

    def move_left(self,dx):
        self.pos[0] -= dx

    def move_right(self,dx):
        self.pos[0] += dx
        
    def get_pos(self):
        return tuple(self.pos)
    
    def update_ball(self):
        pass

