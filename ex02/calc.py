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

#計算後に計算式を表示する欄
keisansiki = tk.Entry(root,justify="right",font=("",10))
keisansiki.grid(row = 0, column = 0, columnspan=4,sticky = tk.W+tk.E)
#テキスト入力欄
entry=tk.Entry(root,justify="right",width=10,font=("",40))
entry.grid(row = 1, column = 0 , columnspan=4,sticky=tk.W+tk.E)

#ボタン情報の一括管理
bt = ["7","8","9","+",
      "4","5","6","-",
      "1","2","3","*",
      "0","C","=","/"]

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