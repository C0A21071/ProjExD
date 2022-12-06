import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tkm


#関数定義
#ボタンを押した際の反応
def button_click(event):
    
    replace = str.maketrans({"÷":"/","x":"*"}) #変換用テーブルの作成
    btn = event.widget
    txt = btn["text"]
    var.set(entry.get())
    if txt == "=": #=を押したときは式を計算する。
        line = entry.get()
        for old,new in replace.items():
            line = line.translate(replace)
        ans = eval(line)
        entry.delete(0,tk.END)
        entry.insert(tk.END,ans)
        keisansiki.delete(0,tk.END) #=が溜まり続けるため、それを廃棄する処理
        keisansiki.insert(tk.END,line)
    elif txt == "C":
        entry.delete(0,tk.END)
        keisansiki.delete(0,tk.END)
    else:
        entry.insert(tk.END,txt)
    

#ウィンドウ設定
root = tk.Tk()
root.title("電卓")
root.geometry("400x500")

var = tk.StringVar() #stringvar変数の使用

"""
#計算後に計算式を表示する欄
keisansiki = ttk.Entry(root,justify="right",font=("",10))
keisansiki.grid(row = 0, column = 0, columnspan=4,sticky = tk.W+tk.E)
"""
keisansiki = tk.Label(root,anchor="e", font=("",10),textvariable=var)
keisansiki.grid(row = 0,column=0, columnspan=4,sticky = tk.W+tk.E)

#テキスト入力欄
entry=ttk.Entry(root,justify="right",width=10,font=("",40))
entry.grid(row = 1, column = 0 , columnspan=4,sticky=tk.W+tk.E)

#ボタン情報の一括管理
bt = ["7","8","9","+",
      "4","5","6","-",
      "1","2","3","x",
      "0","C","=","÷"]

#ボタンの表示
r,c = 2,0
for key in bt:
    button = tk.Button(root,text=f"{key}",width=4,height=2,font=("",30))
    button.bind("<1>",button_click)
    button.grid(row=r,column=c)
    c += 1
    if (c%4 == 0):
        r += 1
        c = 0

#実行
root.mainloop()