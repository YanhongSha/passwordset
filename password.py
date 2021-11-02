# password practice

password = 'a123456'
i = 3

while True:
	i = i-1
	word = input('please input your password:')
	if word == password:
		print('congratulations! You could log in')
		break
	
	elif i > 0:
	    print('sorry, please input your password again, you have', i, 'times left' )

	elif i == 0: 
		print('sorry your account is blocked')
		break
