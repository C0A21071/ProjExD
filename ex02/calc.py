import tkinter as tk
import tkinter.messagebox as tkm


#練習3
def button_click(event):
    btn = event.widget
    num = btn["text"]
    if num == "=":
        siki = entry.get()#数式の文字列
        res = eval(siki)#数式文字列の評価
        entry.delete(0,tk.END)#表示文字列の削除
        entry.insert(tk.END,res)#結果の挿入
    elif num == "C":
        entry.delete(0,tk.END)


    else:#=以外のボタン

    #tkm.showinfo("",f"{num}ボタンがクリックされました")
    #練習6
        entry.insert(tk.END, num)


#練習1
root = tk.Tk()
root.geometry("500x600")


#練習2
r = 3
c = 2
for num in range(9,-1,-1):
    button = tk.Button(root, text = f"{num}",width = 4,height = 2,font=("",30))
    button.grid(row = r,column=c)
    button.bind("<1>",button_click)
    c-=1
    if c == -1:
        r += 1
        c = 2
    #elif num == 0:
     #   c = 0
      #  r = 2
    if num == 1:
        c = 0

entry = tk.Entry(root,justify = "right", width = 10,font = ("",40 ))
entry.grid(row=0,column=0,columnspan = 3)

#練習5
operators = ["C","+","*","="]
for ope in operators:
    button = tk.Button(root, text = f"{ope}",width = 4,height = 2,font=("",30))
    c = 3
    r-=1
    button.grid(row = r,column=c)
    button.bind("<1>",button_click)
    


root.mainloop()