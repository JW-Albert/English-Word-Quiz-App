import time
import random
import csv
score = 0 
def word_file1():
    word = []
    with open("level 1-3.csv",mode='r',encoding="utf-8") as csvfile1:
        content = csv.reader(csvfile1)
        for i in content:
            word.append(tuple(i))
    return word

def examination1():
    global m
    word = word_file1()
    score = 0
    
    question = 100#題數
    for (english_word, chinese_word) in random.sample(word, question):
        print('\n')
        answer = input('{} -->'.format(chinese_word))
        if answer == english_word:
            print('Its correct.')
            score += 1
        else:
            print("wrong")
    print()
    print("score =", score)
    print()
    time.sleep(1)


def word_file2():
    word = []
    with open("level 4.csv",mode='r',encoding="utf-8") as csvfile2:
        content = csv.reader(csvfile2)
        for i in content:
            word.append(tuple(i))
    return word

def examination2():
    global m
    word = word_file2()
    score = 0
    question = 100#題數
    for (english_word, chinese_word) in random.sample(word, question):
        print('\n')
        answer = input('{} -->'.format(chinese_word))
        if answer == english_word:
            print('Its correct.')
            score += 1
        else:
            print("wrong")

    print()
    print("score =", score)
    print()
    time.sleep(1)
    
    
def word_file3():
    word = []
    with open("level 5.csv",mode='r',encoding="utf-8") as csvfile3:
        content = csv.reader(csvfile3)
        for i in content:
            word.append(tuple(i))
    return word

def examination3():
    global m
    word = word_file3()
    score = 0
    question = 100#題數
    for (english_word, chinese_word) in random.sample(word, question):
        print('\n')
        
        answer = input('{} -->'.format(chinese_word))
        if answer == english_word:
            print('Its correct.')
            score += 1
        else:
            print("wrong")
    print()
    print("score =", score)
    print()
    time.sleep(1)
    

def word_file4():
    word = []
    with open("level 6.csv",mode='r',encoding="utf-8") as csvfile4:
        content = csv.reader(csvfile4)
        for i in content:
            word.append(tuple(i))
    return word

def examination4():
    global m
    word = word_file4()
    score = 0
    question = 100#題數
    for (english_word, chinese_word) in random.sample(word, question):
        print('\n')  
        answer = input('{} -->'.format(chinese_word))
        if answer == english_word:
            print('Its correct.')
            score += 1
        else:
            print("wrong")
    print()
    print("score =", score)
    print()
    time.sleep(1)
    
    
def word_file5():
    word = []
    with open("level 4~6.csv",mode='r',encoding="utf-8") as csvfile5:
        content = csv.reader(csvfile5)
        for i in content:
            word.append(tuple(i))
    return word

def examination5():
    global m
    word = word_file5()
    score = 0
    question = 100#題數
    for (english_word, chinese_word) in random.sample(word, question):
        print('\n')
        answer = input('{} -->'.format(chinese_word))
        if answer == english_word:
            print('Its correct.')
            score += 1
        else:
            print("wrong")
    
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
                examination1()
        elif n == '2':
            print("-----系統提示-----")
            print("測驗即將開始")
            time.sleep(1)
            if __name__ == '__main__':
                examination2()
        elif n == '3':
            print("-----系統提示-----")
            print("測驗即將開始")
            time.sleep(1)
            if __name__ == '__main__':
                examination3()
        elif n == '4':
            print("-----系統提示-----")
            print("測驗即將開始")
            time.sleep(1)
            if __name__ == '__main__':
                examination4()
        elif n == '5':
            print("-----系統提示-----")
            print("測驗即將開始")
            time.sleep(1)
            if __name__ == '__main__':
                examination5()
        else:
            print("Error")
