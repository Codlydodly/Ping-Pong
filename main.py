import Tkinter
import tkMessageBox
import time
import thread


class set_up(object):

    


    def create_pong(self): 
        top = Tkinter.Tk()
        C = Tkinter.Canvas(top, bg="black", height= 350, width=600)        
        top.after(0, self.run, C)
        top.mainloop()

    def run(self, C):      
        self.net = self.paddle_and_net(C, 295, 360, 305, 0, "white")
        self.paddle_1 = self.paddle_and_net(C, 20, 5, 10, 100, "white")
        self.paddle_2 = self.paddle_and_net(C, 585, 250, 595, 345, "white")
        self.ball = self.ball(C)
        self.x = 5
        self.y = 5
            

        C.pack()
        thread.start_new_thread ( self.move_ball, (C,))
        # self.move_ball(C)
        self.handle_keyboard(C)
        C.focus_set()
        # top.after(0, self.run, C)


    def move_up(self, Canvas, event):        
        Canvas.move(self.paddle_2, 0, -5)
    
    def move_down(self, Canvas, event):        
        Canvas.move(self.paddle_2, 0, 5)

    def move_w(self, Canvas, event):        
        Canvas.move(self.paddle_1, 0, -5)
    
    def move_s(self, Canvas, event):        
        Canvas.move(self.paddle_1, 0, 5)


    def handle_keyboard(self, Canvas):

        move_up = lambda event : self.move_up(Canvas, event)
        Canvas.bind("<Up>", move_up)

        move_down = lambda event : self.move_down(Canvas, event)
        Canvas.bind("<Down>", move_down)


        move_w = lambda event : self.move_w(Canvas, event)
        Canvas.bind("w", move_w)

        move_s = lambda event : self.move_s(Canvas, event)
        Canvas.bind("s", move_s)
    

    def paddle_and_net(self, Canvas, x1, y1, x2, y2, fill):
        return Canvas.create_rectangle(x1, y1, x2, y2, fill=fill)

    def ball(self,Canvas):
        return Canvas.create_oval(90, 90, 110, 110, width="0", fill="green")

    def move_ball(self, Canvas):
        # print self.x     
        
        if (self.check_collision(Canvas, Canvas.coords(self.ball)) == False):
            self.x = -self.x
        elif (self.check_collision(Canvas, Canvas.coords(self.ball)) == True):
            self.y = -self.y            

        Canvas.move(self.ball, self.x, self.y)
        Canvas.after(100, self.move_ball, (Canvas))


    def check_collision(self, Canvas, position):
        radius = 10
        if (position[0] == Canvas.coords(self.paddle_1)[2]) and (position[1] > Canvas.coords(self.paddle_1)[1]) and (position[1] < Canvas.coords(self.paddle_1)[3]):
            return False
        elif (position[2] == Canvas.coords(self.paddle_2)[0]) and (position[1] > Canvas.coords(self.paddle_2)[1]) and (position[1] < Canvas.coords(self.paddle_2)[3]):
            return False
        elif (position[0] < 0 + radius): 
            return False
            # If this happens the ball should be reset and a point given
        elif (position[1] < 0 + radius):
            return True
        elif (position[2] > 600):
            return False
            # If this happens the ball should be reset and a point given
        elif (position[3] > 350):
            return True
        else:
            return

pp = set_up()
pp.create_pong()