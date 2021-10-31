password = 'a123456'
while True:
	code = input ('please enter your password:')
	if code == password:
		print ('enter')
		break
	elif code != password:
		print ('密碼錯誤！！還有兩次機會')
	code = input ('please enter your password:')
	if code == password:
		print ('enter')
		break 
	elif code != password:
		print ('密碼錯誤！！還有一次機會')
	code = input ('please enter your password:')
	if code == password:
		print ('enter')
		break
	elif code != password:
		print ('輸入失敗')
		break



		


