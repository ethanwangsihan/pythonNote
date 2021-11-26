'''
print("hello world")

ord("a")#turn %s into ascii
chr("56")#turn ascii into %s

a = input('shit\'s \n name:')
print(a)

print(True and True)

print(True and False)
print(5>3 and 3>1)
print(5>3 and 3<1)
print(5>3 or 3<1)
print(not 3<1)

b=1
print(type(b))

t_007='T001'
print(type(t_007))

a='abc'
b=a
a='xyz'
print(b)#b=abc

print(10/3)#精确的除
print(10//3)#整除
print(10%3)#取余

print(len('屁'))

a=input('name:')
b=input('money:')
print('Hi, %s ,you have $%d.'%(a,int(b)))#格式化和数据类型转换



a=['付玺','王思翰','马晟云']

print(a);
print(type(a))
print('List的长度是：',len(a))
print(len(a))
print('List的第二个元素是',a[1])
print('List的倒数第二个元素是',a[-2])
a.append('张落辰')#把元素加到列表最后
print(a[3])
a.insert(3,'魏泽远')#把魏泽远插入到第4个位置
print(a)
a.pop(3)#第4个元素删除
print(a)
a[3]='安研菲'#替换第4个元素
print(a)
a.append('龙雨舟')
print(a)

d={'付玺':5, '王思翰':3, '马晟云':4, '安研菲':2, '龙雨舟':1}#dictinory
print(d['龙雨舟'])
d['付玺']=6#改变付玺的值
print(d['付玺'])
print(d.get('付玺'))#从dictinory取数
print('dyb' in d)#判断key是否存在
print('付玺' in d)
print(d.pop('付玺'))#delete fuxi
print(d)
d['曹明君']=7#add caomingjun to dict
print(d)

if 1>3:
    print("pi")
elif 5555>3:
    print("shi")
else:
    print("niao")
    



a=['付玺','王思翰','马晟云']

for name in a:
    print(name)
 '''
'''
pi=0
for x in list(range(101)):# 1~10+
    pi = pi + x
print(pi)

a=1
b=0
while a<101:
    b=b+a
    a+=1
print(b)

print(max(1,3,7))#print the largest number
print(min(43,5,68))#pritn the smallest number
#数据类型转换函数
print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(1.23))
print(str(100))
print(bool(1))
print(bool(''))
'''


def pi(x,a):
    if  a>=80:
        return "%s,good"%(x)
    else:
        return "%s,pi"%(x)


print(pi('安研菲',80))
print(pi('付玺',50))
s = set([1, 1, 2, 2, 3, 3])＃去重

##################################################################
a=(1,3,5,7)  #tuple can not be changed
b=[]
for i in range(4):
    temp=list(a)#change tuple to list
    temp.pop(i)
    b.append(temp)
    
print(b)
##################################################################
'''
题目 7.
编程题，Python 考试样题一，难度系数 3
用 1、3、5、7 这 4 个数字，能组成的互不相同且无重复数字的三位数有哪 些?共有多少个?这些数的和为多少?
【输入】 
无 
【输出】 多行数字，每行一个三位数 组成的三位数的总个数 这些三位数的总和
'''
#25.7
a=(1,3,5,7)#tuple
b=[]
for i in range(4):#xiabiao=0,1.2,3,
    temp=list(a)
    temp.pop(i)
    b.append(temp)

s=[]
for i in range(4):#panduan
    c=b[i]
    for x in c:
        for y in c:
            for z in c:
                if len(set([x,y,z]))==3:
                    s.append([x,y,z])
v=[]
for l in s:#shuchu
    o=''
    for m in l:
        o=o+str(m)
    o=int(o)
    print(o)
    v.append(o)
print(len(v))
g=0
for k in v:
    g=g+k
print(g)
###############################################################################
#题目 8.
'''
25
26
编程实现:
1) 树木主干向上生长;
2) 分形层数为 4，二叉树;
3) 第一层树枝长度为 60，逐层减 小 6;
4) 左右树枝的倾斜角度不限，最 终效果与图所示大致相同即可;
5) 必须看到绘图过程。
'''
import turtle as t

def smallbranch():
    t.forward(48)
    t.right(30)
    t.forward(42)
    t.back(42)
    t.left(60)
    t.forward(42)
    t.back(42)
    t.right(30)
    t.back(48)

def bigbranch():
    t.forward(60)
    t.left(30)
    t.forward(54)
    t.left(30)
    smallbranch()
    t.right(60)
    smallbranch()
    t.left(30)
    t.back(54)
    t.right(60)
    t.forward(54)
    t.left(30)
    smallbranch()
    t.right(60)
    smallbranch()
    t.left(30)
    t.back(54)
    t.left(30)
    t.back(60)
