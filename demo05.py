#文件的读写

#写日记
import time
# a：追加
# w：写入
now = time.strftime("%y-%m-%d %H:%M:%S")
text = input("请输入今天的心情：")
with open("日记.txt","a",encoding="utf8") as f:
    f.write(now+"\n")     
    f.write(text+"\n")       #默认为GDK编码
    f.write("---------------\n") 

# print("hhhhhh\thhh")
# print("hhhhhh\nhhh")

#读日记
with open("日记.txt","r",encoding="utf8") as f:
    text = f.readlines()
for i in text:
    print(i)
