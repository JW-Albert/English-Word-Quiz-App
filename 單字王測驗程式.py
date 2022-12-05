#cooding = UTF-8
import time
import random
import csv
import email.message
import smtplib
import os
os.system("chcp 65001")

score = 0
number = 0
m = []
level_choose = 0
name = ""
time_start = ""
time_end = ""
time_system_start = ""
time_system_end = ""
time_system_total = ""
send_mail_set = ""
error_m = ""
true_m = ""
system_endding = None

class send_mail():
    def auto():
        send_mail.set()
        send_mail.teacher()
        send_mail.student()
        send_mail.admain()

    def set():
        global send_mail_set
        global m
        global error_m
        global true_m
        global number
        global time_system_start
        global time_system_end
        global time_system_total
        global level_choose
        number = str(number)
        number += "@goog.ptsh.ntct.edu.tw"
        error_m = int(len(m) / 2)
        true_m = 100 - error_m
        error_m = str(error_m)
        true_m = str(true_m)
        time_system_total = time_system_end - time_system_start
        time_system_total = "{:.2f}".format(time_system_total)
        time_system_total = str(time_system_total)
        for k in range(len(m)):
            set = ""
            if(k == 0 or k %2 == 0):
                send_mail_set += m[k]
                send_mail_set += "："
            else:
                set = m[k] + "\n"
                send_mail_set += set
        if(level_choose == "1"):
            level_choose = "1~3"

        elif(level_choose == "5"):
            level_choose = "4~6"

        else:
            pass

    def teacher():
        global time_start
        global time_end
        global time_system_total
        global name
        global number
        global score
        global error_m
        global true_m
        global level_choose
        score = str(score)

        msg = email.message.EmailMessage()
        msg["From"] = "boring.co.ltd@gmail.com"
        msg["To"] = "910041@goog.ptsh.ntct.edu.tw"
        msg["Subject"] = "單字王測驗成績單(教師端)　姓名：" + name + "　等級：" + level_choose

        msg.set_content("姓名：" + name + "　成績：" + score + "　等級：" + level_choose + "\n" 
        + "學生帳號：" + number + "\n"
        + "正確題數：" + true_m + "\n"
        + "錯誤題數：" + error_m + "\n"
        + "作答開始時間：" + time_start + "\n" 
        + "作答結束時間：" + time_end + "\n"
        + "總作答時間：" + time_system_total + "秒")

        server = smtplib.SMTP_SSL("smtp.gmail.com" ,465)
        server.login("boring.co.ltd@gmail.com" ,"faeyuyclikhwinlt")
        server.send_message(msg)
        server.close()


    def student():
        global time_start
        global time_end
        global time_system_total
        global name
        global score
        global number
        global send_mail_set
        global error_m
        global true_m
        global level_choose
        score = str(score)

        msg = email.message.EmailMessage()
        msg["From"] = "boring.co.ltd@gmail.com"
        msg["To"] = number
        msg["Subject"] = "單字王測驗成績單(學生端)　姓名：" + name + "　等級：" + level_choose

        msg.set_content("姓名：" + name + "　成績：" + score + "　等級：" + level_choose + "\n" 
        + "學生帳號：" + number + "\n"
        + "作答開始時間：" + time_start + "\n" 
        + "作答結束時間：" + time_end + "\n"
        + "正確題數：" + true_m + "\n"
        + "錯誤題數：" + error_m + "\n"
        + "總作答時間：" + time_system_total + "秒" + "\n"
        + "錯誤內容：" + "\n"
        + send_mail_set)

        server = smtplib.SMTP_SSL("smtp.gmail.com" ,465)
        server.login("boring.co.ltd@gmail.com" ,"faeyuyclikhwinlt")
        server.send_message(msg)
        server.close()


    def admain():
        global time_start
        global time_end
        global time_system_total
        global name
        global score
        global number
        global send_mail_set
        global error_m
        global true_m
        global level_choose
        score = str(score)

        msg = email.message.EmailMessage()
        msg["From"] = "boring.co.ltd@gmail.com"
        msg["To"] = "910041@goog.ptsh.ntct.edu.tw"
        msg["Subject"] = "單字王測驗成績單(系統端)　姓名：" + name + "　等級：" + level_choose

        msg.set_content("姓名：" + name + "　成績：" + score + "　等級：" + level_choose + "\n" 
        + "學生帳號：" + number + "\n"
        + "作答開始時間：" + time_start + "\n" 
        + "作答結束時間：" + time_end + "\n"
        + "正確題數：" + true_m + "\n"
        + "錯誤題數：" + error_m + "\n"
        + "總作答時間：" + time_system_total + "秒" + "\n"
        + "錯誤內容：" + "\n"
        + send_mail_set)

        server = smtplib.SMTP_SSL("smtp.gmail.com" ,465)
        server.login("boring.co.ltd@gmail.com" ,"faeyuyclikhwinlt")
        server.send_message(msg)
        server.close()