t.left(120)
bigbranch()
t.right(60)
bigbranch()
##########################################
'''题目 50. 考试 191215，Python 编程题真题 【提示信息】
识别出图形中的基本形状，以基本形状为单位绘制出最终图形。 绘制所示图形，中间是半径为 120 的圆，四周是边长为 80 的 12 个菱形。 【编程实现】
使用 turtle 绘制如图中所示的图形。
1) 背景为白色，中间圆为红色轮廓线，不填充;
2) 图中菱形的长对角线延长线经过圆心(如图中虚线所示，虚线不用绘制);
3) 菱形为黑色轮廓线、黄色填充，其中锐角为 60 度;
4) 绘图过程中隐藏画笔，能清 楚地看到图形绘制过程。
【评分标准】(下列各评分项单 独计分，不分先后，合计 25 计 分点)
4 分:正确绘制出一个半径为 120 的不填充、红色圆形;
6 分:正确绘制出一个边长为 80、锐角为 60 度的黄色填充、 黑色轮廓的菱形;
9 分:正确绘制出 12 个相同的菱 形，且其长对角线的延长线经过 圆心(图中虚线不用绘制);
6 分:绘制图形如图所示，菱形方向正确、均匀分布、画笔隐藏，且能看到 绘制过程。
【正确率】20.7%的中高级组考生此题得到满分。18.8%的初级组考生此题得 到满分。'''
import turtle as t
def drawDiamond(angle,color):
    t.speed(0)
    t.penup()
    t.seth(angle)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill() 
    t.pencolor('black')
    t.left(30)
    t.forward(80)
    t.right(60)
    t.forward(80)
    t.right(120)
    t.forward(80)
    t.left(300)
    t.forward(80)
    t.end_fill()
c=30
a=300
b=0
while (c<=360):
    t.seth(c)
    t.pencolor('red')
    t.circle(120,30)
    drawDiamond(a+c,'yellow')
    c=c+30
#############################################################################################################
'''题目 51. 考试 191215，Python 编程题真题 【提示信息】
  41
杨辉三角形，是二项式系数在三角形中的一种几何排列。中国南宋数学家杨 辉在 1261 年所著的《详解九章算法》一书有明确记 载。欧洲数学家帕斯卡在 1654 年发现这一规律，所 以又叫做帕斯卡三角形。其定义为:其顶端(第 1 行)
是 1;第 2 行是两个 1;第 3 行是‘1，2，1’，中间 的‘2’ 是其上方相邻的两个数字的和;依次类推， 产生如图所示的杨辉三角形。
【编程实现】
对于任意输入的 3~15 之间的正整数 n，请编程输出 前 n 行数字、以及由其组成的杨辉三角形。
函数提示:print(‘{:<3}’.format(10)) 能够以 3 个字符宽度、左对齐的方式显 示数字 10。
输入:一个正整数 n(2 ≤ n ≤ 15)。
输出:由两部分组成。第一部分输出由 n 行数字组成的列表;第二部分输出
n 行数字组成的杨辉三 角形。具体输出格式参考如下样例。 【结果样例】
样例输入:请输入一个在 2~15 之间的正整数:6 样例输出:如右图。
【评分标准】(本题合计 35 计分点)
15 分:正确输出 n 行数字组成的列表;
9 分:正确输出 n 行数字组成的杨辉三角 形，输出格式不需要完全符合样例;
11 分:正确输出 n 行数字组成的杨辉三角 形，且格式符合样例，即要求各数字间距相 同、左右对称、上下隔行对齐。
【正确率】此题仅出现在中高级组的考试
中。
12.6%的考生得到或超过 15 分;7.1%的考生得到或超过 24 分;2.4%的考生得 到满分。 考虑到此题为考试最后一题，估计多数考生未做或未完成此题的原 因是时间限制。
'''
import sys
n=input('please input n:')
n=int(n)
if n < 3 or n > 15:
    print ("no")
    sys.exit(0)
a=[]
for i in range(n):
    b=[]
    for j in range(i+1):
        if j==0 :
            b.append(1)
        elif j==i:
            b.append(1)
        elif j>0 and j<=(i-1):
            b.append(a[i-1][j-1]+a[i-1][j])
    a.append(b)
for u in range(n):
    print(a[u])


#######################################################################
  '''  程第一题 【编程实现】
分别输入两个正整数 M、N，输出 M 到 N 之间(含 M、N)所有可被 7 整 除，但不是 5 的倍数的数字，并以逗号分隔按顺序打印在一行。
输入描述:分别输入两个正整数 M、N
输出描述:输出 M 到 N 之间(含 M、N)所有可被 7 整除，但不是 5 的倍数 的数字，并以逗号分隔按顺序打印在一行
【样例输入】
100
147
【样例输出】 112,119,126,133,147

'''
a=input()
b=input()
c=a
c=int(c) 
b=int(b)
while c<=b:
    if c%7==0 and c%5!=0:
        print(c)
        c=c+1
    else:
        c+=1

