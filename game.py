import tkinter as tk
from typing import Optional, Protocol


class GameObject(Protocol):
    def update(self):
        """Update the game object."""

    def paint(self, canvas: tk.Canvas):
        """Paints the game object."""


class Game:
    """Game engine base."""
    def __init__(self, title: str, 
                 width: int, height: int, timestep: int = 50):
        """Constructor for the game engine."""
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
                                bg="white",
                                highlightthickness=0
                                )
        
        self.canvas.grid(row=0, column=0, rowspan=2, columnspan=1)

        self.objects: list[GameObject] = []

    def add_object(self, object: GameObject):
        """Add a game object."""
        self.objects.append(object)
    
    def remove_object(self, object: GameObject):
        """Remove a game object."""
        self.objects.remove(object)

    def run(self):
        """Start the game."""
        self.running = True
        self._run()
        self.root.mainloop()

    def _run(self):
        """Run the game."""
        self.update()
        self.paint()

        if self.running:
            self.timer_id = self.root.after(self.timestep, self._run)

    def end(self):
        """End the game."""
        self.running = False
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)
        self.root.destroy()

    def update(self):
        """Update the game."""
        for obj in self.objects:
            obj.update()

    def paint(self):
        """Paints the game."""
        self.canvas.delete(tk.ALL)  # clear the screen
        for obj in self.objects:
            obj.paint(self.canvas)
