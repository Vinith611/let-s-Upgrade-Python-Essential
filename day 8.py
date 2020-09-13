#day8 assignment 1
def divide(func):
    def inner(a, b):
		a= int(input("Enter a:"))
		b= int(input("Enter b:"))
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("OOPs! cannot divide")
            return

        return func(a, b)
    return inner

def divide(a, b):
    print(a/b)
    
    
    
# day 8 assignment 2
try:
	fname = open("a.txt","r")
	fname.write("hello world")
	
except:
	print("Cannot write the contents to the file")
	
finally:
	f.close()
	print("File closed")
