def is_character_match(string1, string2):
	list1 = []
	list2 = []

	for i in sorted(string1.lower()):
		if i != ' ':
			list1.append(i)

	for j in sorted(string2.lower()):
		if j != ' ':
			list2.append(j)
	
	str1 = ''.join(list1)
	str2 = ''.join(list2)

	return str1 == str2
	