########################################################################
        '''
题目 52. 考试 200112，Python 编程题真题 【提示信息】
约分是把分数化成最简分数的过程，约分后分数的值不变，且分子分母的最 大公约数为 1，若最终结果的分母为 1，则直接用整数表示。
两个以逗号分隔输入的整数，可以采用如下方法进行转换、分离: str = input()
nums = eval(str)
【编程实现】
  42
输入:输入两个正整数(以逗号分隔)分别作为分数的分子和分母。
输出:第一行显示输入的分数;第二行显示约分后得到的最简分数，若分母 为 1，直接用整数表示。
【结果样例】 样例输入 1: 27,30 样例输出 1: 27/30
9/10 样例输入 2: 36,6 样例输出 2: 36/6
6
【评分标准】(下列各评分项单独计分，得分累加，共 25 计分点)
6 分:能接收输入的信息，在第一行正确显示输入的分数，格式符合样例; 9 分:至少针对一个输入，能输出正确的最简分数，输出格式符合样例;
10 分:针对裁判指定所有样例的输入，都能输出正确的最简分数，且输出格 式符合样例。'''
import sys
c=2
a=input()
b=input()
b=int(b)
a=int(a)
if a==b:
    print("1")
    sys.exit()
else:
    while c<=b:

        if a % c==0 and b%c==0:
            a=a/c
            b=b/c
            print(a,b)
            sys.exit()
        else:
            c+=1

#:) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :)
   '''         
编程第二题 【编程实现】
      输入一行字符，分别统计出其英文字母、空格、数字和其它字符的个数并输
      出。
输入描述:输入一行字符 输出描述:按英文字母、空格、数字和其它字符的顺序输出其对应的个数 【样例输入】
a1b2cd4 !!!5
【样例输出】
4
5
4
3
'''

zifu=0
shuzi=0
zimu=0
kongge=0
a=input()
for b in a:
    c=ord(b)
    if c >=48 and c <= 57:
        shuzi+=1
    elif c>=65 and c<=90 or c>= 96 and c<= 122:
        zimu+=1
    elif c==32:
        kongge+=1
    else:
        zifu+=1
print(zimu)
print(kongge)
print(shuzi)
print(zifu)
#:) :) :) :) :) :) :) :) :) :) :) :) :) :) :) : ): ):) :) :) :) :) :) :) :)

##########################################################
List, tuple, dict, set总结

list
特点:
    相当于一个有序的数组
    通过下标来操作里面的元素
初始化:
    a=[1,'b',3]
读取(通过下标)元素:
    a[0],a[1]
增加元素(只能在最后)
    a.append('pi')
修改已有元素
    a[0]=8
删除(通过下标)元素
    a.pop(0), a.pop(1)
查找元素:
    只能通过遍历整个list
    for i in a
        if i=='c':
            print(i)
切片(从中取出一段元素):
    a[0:2] #[1,'b']
排序:
    >>> a = ['c', 'b', 'a']
    >>> a.sort()
    >>> a
    ['a', 'b', 'c']
    
    

tuple:
特点:
    和list相似, 但初始化后不能修改和删除任何元素

初始化:
    classmates = ('Michael', 'Bob', 'Tracy')
读取(通过下标)元素:
    classmates[0],classmates[1]
查找元素:
    只能通过遍历整个tuple
    for i in classmates
        if i=='Bob':
            print(i)

dict:
特点:
    用来保存一组key/value
    可以使用key来查找和修改value
    key不能重复
    一组key/value在dict中没有顺序
    value可以变化, key不能改变,只能增加和删除
初始化:
    d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
读取(通过key)元素:
    d['Michael'] #如果不存在一个'Michael'的key,就会报错
增加元素:
    d['Adam'] = 67
修改已有元素(如果下标key已经存在就是修改,否则就是增加元素):
    d['Michael']=99
删除(通过Key)元素:
    d.pop('Michael')
查找元素:
    if 'Michael' in d #判断d中是否存在一个key='Michael'
        print(d['Michael']) #如果存在就返回它的value
    或者
    print(d.get('Michael',-1)) #如果存在一个key='Michael'就返回它的value, 如果不存在就返回-1
    
set:
特点:
    用来保存一组key(没有value)
    key不能重复(如果加入重复的key,不会有任何作用)
    一组key在set中没有顺序
    key不能改变,只能增加和删除

初始化:
    >>> s = set([1, 2, 3])
    >>> s
    {1, 2, 3}
增加key:
    >>> s.add(4)
    >>> s
    {1, 2, 3, 4}
删除key:
    >>> s.remove(4)
    >>> s
    {1, 2, 3}

判断set中是否存在某个key:
    >>>print(1 in s)
    Ture
    
