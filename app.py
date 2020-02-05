from PIL import Image, ImageTk
import tkinter as tk
import argparse
import datetime
import cv2
import os

class Application:
    def __init__(self, output_path = "./"):
        self.vs = cv2.VideoCapture(0)
        self.output_path = output_path 
        self.current_image = None 

        self.root = tk.Tk()  
        self.root.title("Sudoku_Vision")
        self.root.protocol('WM_DELETE_WINDOW', self.destructor)

        self.panel = tk.Label(self.root)  
        self.panel.pack(padx=10, pady=10)

        button1 = tk.Button(self.root, text="Capture!",bg="teal", command=self.take_snapshot)
        button1.pack(fill="both", expand=True, padx=10, pady=10)

        self.video_loop()

    def video_loop(self):
        ok, frame = self.vs.read() 
        if ok: 
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)  
            self.current_image = Image.fromarray(cv2image) 
            imgtk = ImageTk.PhotoImage(image=self.current_image)  
            self.panel.imgtk = imgtk  
            self.panel.config(image=imgtk)  
        self.root.after(30, self.video_loop)  

    def take_snapshot(self):
        ts = datetime.datetime.now() 
        filename = "test_images/{}.png".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))  
        p = os.path.join(self.output_path, filename) 
        self.current_image.save(p, "PNG")  
        print("[INFO] saved {}".format(filename))
        os.system('python3 main.py --filename {}'.format(filename))

    def destructor(self):
        print("[INFO] closing...")
        self.root.destroy()
        self.vs.release() 
        cv2.destroyAllWindows()  


print("[INFO] starting...")
app = Application()
app.root.mainloop()