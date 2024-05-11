def TextNum(my_str):
	if len(my_str) != 4:
		if len(my_str) != 6:
			return False
	for i in my_str:
		try:
			int(i)
		except:
			return False
	return True
text = input()
print(TextNum(text))