def Settlement():
    
    print("正確答案：")
    global m
    y = 0
    for i in range(len(m)):
        y += 1
        if(y == 1):
            print(m[i],end=" : ")
            y = -1
        else:
            print(m[i])
    print()
    os.system("pause")

class MAIN():
    def word_file(name):
        word = []
        with open(name ,mode='r' ,encoding="utf-8") as csvfile1:
            content = csv.reader(csvfile1)
            for i in content:
                word.append(tuple(i))
        return word
    
    def examination(name):
        os.system("cls")
        global m
        global time_start
        global time_end
        global time_system_start
        global time_system_end
        global system_endding
        global score
        print("{:*^90}".format("系統提示"))
        print("{: ^90}".format("測驗即將開始"))
        time.sleep(1)
        time_start = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        time_system_start = time.time()

        word = MAIN.word_file(name)
        score = 0
        a = 1
        question = 100 #題數
        errors = 0
        for (english_word, chinese_word) in random.sample(word, question):
            try:
                print('\n')
                print(a,'::')
                a += 1
                answer = input('{} -->'.format(chinese_word))
                if answer == english_word:
                    print("---It's correct.")
                    score += 1

                else:
                    print("---wrong")
                    m.append(chinese_word)
                    m.append(english_word)
        
            except:
                if(KeyboardInterrupt):
                    system_endding = True
                    break

                errors += 1
                a -= 1
            
        if(errors != 0):
            for (english_word, chinese_word) in random.sample(word, errors):
                print(chinese_word)
                print('\n')
                print(a,'::')
                a += 1
                
                answer = input('{} -->'.format(chinese_word))

                if answer == english_word:
                    print('---Its correct.')
                    score += 1
                else:
                    print("---wrong")
                    m.append(chinese_word)
                    m.append(english_word)

        time_system_end = time.time()
        time_end = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        print()

        if(system_endding == True):
            return 0
        
        os.system("cls")
        print("成績寄送中")
        send_mail.auto()
        os.system("cls")
        print("score =", score)
        print("請確認成績")
        os.system("pause")
        os.system("cls") 
        print()
        Settlement()
         
        
print("{:-^90}".format("單字測驗"))
name = input("請輸入真實姓名： ")
number = input("請輸入真實學號： ")
time.sleep(0.5)
os.system("cls")

claer = None
while True:
    print("{:-^90}".format("身分驗證"))
    print("姓名：" + name)
    print("學號：" + number)
    print("若有錯誤請直接關閉程式並重新開起")
    os.system("pause")
    os.system("cls")
    
    print("{:-^94}".format(""))
    print("單字等級選單：")
    print("(1)level 1~3  (2)level 4  (3)level 5  (4)level 6  (5)level 4~6  (6)離開")
    level_choose = input("選擇等級：")

    if(level_choose == "6"):
        break

    os.system("cls")

    print("{:-^94}".format(""))
    print("{:^90}".format("按下 Ctrl+c 終止程式"))
    print("{:^90}".format("按下 Enter 鍵開始"))
    print("{:-^94}".format(""))
    start = input()
    print('\n')
    
    if start == '':
        if level_choose == '1':
            if __name__ == '__main__':
                MAIN.examination("level 1-3.csv")

        elif level_choose == '2':
            if __name__ == '__main__':
                MAIN.examination("level 4.csv")

        elif level_choose == '3':
            if __name__ == '__main__':
                MAIN.examination("level 5.csv")

        elif level_choose == '4':
            if __name__ == '__main__':
                MAIN.examination("level 6.csv")

        elif level_choose == '5':
            if __name__ == '__main__':
                MAIN.examination("level 4-6.csv")

        elif level_choose == '6':
            break

        else:
            print("{:-^90}".format("您輸入的選項錯誤"))
    os.system("cls")
    print("\n")