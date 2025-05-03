from draw import Window
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(20, 20, 10, 10, 50, 50, win, 10)
    maze._break_entrance_and_exit()
    #clmaze._break_walls_r(0, 0)
    win.wait_for_close()

if __name__ == "__main__":
    main()
