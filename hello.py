# /usr/bin/env python
# _*_ coding:utf-8 _*_

print (ord("A"))
print (chr(65))
print (u"中文")
print (u"u4e2d")

length = 10
for i in range(length):
	print ("i = %d" % i)

def testDef(x):
	if not isinstance(x ,int):
		raise TypeError("X Error")
	
	print (x)

testDef(100)

#testDef(3.14)

for index ,number in enumerate(range(5)):
	print ("index = %d , number = %d" %(index,number))

print([x*x for x in range(10)])
c = ["A","B","C"]
print ([str(a)+""+b for a in range(3) for b in ["A","B","C"]])

def gen():
	print (10)
	yield 1
	print (20)
	yield 2
	print (30)
	yield 3

g = gen()
print (g.next())
print (g.next())
print (g.next())
#print (g.next())

import functools

def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print ("this is wapper")
		return func(*args,**kw)
	return wrapper



@log
def now():
	print ("now")
now()






def test1():
    print ("test1")

test1()

def test2():
	print (0)

def test3(a):
	print ("test")

test3(100)









