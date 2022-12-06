import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm


def key_down(event):
    global key 
    key = event.keysym


def key_up(event):
    global key 
    key = ""

def button_click(event):#進むボタンを押した回数を表示する
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"進んだ回数は{count}回です")


def main_proc():
    global cx,cy,mx,my,count,tori
    if key =="Up" and maze_lst[mx][my-1] == 0:#上を押したとき
        tori = tk.PhotoImage(file="fig/6.png")
        my-=1
        count +=1
    elif key == "Down" and maze_lst[mx][my+1] == 0:#下を押したとき
        tori = tk.PhotoImage(file="fig/4.png")
        my+=1
        count +=1
    elif key == "Left" and maze_lst[mx-1][my] == 0:#左を押したとき
        tori = tk.PhotoImage(file="fig/5.png")
        mx -=1
        count +=1
    elif key == "Right" and maze_lst[mx+1][my] == 0:#右を押したとき
        tori = tk.PhotoImage(file="fig/2.png")
        mx+=1
        count +=1

    cx,cy = mx*100+50,my*100+50
    canvas.create_image(cx,cy,image=tori,tag ="tori")
    canvas.coords("tori",cx,cy)
    if cx == 13*100+50 and cy == 7*100+50:#右下のマスについたら終了する
        return

    root.after(100,main_proc)
    print(count)



if __name__ =="__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    button = tk.Button(root,text = "操作した回数",width = 20,height = 5,bg = "yellow",fg = "red")
    button.bind("<1>",button_click)
    button.pack()

    canvas = tk.Canvas(root,width=1500,height=900,bg ="black" )
    canvas.pack()
    maze_lst = mm.make_maze(15,9)
    mm.show_maze(canvas,maze_lst)
    
    mx,my = 1,1
    cx, cy = mx*100+50,my*100+50
    tori = tk.PhotoImage(file="fig/1.png")
    canvas.create_image(cx, cy, image=tori,tag = "tori")
    
    goal = tk.PhotoImage(file = "fig/9.png")
    canvas.create_image(13*100+50,7*100+50,image=goal,tag ="goal")
    key = ""
    count = 0

    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()

    
    root.mainloop()