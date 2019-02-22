from stack import Stack 

def postFix(exp):
	stack = Stack()
	expList = exp.split(' ')
	for c in expList:
		#print(c)
		if(c in ['+','-','*','/']):
			operator = c
			b = float(stack.pop())
			a = float(stack.pop())
			if operator == '+':
				result = a + b
			elif operator == '-':
				result = a - b
			elif operator == '*':
				result = a * b
			elif operator == '/':
				result = a / b
			stack.push(result)
		else:
			stack.push(c)
	#print(stack)
	return stack.pop()

def main():
	expression = '9 3 /'
	answer = postFix(expression)
	print(answer)

if __name__ == "__main__":
	main()