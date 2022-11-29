import tkinter as tk
import tkinter.messagebox as tkm

#関数定義

#ボタンを押した際の反応
def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"{txt}のボタンがクリックされました")

#ウィンドウ設定
root = tk.Tk()
root.title("電卓")
root.geometry("300x500")

#テキスト入力欄
entry=tk.Entry(root,justify="right",width=10,font=("",40))
entry.grid(row = 0, column = 0 ,columnspan=3)

#0-9のボタン表示
r,c = 1,0
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
    button.grid(row=r,column=c)
    c += 1
    if (c%3 == 0):
        r += 1
        c = 0
#実行
root.mainloop()