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
        self.ball_1 = self.ball(C)        

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
        x = 5
        y = 5
        while True:
            if (self.check_collision(Canvas, Canvas.coords(self.ball_1)) == False):
                x = -x
            elif (self.check_collision(Canvas, Canvas.coords(self.ball_1)) == True):
                y = -y            

            Canvas.move(self.ball_1, x, y)
            time.sleep(0.001)

    def check_collision(self, Canvas, position):
        if (position[0] == Canvas.coords(self.paddle_1)[2]):
            return False
        elif (position[2] == Canvas.coords(self.paddle_2)[0]):
            return False
        elif (position[0] == 0) or (position[0] == 600):
            return False
            # If this happens the ball should be reset and a point given
        elif ((position[1] ==0) or (position[1] == 350)):
            return True
        elif ((position[2] == 0) or (position[2] == 600)):
            return False
            # If this happens the ball should be reset and a point given
        elif ((position[3] ==0) or (position[3] == 350)):
            return True
        else:
            return 



pp = set_up()
pp.create_pong()