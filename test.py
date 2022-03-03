print("Hello,Python!!")
num=1
num01=2
num_01=3

print(num)
print(num01)
print(num_01)
#num$01=4
#num-01=5
#01num=6

# print(num$01=4)
# print(num-01=5)
# print(01num=6)
Num=1
NUM=2

print(Num)
print(NUM)

# return=10
# print("return")

num01=123
num02=1.23

print(type(num01))
print(type(num02))

string_a="Hello,World"

print(string_a)
print(type(string_a))

a=10
b=1

bool01=(a<b)

print(bool01)
print(type(bool01))


a=[["sato","tanaka"],["takahashi","suzuki"]]
print(a[0][0])
print(a[0][1])
print(a[1][0])
print(a[1][1])


x=10
y=2

print(x==y)
print(x!=y)


x=8
y=3

print(x>=5 and x<=10)
print


x=8
y=12
z=20

x+=10
z+=y

print(x)
print(z)


age=0

if age >= 20:
    print("adult")
elif age ==0:
    print("baby")    
else:
    print("child")   


for i in range(5):
    if i ==3:
        continue
    print(i)


# for i in range(3):
#   

arr =[2,4,6,8,10]
sum=0
for i in arr:
    sum+=i
print(sum)

def say_hello(greeting):
    print(greeting)

say_hello("hello")




hello=say_hello
hello("Good Morning")

def div(a,b,c):
    return(a+b+c)/3
div_result=div(9,4,2)    
print(div_result)


class Student:
    def __init__(self,name):
        self.name =name

    def calculate_avg(self,data):
        sum =0
        
        for num in data:
            sum +=num

        avg =sum/len(data)
        return avg
    def judge(self,avg):
        if(avg >=60):
            result="passed"
        else:
            result="failed"     
        return result

a001 = Student("sato")
data = [70,65,50,10,30]
avg =a001.calculate_avg(data)
result = a001.judge(avg)

print(avg)
print(a001.name+""+result)


