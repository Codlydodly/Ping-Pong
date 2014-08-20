import Tkinter
import tkMessageBox

def callback(event):
    movecircle(C, circ1)
    movecircle(C, circ2)

class set_up(object):
           

    def create_pong(self):


        top = Tkinter.Tk()

        C = Tkinter.Canvas(top, bg="black", height= 350, width=600)
       
        self.net = self.paddle_and_net(C, 295, 360, 305, 0, "white")
        self.paddle_1 = self.paddle_and_net(C, 20, 5, 10, 100, "white")
        self.paddle_2 = self.paddle_and_net(C, 585, 250, 595, 345, "white")
        self.ball_1 = self.ball(C)
        

        C.pack()   
        self.handle_keyboard(C)
        top.mainloop()   

      

    def move_paddl1(self, Canvas, event):
        Canvas.coords(self.paddle_1, 20, event.y, 10, event.y + 95)

    def handle_keyboard(self, Canvas):
        callback = lambda event : self.move_paddl1(Canvas, event)
        Canvas.bind("<B1-Motion>", callback)

    def paddle_and_net(self, Canvas, x1, y1, x2, y2, fill):
        return Canvas.create_rectangle(x1, y1, x2, y2, fill=fill)

    def ball(self,Canvas):
        return Canvas.create_oval(90, 90, 110, 110, width="0", fill="green")

   

pp = set_up()
pp.create_pong()