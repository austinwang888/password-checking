password = 'a123456'
i = 3
while True:
	code = input ('please enter your password:')
	if code == password:
		print ('enter')
		break
	else:
		i = i -1
		print ('密碼錯誤！！還有', i, '次機會')
		if i == 0:
			break
	



		


