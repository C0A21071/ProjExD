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
    if txt == "C":
        entry.delete(0,tk.END)
    else:
        entry.insert(tk.END,txt)
    

#ウィンドウ設定
root = tk.Tk()
root.title("電卓")
root.geometry("400x500")

#計算後に計算式を表示する欄
keisansiki = tk.Entry(root,justify="right",font=("",10))
keisansiki.grid(row = 0, column = 0, columnspan=4,sticky = tk.W+tk.E)
#テキスト入力欄
entry=tk.Entry(root,justify="right",width=10,font=("",40))
entry.grid(row = 1, column = 0 , columnspan=4,sticky=tk.W+tk.E)

root.grid_rowconfigure(1,weight=1)

#ボタン情報の一括管理
bt = ["7","8","9","+",
      "4","5","6","-",
      "1","2","3","*",
      "0","C","="]

r,c = 2,0
for key in bt:
    button = tk.Button(root,text=f"{key}",font=("",30),width=4,height=2)
    button.bind("<1>",button_click)
    button.grid(row=r,column=c)
    c += 1
    if (c%4 == 0):
        r += 1
        c = 0

"""
#0-9のボタンと、右端に四則演算のボタンを表示
r,c = 2,0
bt = ["+","-","x","÷"]
for i in range(9,-5,-1):
    if(c%4 == 3):#cのカウントが右端に来たとき
        button = tk.Button(root,text=f"{ope[j]}",font=("",30),width=4,height=2)
        j += 1
    else:
        button = tk.Button(root,text=f"{i}",font=("",30),width=4,height=2)

    button.bind("<1>",button_click)
    button.grid(row=r,column=c)
    c += 1
    if (c%4 == 0):
        r += 1
        c = 0
        i += 2

#+と=のボタン配置
operators = ["+","="]
for ope in operators:
    button = tk.Button(root,text=f"{ope}",font=("",30),width=4,height=2)
    button.bind("<1>",button_click)
    button.grid(row=r,column=c)
    c += 1
    if (c%4 == 0):
        r += 1
        c = 0

"""

#実行
root.mainloop()