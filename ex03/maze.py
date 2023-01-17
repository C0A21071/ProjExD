import tkinter as tk
import maze_maker as mm
import tkinter.messagebox as tkm
import time

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
    global need_time,finish_time
    if (mx == yokohaba-2) and (my == tatehaba-2):
        finish_time = time.perf_counter()
        need_time = finish_time - start_time
        need_time = '{:.2f}'.format(need_time)
        timeans = "{0}".format(need_time) + "秒"
        tkm.showinfo("ゴール！！！",f"最終入力まで{timeans}。\n入力回数は{count}回でした。")
        if jid is not None: #ゴール時に連続してポップアップが出るのを止める
            root.after_cancel(jid)
            jid = None


def main_proc():
    global cx, cy, mx, my, jid, start_time, finish_time ,need_time, first_input,last_input,count
    #wasdキーでの移動を実装
    if key == "Up" or key == "w": my -= 1
    if key == "Down" or key == "s": my += 1
    if key == "Left" or key == "a": mx -= 1
    if key == "Right" or key == "d": mx += 1
    if (maze_lst[mx][my] == 1): #移動先が壁なら以下のif分で逆方向に戻す
        if key == "Up" or key == "w": my += 1
        if key == "Down" or key == "s": my -= 1
        if key == "Left" or key == "a": mx += 1
        if key == "Right" or key == "d": mx -= 1

    if key in ["Up","Down","left","Right","w","a","s","d"]:
        count += 1
        if first_input == 0:
            start_time = time.perf_counter()
            first_input = 1
        
        
    
    cx, cy = (mx*100)+50, (my*100)+50
    canvas.coords("kokaton", cx, cy)
    goal_check()
    jid = root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()
    #jobid
    jid = None

    #経過時間を取得する為の変数
    start_time = 0
    finish_time = 0
    need_time = 0

    #初回入力と最終入力のフラグを取る
    first_input = 0
    last_input = 0

    #入力数のカウントをする
    count = 0

    #迷路のサイズをこちらで指定する。横幅はyokohaba、縦幅はtatehaba
    yokohaba = 15
    tatehaba = 9
    #maze_lst = mm.make_maze(15, 9)
    maze_lst = mm.make_maze(yokohaba,tatehaba)
    #print(maze_lst)
    mm.show_maze(canvas, maze_lst) #迷路生成のモジュールを呼び出す

    mx,my = 1,1 #初期位置の指定
    cx, cy = (mx*100)+50, (my*100)+50 #初期位置から座標を割り出す

    #鳥画像の場所
    tori = tk.PhotoImage(file=r"C:\Users\admin\Documents\東京工科大学\講義資料\二年次\後期\プロジェクト演習[CD]\テーマD\ProjExD2022\fig\8.png")
    
    make_start_goal() #スタートとゴールに着色する関数
    
    canvas.create_image(cx, cy, image=tori, tag="kokaton") #鳥を表示する
    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc() #ゲームの挙動に関わる関数を呼ぶ
    
    
    root.mainloop()