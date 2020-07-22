#判断 
a = 1
b = 2
if a > b:
    print("a比b大")
else:
    print("b更大")

age = int(input("请输入你的年龄："))
if age > 60 and age <=70:
    print("退休")
elif age > 30:
    print("责任")
elif age > 20:
    print("未来")
else:
    print("读书")

a = 10
if type(a) is int:
    print("shuzi")
elif type(a) is str:
    print("zifuchuan")
else:
    print("qita")


#循环
a = 2
while a < 10:
    print("hhhh")
    a = a + 1

"""
假设有10个学生的成绩，需要录入系统中
十个人：张三、李四、王麻子、小红、小李、小王、小明、小周、小哈、小可乐
并且名字和成绩相对应
而且大于60的和小于60的分开放
"""
highchengji = {}   #定义空字典，存储大于60的成绩
lowchengji = {}    #定义空字典，存储小于60的成绩
studentlist = ["张三","李四","王麻子","小红","小李","小王","小明","小周","小哈","小可乐"]
a = 0     #变量，数组下标变化
while a < len(studentlist)-1:
    chengji = int(input("请输入"+studentlist[a]+"的成绩："))
    if chengji >= 60:
        highchengji[studentlist[a]] = chengji
    else:
        lowchengji[studentlist[a]] = chengji
    a = a + 1
print("大于60的：",highchengji)
print("小于60的：",lowchengji)

#for循环
highchengji = {}   #定义空字典，存储大于60的成绩
lowchengji = {}    #定义空字典，存储小于60的成绩
studentlist = ["张三","李四","王麻子","小红","小李","小王","小明","小周","小哈","小可乐"]
a = 0     #变量，数组下标变化
#while a < len(studentlist)-1:
for i in studentlist:
    chengji = int(input("请输入"+studentlist[a]+"的成绩："))
    if chengji >= 60:
        highchengji[studentlist[a]] = chengji
    else:
        lowchengji[studentlist[a]] = chengji
    #a = a + 1
print("大于60的：",highchengji)
print("小于60的：",lowchengji)

#九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"x",j,"=",i*j,end=" ")   #end 隔开
    print()    #换行

"""
通过print打印，模拟一个红绿灯功能，红灯30次，绿灯35次，黄灯3次，循环
"""
light = {"红灯":30,"绿灯":35,"黄灯":3}
while True:      #死循环
    for i in light:
        for j in range(light[i]):
            print(i,"倒计时还有：",light[i]-j,"秒")

"""
使用代码，实现一个注册功能。
用户输入账号密码，账号长度5-8，密码6-12位，账号小写开头。
存储到字典中，{username：password}
"""
username = input("请输入账号：")
password = input("请输入密码：")
if len(username) >= 5 and len(username) <= 8:
    if username[0] in "qwertyuiopasdfghjklzxcvbnm":
        if len(password) >= 6 and len(password) <= 12:
            print("注册成功",{username:password})
        else:
            print("密码6-12位")
    else:
        print("首字母必须小写开头")
else:
    print("账号不合格，5-8位")


#continue
for i in range(10):
    if i == 4:
        continue
    print(i)      #输出0,1,2,3,5,6,7,8,9

#break
for i in range(10):
    if i == 4:
        break
    print(i)      #输出0,1,2,3