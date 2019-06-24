#-----------------------------------------------------------
#TO DO

#figure out why the "if x == False:" does not work in check_existence, do_modify_word, do_delete_word.
#read about classes
#read about repl
#rewrite the script based on what I learned.

#-----------------------------------------------------------
#ATTEMPTS

#The next three dicts are not in use here.
#I added them because I considered them an option at some point in the process.
dictionary_E = {
	'create': 'erstellen',
	'retrieve': 'aufrufen',
	'update': 'aktualisieren',
	'delete': 'löschen',
	'read': 'lesen',
	'evaluate': 'auswerten',
	'print': 'ausgeben',
	'loop': 'wiederholen'
}
list_of_dicts = [
	{'erstellen': 'create', 'aufrufen': 'retrieve', 'aktualisieren': 'update', 'löschen': 'delete', 'lesen': 'read', 'auswerten': 'evaluate', 'ausgeben': 'print', 'wiederholen': 'loop'},
	{'create': 'erstellen', 'retrieve': 'aufrufen', 'update': 'aktualisieren', 'delete': 'löschen', 'read': 'lesen', 'evaluate': 'auswerten', 'print': 'ausgeben', 'loop': 'wiederholen'}
	]
dict_KGE = {'1':['erstellen', 'create'], '2':['aufrufen', 'retrieve'], '3':['aktualisieren', 'update'], '4':['löschen', 'delete']}

#The def update_check is not in use here.
#I added it because you could use it after every chosen_action and see whether the dict has been updated.
def update_check(German_word, English_word):
	print(f"\nAre {German_word} and {English_word} in the dictionary?")
	new_word = True
	for key in dictionary_G.items():
		if German_word == key:
			new_word = True
			print("Yes.")#Initially, I wanted "True" or "False"

	if new_word == False:#does not work.
	#Also, I don't know if this case (new_word == False) is ever gonna be "False".
		print("There must be a mistake.")
		exit()
	start()

#-----------------------------------------------------------

action_list = ['Add a word', 'See if a word already exists', 'Modify a translation', 'Delete a word', 'Quit']

dictionary_G = {
	'erstellen': 'create',
	'aufrufen': 'retrieve',
	'aktualisieren': 'update',
	'löschen': 'delete',
	'lesen': 'read',
	'auswerten': 'evaluate',
	'ausgeben': 'print',
	'wiederholen': 'loop'
}

def do_add_word():
	German_word = input("\nAdd the German word: ")
	English_word = input("Add the English word: ")
	newdict= {}
	newdict[German_word] = English_word

	item_found = False
	for key, value in dictionary_G.items():
		if German_word == key and English_word == value:
			item_found = True
			print("Already exists.")
			do_add_word()

	dictionary_G.update(newdict)
	display_dict()
	start()

def check_existence():
	check_word = input("\nDoes the following word already exist in the dictionary? ")

	word_exists = True
	for key in dictionary_G.keys():#Could I somehow merge the two for-loops?
		if check_word == key:
			word_exists = True
			print(f"{check_word} already exists.")
			exit()

	for value in dictionary_G.values():
		if check_word == value:
			word_exists = True
			print(f"{check_word} already exists.")
			exit()

	if word_exists == False: #does not work.
		print(f"{check_word} does not exist yet. Would you like to add it?")
		add_word = input(">")
		if add_word == "yes":
			do_add_word()
		if add_word == "no":
			exit()

def do_modify_word():
	modify_word = input("\nWhat word would you like to change? ")

	item_found = True
	for key, value in dictionary_G.items():#Could I somehow merge the two for-loops?
		if modify_word == value:
			item_found = True
			English_word = input("Enter the new word: ")
			newdict = {}
			newdict[key] = English_word
			dictionary_G.update(newdict)
			display_dict()
			start()

	for key in dictionary_G.keys():
		if modify_word == key:
			item_found = True
			German_word = input("Enter the new word: ")
			dictionary_G[German_word] = dictionary_G.pop(key)
			display_dict()
			start()

	if item_found == False:#does not work.
		print("Enter a word from the dict.")
		display_dict()
		do_modify_word()

def do_delete_word():
	delete_word = input("\nWhat word would you like to delete? ")

	#key_found = True
	for entry in dictionary_G.keys():
		if delete_word == entry:
			#key_found = True
			del dictionary_G[delete_word]
			print(f"\n{delete_word} has been deleted.")
			display_dict()
			start()
	for entry in dictionary_G.values():# here, I wanted to use 'if key_found == False',
	#but it wouldn't work.
		if delete_word == entry:
			#key_found = False
			print("Enter the German word.")
			do_delete_word()
	# if key_found == False:#does not work.
	# 	print("Enter the German word.")
	# 	do_delete_word()

def display_dict():
	print("\nHere's your dictionary:\n")
	print ("{:<15} {:<15}".format('GERMAN', 'ENGLISH'))
	for k, v in dictionary_G.items():
		print("{:<15} {:<15}".format(k, v))

def start():

	continue_flag = True

	while continue_flag:

		display_dict()

		print ("\nPlease choose what you want to do to the dictionary:\n")
		for index, action in enumerate (action_list, start=1):
			print (index, action)

		chosen_action = input()

		if chosen_action == "1":
			do_add_word()

		if chosen_action == "2":
			check_existence()

		if chosen_action == "3":
			do_modify_word()

		if chosen_action == "4":
			do_delete_word()

		if chosen_action == "5":
			continue_flag = False

	exit()

start()
