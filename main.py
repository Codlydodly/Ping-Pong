import Tkinter
import tkMessageBox
import time
import thread

class set_up(object):

    def create_pong(self): 
        top = Tkinter.Tk()
        top.title("Pong")
        C = Tkinter.Canvas(top, bg="black", height= 350, width=600)        
        top.after(0, self.run, C, top)    
        top.mainloop()

    def run(self, C, top):
        self.quit_button = Tkinter.Button(top, text="Quit", highlightbackground="black", command=C.quit)
        self.replay_button = Tkinter.Button(top, text="Replay", highlightbackground="black", command=   lambda: self.reset_score(C, top))
        self.net = self.paddle_and_net(C, 295, 360, 305, 0, "white")
        self.paddle_1 = self.paddle_and_net(C, 20, 5, 10, 100, "white")
        self.paddle_2 = self.paddle_and_net(C, 585, 250, 595, 345, "white")
        self.ball = self.ball(C)
        self.leftscore = 0
        self.rightscore = 0       
        self.score = self.score_board(C, 280, 20, 25, 0)
        self.score2 = self.score_board(C, 320, 20, 25, 0)
        self.x = 5
        self.y = 5        
        self.pressedKeys=set()
        C.pack()
        thread.start_new_thread ( self.move_ball, (C,))
        self.handle_keyboard(C)
        C.focus_set()

    def reset_score(self, C, top):
        C.delete(self.quit_button_window)
        C.delete(self.replay_button_window)
        C.delete(self.win)
        C.delete(self.lose)
        self.leftscore = 0
        self.rightscore = 0
        self.change_score(C)
        self.reset_ball(C)
        self.move_ball(C)       

    def move_up(self, Canvas):
        if Canvas.coords(self.paddle_2)[1] > 0: 
            Canvas.move(self.paddle_2, 0, -5)
    
    def move_down(self, Canvas):        
        if Canvas.coords(self.paddle_2)[3] < 350: 
            Canvas.move(self.paddle_2, 0, 5)

    def move_w(self, Canvas):
        if Canvas.coords(self.paddle_1)[1] > 0:        
            Canvas.move(self.paddle_1, 0, -5)
    
    def move_s(self, Canvas):
        if Canvas.coords(self.paddle_1)[3] < 350:
            Canvas.move(self.paddle_1, 0, 5)

    def move_paddles(self, Canvas):
        if 'w' in self.pressedKeys:
            self.move_w(Canvas)
        if 's' in self.pressedKeys:
            self.move_s(Canvas)
        if 'Up' in self.pressedKeys:
            self.move_up(Canvas)
        if 'Down' in self.pressedKeys:
            self.move_down(Canvas)
        Canvas.after(10, self.move_paddles, (Canvas))    

    def onKeyPress(self, event):
        self.pressedKeys.add(event.keysym)

    def onKeyRelease(self, event):
        self.pressedKeys.remove(event.keysym)

    def handle_keyboard(self, Canvas):
        Canvas.bind("<Key>", self.onKeyPress)
        Canvas.bind("<KeyRelease>", self.onKeyRelease)
        self.move_paddles(Canvas)

    def score_board(self, Canvas, xcoord, ycoord, size, text):
        return Canvas.create_text(xcoord, ycoord, fill="white", font=("TkDefaultFont", size), text=text)

    def paddle_and_net(self, Canvas, x1, y1, x2, y2, fill):
        return Canvas.create_rectangle(x1, y1, x2, y2, fill=fill)

    def ball(self,Canvas):
        return Canvas.create_oval(90, 90, 110, 110, width="0", fill="green")

    def change_score(self, Canvas):
            Canvas.itemconfig(self.score, text=self.leftscore)
            Canvas.itemconfig(self.score2, text=self.rightscore)
            if self.leftscore == 11:
                self.left_win(Canvas)
            elif self.rightscore == 11:
                self.right_win(Canvas)

    def right_win(self, Canvas):
        self.lose = self.score_board(Canvas, 150, 150, 50,"YOU LOSE")
        self.win = self.score_board(Canvas, 450, 150, 50,"YOU WIN")
        self.quit_button_window = Canvas.create_window(350, 235, window=self.quit_button)
        self.replay_button_window = Canvas.create_window(250, 235, window=self.replay_button)
       

    def left_win(self, Canvas):
        self.lose = self.score_board(Canvas, 450, 150, 50,"YOU LOSE")
        self.win = self.score_board(Canvas, 150, 150, 50,"YOU WIN")
        self.quit_button_window = Canvas.create_window(350, 235, window=self.quit_button)
        self.replay_button_window = Canvas.create_window(250, 235, window=self.replay_button)

    def move_ball(self, Canvas):
        if (self.check_collision(Canvas, Canvas.coords(self.ball)) == False):
            self.x = -self.x
        elif (self.check_collision(Canvas, Canvas.coords(self.ball)) == True):
            self.y = -self.y
        Canvas.move(self.ball, self.x, self.y)
        if (self.rightscore < 11) and (self.leftscore < 11):
            Canvas.after(10, self.move_ball, (Canvas))

    def reset_ball(self, Canvas):
        Canvas.coords(self.ball, 290, 165, 310, 185)
        time.sleep(0.5)

    def check_collision(self, Canvas, position):
        radius = 10
        if (position[0] == Canvas.coords(self.paddle_1)[2]) and (position[1] > Canvas.coords(self.paddle_1)[1]) and (position[1] < Canvas.coords(self.paddle_1)[3]):
            return False
        elif (position[2] == Canvas.coords(self.paddle_2)[0]) and (position[1] > Canvas.coords(self.paddle_2)[1]) and (position[1] < Canvas.coords(self.paddle_2)[3]):
            return False
        elif (position[0] < 0 + radius):
            self.rightscore += 1
            self.change_score(Canvas)
            self.reset_ball(Canvas)
            return False            
        elif (position[1] < 0 + radius):
            return True
        elif (position[2] > 600):
            self.leftscore += 1
            self.change_score(Canvas)
            self.reset_ball(Canvas)
            return False            
        elif (position[3] > 350):
            return True
        else:
            return

pp = set_up()
pp.create_pong()