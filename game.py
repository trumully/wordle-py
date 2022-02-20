import tkinter as tk
from typing import Optional

class Game:
    def __init__(self, title: str, 
                 width: int, height: int, timestep: int = 50):
        self.root = tk.Tk()
        self.root.title(title)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.end)
        self.timestep = timestep
        self.timer_id: Optional[str] = None

        self.frame = tk.Frame(self.root)
        self.frame.grid(row=0, column=0)

        self.canvas = tk.Canvas(master=self.frame,
                                width=width,
                                height=height,
                                bg="white"
                                )
        
        self.canvas.grid(row=0, column=0, rowspan=2, columnspan=1)

    def run(self):
        self.running = True
        self._run()
        self.root.mainloop()

    def _run(self):
        if self.running:
            self.timer_id = self.root.after(self.timestep, self._run)

    def end(self):
        self.running = False
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)
        self.root.destroy()
