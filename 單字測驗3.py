import time
import random
import csv
score = 0
def word_file(name):
    word = []
    with open(name,mode='r',encoding="utf-8") as csvfile1:
        content = csv.reader(csvfile1)
        for i in content:
            word.append(tuple(i))
    return word

def examination(name):
    global m
    word = word_file(name)
    score = 0
    a = 1
    question = 100#題數
    for (english_word, chinese_word) in random.sample(word, question):
        print('\n')
        print(a,'::')
        a += 1
        answer = input('{} -->'.format(chinese_word))
        if answer == english_word:
            print('---Its correct.')
            score += 1
        else:
            print("---wrong")
    print()
    print("score =", score)
    print()
    time.sleep(1)
      



 
while True:
    print("----------------------------單字測驗----------------------------")
    print("單字等級選單:")
    print("(1)level 1~3  (2)level 4  (3)level 5  (4)level 6  (5)level 4~6 ")
    n = input("選擇等級:")
    time.sleep(0.5)
    enter = input("按下enter鍵開始")
    print('\n')
  
    if enter == '':
        if n == '1':
            print("-----系統提示-----")
            print("測驗即將開始")
            time.sleep(1)
            if __name__ == '__main__':
                examination("level 1-3.csv")
        elif n == '2':
            print("-----系統提示-----")
            print("測驗即將開始")
            time.sleep(1)
            if __name__ == '__main__':
                examination("level 4.csv")
        elif n == '3':
            print("-----系統提示-----")
            print("測驗即將開始")
            time.sleep(1)
            if __name__ == '__main__':
                examination("level 5.csv")
        elif n == '4':
            print("-----系統提示-----")
            print("測驗即將開始")
            time.sleep(1)
            if __name__ == '__main__':
                examination("level 6.csv")
        elif n == '5':
            print("-----系統提示-----")
            print("測驗即將開始")
            time.sleep(1)
            if __name__ == '__main__':
                examination("level 4~6.csv")
        else:
            print("--------------Input Error--------------")
    print("本程式由王建葦指導")
    print("由張偉德開發")