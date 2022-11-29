import tkinter as tk
import tkinter.messagebox as tkm

#関数定義
#ボタンを押した際の反応
def button_click(event):
    btn = event.widget
    txt = btn["text"]

    if txt == "=": #=を押したときは式を計算する。
        line = entry.get()
        ans = eval(line)
        entry.delete(0,tk.END)
        entry.insert(tk.END,ans)
        keisansiki.insert(tk.END,line)
    else:
        entry.insert(tk.END,txt)
    

#ウィンドウ設定
root = tk.Tk()
root.title("電卓")
root.geometry("300x500")

#計算後に計算式を表示する欄
keisansiki = tk.Entry(root,justify="right",width=20,font=("",10))
keisansiki.grid(row = 0, column = 1, columnspan=3)
#テキスト入力欄
entry=tk.Entry(root,justify="right",width=10,font=("",40))
entry.grid(row = 1, column = 0 , columnspan=3)

#0-9のボタン表示
r,c = 2,0
for i in range(9,-1,-1):
    button = tk.Button(root,text=f"{i}",font=("",30),width=4,height=2)
    button.bind("<1>",button_click)
    button.grid(row=r,column=c)
    c += 1
    if (c%3 == 0):
        r += 1
        c = 0

#+と=のボタン配置
operators = ["+","="]
for ope in operators:
    button = tk.Button(root,text=f"{ope}",font=("",30),width=4,height=2)
    button.bind("<1>",button_click)
    button.grid(row=r,column=c)
    c += 1
    if (c%3 == 0):
        r += 1
        c = 0

#実行
root.mainloop()