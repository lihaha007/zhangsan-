"""
print("hello world!")   #字符串
print("哈哈"+"xixi")
print("haha"*10)
print(233)    #整数
print(2.33)   #小数
print(True)   #布尔值
print(())    #元组
print([])   #数组
print({})   #字典

锄禾日当午
汗滴禾下土
"""

a = input("请输入：")
print("input获取的内容：",a)


a = input("请输入：")
b = input("请输入：")
print("两段字符串的长度：",len(a)+len(b))


#  元组,下标从0开始编号
a = ()  #空元组
a = (1,2,3,"哈哈","哈哈","哈哈","哈哈","xixi",True)
print(a.index("哈哈"))   #就近原则
print(a)
print(a[3])
print(a.index("xixi"))
print(a.count("哈哈"))

#  二维元组
a = (1,2,3,"哈哈","哈哈","哈哈","哈哈","xixi",True)
print(a[0:4])   #左闭右开，输出：(1, 2, 3, '哈哈')
print(a[4:7])    #('哈哈', '哈哈', '哈哈')
print(a[7:])    #('xixi', True)
b = (a,"haha","xixi")
print(b[0])      #输出：(1, 2, 3, '哈哈', '哈哈', '哈哈', '哈哈', 'xixi', True)
print(b[0][4])   #输出：哈哈


#数组
a = [1,2,3,"哈哈","xixi",True]
print(a[4])
a.append("heihei")
a.insert(3,"yoyo")
a.pop(2)   #剪切/删除
b = a.pop(0)      #输出：1
c = a.pop(0)    #2
print(b+c)  #3
#a.clear()
a.extend()

# True = 1
# False = 0

"""
所有的方法都是小括号结尾。Input()、print()
元组数组字典的取值都是中括号。a[0]
"""

#字典
a = {"name":"zhangsan",0:"hh","age":25}
#取值
print(a["name"])
print(a.get("name"))
#新增
a["high"] = "183cm"
#修改
a["name"] = "lisi"
print(a)
a.update(name="xixi")

"""
获取用户的个人信息，并且存储到字典中
个人信息：name age sex
"""
name = input("请输入你的姓名：")
age = input("请输入你的年龄：")
sex = input("请输入你的性别：")
userinfo = {}
userinfo.update(name=name,sex=sex,age=age)
print(userinfo)