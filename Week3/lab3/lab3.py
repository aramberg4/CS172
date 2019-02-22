from fraction import Fraction

def H(n):
	h = Fraction(0,1)
	for k in range(1,n+1):
		h += Fraction(1,k)
	return h

def T(n):
	t = Fraction(0,1)
	k = 0
	while(k <= n):
		#print('k='+str(k))
		t += Fraction(1,2)**k
		#print('t='+str(t.approximate()))
		k+=1
	return t

def Z(n):
	z = Fraction(0,1)
	for k in range(0,n+1):
		z += Fraction(1,2)**k
	return Fraction(2,1) - z

def R(n, b):
	r = Fraction(0,1)
	for k in range(1,n+1):
		r += Fraction(1,k)**b
	return r


def main():
	print('Welcome to Fun with Fractions!')
	while True:
		try:
			userInput = int(input('Enter Number of iterations (integer>0): '))
			break
		except:
			print('Not accepted. Try again.')
	print( 'H(' +str(userInput) + ')=' + str(H(userInput)))
	print( 'H(' +str(userInput) + ')~=' + str(H(userInput).approximate()))
	print( 'T(' +str(userInput) + ')=' + str(T(userInput)))
	print( 'T(' +str(userInput) + ')~=' + str(T(userInput).approximate()))
	print( 'Z(' +str(userInput) + ')=' + str(Z(userInput)))
	print( 'Z(' +str(userInput) + ')~=' + str(Z(userInput).approximate()))
	for i in range(2,9):
		print( 'R(' +str(userInput) + ','+str(i)+')=' + str(R(userInput,i)))
		print( 'R(' +str(userInput) + ','+str(i)+')~=' + str(R(userInput,i).approximate()))

if __name__ == "__main__" :
    main()