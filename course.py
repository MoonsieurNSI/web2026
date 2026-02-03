def nombre_coureurs(lst):
	'''
	retourne le nombre de coureurs dans lst
	'''
	assert type(lst) == list
	assert all([type(obj) == str for obj in lst]) == True
	return len(lst)

#############################
def premier(lst):
	'''
	retoune le premier coureur de lst
	'''
	assert type(lst) == list
	assert all([type(obj) == str for obj in lst]) == True
	return lst[0]


#############################
def dernier(lst):
	'''
	retoune le dernier coureur de lst
	'''
	assert type(lst) == list
	assert all([type(obj) == str for obj in lst]) == True
	return lst[len(lst) - 1]

##############################
def coureur_en_position(lst, position):
	'''
	retoune le coureur à la position: postion - 1
	'''
	assert type(lst) == list
	assert all([type(obj) == str for obj in lst]) == True
	assert type(position) == int and position >= 1 and position <= len(lst)
	return lst[position - 1]


# Test
classement = ["Nadia", "Franck", "Thomas", "Elizabeth", "Laure"]
assert nombre_coureurs(classement) == 5
assert premier(classement) == "Nadia"
assert dernier(classement) == "Laure"
assert coureur_en_position(classement, 1) == "Nadia"
assert coureur_en_position(classement, 3) == "Thomas"

print("bvo poulet")
