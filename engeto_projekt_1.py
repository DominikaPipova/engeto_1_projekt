TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

#users and their password
registered_users = dict()
registered_users = {"bob": "123", "ann":"pass123", "mike": "password123", "liz": "pass123"}

#user is requsted to insert their username and password
user = input("Zadej username: ")
password = input("Zadej heslo: ")

oddelovac = "-" * 40
print(oddelovac)

#verification of user and password
if user in registered_users.keys() and registered_users.get(user) == password:
  print(f"Welcome to the app, {user}")
  print(f"\nWe have {len(TEXTS)} texts to be analyzed.")
  print(oddelovac)
else: 
  print(f"Your username or password is invalid.")
  print(oddelovac)
  exit()

#if TEXTS does not have any text, the program ends.
#if the TEXTS does have any text, the max text to select is given to the user to select from. 
if TEXTS == []:
  print("There is no text to be choose from.")
  exit()

#user is requested to insert which text they want to analyze
selected_text = input(f"Enter a number between 1 and {len(TEXTS)} to select: ")
print(oddelovac)

#verification if the input is valid. If not, the program ends.
if selected_text.isnumeric():
  selected_text = int(selected_text) - 1
  if selected_text > len(TEXTS):
    print(f"The selected text does not exist in TEXTS. Enter a number between 1 and {len(TEXTS)}. Star the program again.")
    exit()
else:
  print("This is not a number. Start the program again and select a valid number.")
  exit()

#separation and clean up of each text in TEXTS
words = TEXTS[selected_text].split()
words = [word.strip(".,:?!") for word in words]

#count of words in the text
print(f"There are {len(words)} words in the selected text.")

#preparation of lists to count the words in each text for the analysis
titlecase_words = []
uppercase_words = []
lowercase_words = []
numeric_words = []

for word in words:
  if word.istitle():
    titlecase_words.append(word)
  elif word.isupper():
    uppercase_words.append(word)
  elif word.islower():
    lowercase_words.append(word)
  elif word.isalnum():
    numeric_words.append(word)
print(f"There are {len(titlecase_words)} titlecase words.")
print(f"There are {len(uppercase_words)} uppercase words.")
print(f"There are {len(lowercase_words)} lowercase words.")
print(f"There are {len(numeric_words)} numeric strings.")
print(f"The sum of all the numbers is {sum([int(word) for word in numeric_words])}")

#calculation of the lenght for each word in the selected text
words_lenght = []
for word in words:
  words_lenght.append(len(word))

words_lenght = sorted(words_lenght) #to have the table from the shortest to longest word

counts = {} #creation of a dictionary to have the lenght as keys and the count of the occurance as values
for lenght in words_lenght:
  counts[str(lenght)] = counts.setdefault(str(lenght),0) + 1

column_width = max(counts.values()) + 2 #calculation of the middle column width
symbol = "*" #to represent the column graph

print(oddelovac)
print("LEN|".rjust(6) + "OCCURENCES".center(column_width) + "|NR.") #header of the table
print(oddelovac)

#values in the table
for keys in counts:
  print(keys.rjust(5) + "|" + (counts[keys] * symbol).ljust(column_width) + "|" + str(counts[keys]))
