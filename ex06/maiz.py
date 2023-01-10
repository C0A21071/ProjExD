import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym

#キーを離しても押された状態を保つために、キーを話したときの関数を削除した
#def key_up(event):
 #   global key
  #  key = ""


def main_proc():
    global cx, cy, mx, my
    #wasdキーもしくわ矢印キーにより移動可能にしている
    if key == "Up" or key == "w": my -= 1
    if key == "Down" or key == "s": my += 1
    if key == "Left" or key == "a": mx -= 1
    if key == "Right" or key == "d": mx += 1
    if (maze_lst[mx][my] == 1): #壁に衝突時にif文によりすり抜けないようにする
        if key == "Up" or key == "w": my += 1
        if key == "Down" or key == "s": my -= 1
        if key == "Left" or key == "a": mx += 1
        if key == "Right" or key == "d": mx -= 1
       
    cx, cy = mx*40+20, my*40+20
    canvas.coords("kokaton", cx, cy)
    
    root.after(150, main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1200, height=1000, bg="black")
    canvas.pack()

    maze_lst = mm.make_maze(30, 18)
    # print(maze_lst)
    mm.show_maze(canvas, maze_lst)

    mx, my = 1, 16
    cx, cy = mx*30+30, my*30+30
    tori = tk.PhotoImage(file="fig/1.png")
    canvas.create_image(cx, cy, image=tori, tag="kokaton")

    #キーを離しても押された状態を保つようにしている
    root.bind("<KeyPress>", key_down)
    #root.bind("<KeyRelease>", key_up)
    main_proc()
    root.mainloop()