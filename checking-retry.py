password = 'a123456'
i = 3 # 剩餘機會
while i > 0:
	code = input ('please enter your password:')
	if code == password:
		print ('enter')
		break
	else:
		i = i -1
		print ('密碼錯誤！！還有', i, '次機會')
		
	



		


