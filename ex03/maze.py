import tkinter as tk
import maze_maker as mm
import tkinter.messagebox as tkm

def key_down(event):
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""

#以下追加関数

def make_start_goal(): #スタートとゴールに色をつける
    #スタート位置を緑色にする
    canvas.create_rectangle(mx*100, my*100, mx*100+100, my*100+100, fill="green")
    #ゴール位置を赤色にする
    canvas.create_rectangle((yokohaba-2)*100, (tatehaba-2)*100, (yokohaba-2)*100+100, (tatehaba-2)*100+100, fill="red")

def goal_check(): #ゴールした際にポップアップを出す。
    if (mx == yokohaba-2) and (my == tatehaba-2):
        tkm.showinfo("ゴール！！！","ゴールしました")
        if jid is not None: #ゴール時に連続してポップアップが出るのを止める
            root.after_cancel(jid)
            jid = None



def main_proc():
    global cx, cy, mx, my, jid
    #wasdキーでの移動を実装
    if key == "Up" or key == "w": my -= 1
    if key == "Down" or key == "s": my += 1
    if key == "Left" or key == "a": mx -= 1
    if key == "Right" or key == "d": mx += 1
    if (maze_lst[mx][my] == 1): #移動先が壁なら以下のif分で逆方向に戻す
        if key == "Up": my += 1
        if key == "Down": my -= 1
        if key == "Left": mx += 1
        if key == "Right": mx -= 1
    cx, cy = (mx*100)+50, (my*100)+50
    canvas.coords("kokaton", cx, cy)
    goal_check()
    jid = root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    #迷路のサイズをこちらで指定する。横幅はyokohaba、縦幅はtatehaba
    yokohaba = 15
    tatehaba = 9

    #jobid
    jid = None
    #maze_lst = mm.make_maze(15, 9)
    maze_lst = mm.make_maze(yokohaba,tatehaba)


    #print(maze_lst)
    mm.show_maze(canvas, maze_lst)

    mx,my = 1,1
    cx, cy = (mx*100)+50, (my*100)+50
    tori = tk.PhotoImage(file=r"C:\Users\admin\Documents\東京工科大学\講義資料\二年次\後期\プロジェクト演習[CD]\テーマD\ProjExD2022\fig\8.png")
    
    make_start_goal() #スタートとゴールに着色する関数
    
    canvas.create_image(cx, cy, image=tori, tag="kokaton")
    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()
    
    root.mainloop()