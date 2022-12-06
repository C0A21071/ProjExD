import random

taisyou = 5 #対象文字数
kessonn = 2 #欠損文字数
kurikaesi = 3 #最大繰り返し数

taisyoumoji = []
kessonnmoji = []

#文字の正誤判定と最終的な正誤の発表を行う
def mojihantei():
    for i in range(kessonn):
        ans = input(f"{i+1}つ目の文字を入力してください：")
        print(kessonnmoji)
        if(ans in kessonnmoji):
            continue
        else:
            print("不正解です。またチャレンジしてください")
            return 0
    print("正解です。")
    return 1

#初期ステータスの生成をする関数
def mk_status():
    #対象文字を必要分だけリストに格納
    for i in range(taisyou):
        a = random.randint(65,90)
        taisyoumoji.append(chr(a))
    #対象文字のリストから必要分だけ欠損文字リストに格納
    kessonnmoji = random.sample(taisyoumoji,k=kessonn)

    #対象文字のリストから欠損文字を抜いたものを表示文字リストに格納
    hyoujimoji = kessonnmoji + taisyoumoji
    print(hyoujimoji)
    print(set(hyoujimoji))
    print("対象文字")
    print(taisyoumoji)
    print("欠損文字")
    print(kessonnmoji)  
    print("表示文字")
    print(hyoujimoji)

def quest_num():
    needinput = int(input("欠損文字はいくつあるでしょうか？:"))
    if (needinput == kessonn):
        print("正解です。具体的に欠損文字を一文字ずつ入力せよ。")
        return 1
    else:
        print("不正解です。またチャレンジしてください。")
        return 0

if __name__ == "__main__":
    i = 0
    while i < kurikaesi:
        mk_status()
        if (quest_num() == 1):
            if (mojihantei()==0):
                i += 1
            else:
                i += kurikaesi
        else:
            i += 1
            print(f"残り{kurikaesi-i}回")
            print("-"*20)