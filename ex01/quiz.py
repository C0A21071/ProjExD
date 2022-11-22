import random

def main():
    shutudai()
    kaitou()

def shutudai():
    global mondai,seikai,mondai1

    mondai = ["サザエの旦那の名前は？","カツオの妹の名前は？","タラオはカツオから見てどんな関係？"]
    seikai = [["マスオ","ますお"],["ワカメ","わかめ"],["甥","おい"]]
    mondai1 = random.choice(mondai)
    print("問題:"+mondai1)

def kaitou():
    kaitou1 = input("答えてください:")
    if mondai1 == mondai[0]:
        if kaitou1 == seikai[0][0:1]:
            print("正解!!!")
        else:
            print("出直してこい")
    elif mondai1 == mondai[1]:
        if kaitou1 == seikai[1][0:1]:
            print("正解!!!")
        else:
            print("出直してこい")
    elif mondai1 == mondai[2]:
        if kaitou1 == seikai[2][0:1]:
            print("正解!!!")
        else:
            print("出直してこい")
    else:
        print("出直してこい")

if __name__ == "___main__":
    qa_lst = [
        {"q":"サザエの旦那の名前は？","a":["ますお","マスオ"]}
    ]