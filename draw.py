from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, canvas, color="black"):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=color)


class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, bg="white", width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=True)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.canvas.update()
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        self.root.mainloop()

    def close(self):
        self.running = False
        self.root.destroy()

    def draw_line(self, start, end, color="black"):
        line = Line(start, end)
        line.draw(self.canvas, color)


class Cell:
    def __init__(self, win=None):
        self.win = win
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self._visited = False

    def draw(self, x1, y1, x2, y2):
        if self.win is None:
            return   # Lets siply return for now
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

        if self.has_left_wall:
            self.win.draw_line(Point(x1, y1), Point(x1, y2))
        else :
            self.win.draw_line(Point(x1, y1), Point(x1, y2), "white")
        if self.has_top_wall:
            self.win.draw_line(Point(x1, y1), Point(x2, y1))
        else:
            self.win.draw_line(Point(x1, y1), Point(x2, y1), "white")
        if self.has_right_wall:
            self.win.draw_line(Point(x2, y1), Point(x2, y2))
        else:
            self.win.draw_line(Point(x2, y1), Point(x2, y2), "white")
        if self.has_bottom_wall:
            self.win.draw_line(Point(x1, y2), Point(x2, y2))
        else:
            self.win.draw_line(Point(x1, y2), Point(x2, y2), "white") 

    def draw_move(self, to_cell, undo=False):
        x1 = (self.x1 + self.x2) // 2
        y1 = (self.y1 + self.y2) // 2
        x2 = (to_cell.x1 + to_cell.x2) // 2
        y2 = (to_cell.y1 + to_cell.y2) // 2
        color = "gray" if undo else "red"
        self.win.draw_line(Point(x1, y1), Point(x2, y2), color)
