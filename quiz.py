def list comprehension():
	a=[100,110,120,130,140,150]:
	h=a/3
	print(h)
	
	
def sorted():
	a=['apple','banana','mango']
	b=['avocado','peach','orange']
    c=['pineapple','lemon','guava']
    d=set(a+b+c)
    print(d)

def divisible_by_three(n):
	divisible=range(1,n%3)
	final_divisible=division(divisible)
	print(final_divisible)
	

def list():
	x=[[1,2],[3,4],[5,6]]
	h=[]
	for sublist in x
		for h in sublist:
			print(h.append(x))

def smallest():
	n=[1,3,4,6,8,9]
	print (min(n))


def duplicate():
	s=['a','b','a','e','d','b','c','e','f','g','h']
	print(s.sort())

def student():
    student1= {'age': 19, 'name': 'joy'}
    student2= {'age': 20, 'name': 'conny'}
    student3= {'age': 15, 'name': 'nasambu'}
    student4= {'age': 18, 'name': 'Natasha'}
    Students=[student1,student2,student3,student4]
    for student in Students:
    	print("Hello {} your were born {}.".format(student["name"],student['age']))

			