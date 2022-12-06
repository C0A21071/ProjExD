import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm


def key_down(event):
    global key 
    key = event.keysym


def key_up(event):
    global key 
    key = ""


def main_proc():
    global cx,cy,mx,my
    if key =="Up":#上を押したとき
        my-=1
    elif key == "Down":#下を押したとき
        my+=1
    elif key == "Left":#左を押したとき
        mx -=1
    elif key == "Right":#右を押したとき
        mx+=1

    if maze_lst[mx][my] == 1:#移動先が壁の場合
        if key =="Up":#上を押したとき
            my+=1
        elif key == "Down":#下を押したとき
            my-=1
        elif key == "Left":#左を押したとき
            mx +=1
        elif key == "Right":#右を押したとき
            mx-=1
    cx,cy = mx*100+50,my*100+50
    canvas.coords("tori",cx,cy)
    root.after(100,main_proc)


if __name__ =="__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root,width=1500,height=900,bg ="black" )
    canvas.pack()

    maze_lst = mm.make_maze(15,9)
    mm.show_maze(canvas,maze_lst)

    tori = tk.PhotoImage(file="fig/1.png")

    mx,my = 1,1
    cx, cy = mx*100+50,my*100+50
    canvas.create_image(cx, cy, image=tori,tag = "tori")
    
    key = ""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)

    main_proc()


    root.mainloop()