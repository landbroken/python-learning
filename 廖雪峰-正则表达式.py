#廖雪峰-正则表达式
#https://www.liaoxuefeng.com/wiki/
#0014316089557264a6b348958f449949df42a6d3a2e542c000/
#00143193331387014ccd1040c814dee8b2164bb4f064cff000
#正则表达式
import re
rule=r'^\d{3}\-\d{3,8}$'



def MyMatch(strIn:str):
    if(re.match(rule,strIn)):
        print('ok')
    else:
        print('failed')

MyMatch(r'010 12345')
MyMatch(r'010-12345')

#切分字符串
ret=re.split(r'[\s\,]+', 'a,b, c  d')
print(ret)
ret=re.split(r'[\s\,\;]+', 'a,b;; c  d')
print(ret)

#分组
#正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）
#^(\d{3})-(\d{3,8})$分别定义了两个组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
ret=m.group(0)
print(ret)
ret=m.group(1)
print(ret)
ret=m.group(2)
print(ret)

#贪婪匹配
re.match(r'^(\d+)(0*)$', '102300').groups()
re.match(r'^(\d+?)(0*)$', '102300').groups()

#预编译加速
import re
#编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
#使用
ret=re_telephone.match('010-12345').groups()
print(ret)
ret=re_telephone.match('010-8086').groups()
print(ret)

#练习-没通过
strEmail1=r'someone@gmail.com'
strEmail2=r'bill.gates@microsoft.com'
def EmailRule(strIn):
    rule=r'^(\w)+(\.\w+)*@(\w)+((\.\w{2,3}){1,3})$'
    ret=re.match(rule,strIn)
    if(ret):
        print(ret)
    else:
        print("failed")

EmailRule(strEmail1)
EmailRule(strEmail2)
