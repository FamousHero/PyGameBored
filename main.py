import tkinter as tk
import math

class Display(tk.Canvas):
    def __init__(self, parent, width, height, **kwargs):
        super().__init__(parent, width=width, height=height, **kwargs) # inherit base class & its methods
        self.grid(column=0, row=0)
        self.line = self.create_line(0,500, 1000,500, width=50)
        self.width = width
        self.height = height
        self.angle = 1
        self.focus_set()
    
    def move(self, event,offset_x, offset_y):
        print("pressed sometihng: " + event.char)
        x1,y1,x2,y2 = self.coords(self.line)
        self.coords(self.line, x1+offset_x,y1+offset_y,x2+offset_x,y2+offset_y)
        self.update()

    def rotate(self, objectId, angle_deg):
        x1, y1, x2, y2 = self.coords(self.line)
        angle_rad = math.radians(angle_deg)
        center_x, center_y = self.width/2, self.height/2
        x1, y1, x2, y2 = x1-center_x, y1-center_y, x2-center_x, y2-center_y
        new_x1 = x1*math.cos(angle_rad) - y1*math.sin(angle_rad)
        new_y1 = x1*math.sin(angle_rad) + y1*math.cos(angle_rad)
        new_x2 = x2*math.cos(angle_rad) - y2*math.sin(angle_rad) 
        new_y2 = x2*math.sin(angle_rad) + y2*math.cos(angle_rad)
        new_x1, new_x2 = new_x1+center_x, new_x2+center_x
        new_y1, new_y2 = new_y1+center_y, new_y2+center_y
        self.coords(self.line, new_x1, new_y1, new_x2, new_y2)
        self.update()
        if self.angle < 360:
            self.angle += 1
            self.after(20, self.rotate, self.line, 1)
    



if __name__ == "__main__":
    window = tk.Tk()
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0,weight=1)
    canvas = Display(window, width=1000, height=1000, background='gray75')
    canvas.grid(column=0, row=0)
    window.after(1000, canvas.rotate, canvas.line, 1)
    # Rotating around center of screen, not line
    # moving during rotation will affect final position
    canvas.bind("d", lambda x: canvas.move(x,3,0))
    canvas.bind("w", lambda x: canvas.move(x,0,-3))
    canvas.bind("a", lambda x: canvas.move(x,-3,0))
    canvas.bind("s", lambda x: canvas.move(x,0,3))

    window.mainloop()