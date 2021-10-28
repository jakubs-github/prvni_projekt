'''
author =
'''
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

pocet_text = len(TEXTS)

oddelovac = 42 * "-"

database = {
	'bob': '123',
	'ann': 'pass123',
	'mike': 'password123',
    'liz': 'pass123'
			}

# vložení a ověření uživatelského jména a hesla,
# v případě nesprávných údajů oznámit a ukončit
uzivatelske_jmeno = input("username: ")
heslo = input("password: ")

if database.get(uzivatelske_jmeno) == heslo:
    print(f"""{oddelovac}
Welcome to the app, {uzivatelske_jmeno}
We have {pocet_text} texts to be analyzed.
{oddelovac}
""")
else:
    print("Username or password doesn't exist!")
    quit()

#vyžádání čísla textu k analýze
vybrane_cislo = input(f"Enter a number btw. 1 and {pocet_text} to select: ")
if vybrane_cislo.isalpha():
    print(f"""Invalid input!
{oddelovac}
""")
    quit()
elif int(vybrane_cislo) >= (pocet_text+1) or int(vybrane_cislo) == 0:
    print(f"""Out of range!
{oddelovac}
""")
    quit()
elif int(vybrane_cislo) >= 1 and int(vybrane_cislo) <= pocet_text:
    print(oddelovac)

# Rozdělit text na slova, vyčistit a vložit do listu
jednotlivy_text = TEXTS[int(vybrane_cislo)-1]
vycistena_slova = list()

for slovo in jednotlivy_text.split():
    vycistena_slova.append(
        slovo.strip(",.:;"))

# Analýza textu a výpis

pocitadlo = {"sum": 0,
             "titlecase": 0,
             "uppercase": 0,
             "lowercase": 0,
             "num": 0,
             "sumnum": 0}

for slovo in vycistena_slova:
    if slovo.istitle():
        pocitadlo["titlecase"] += 1

for slovo in vycistena_slova:
    if slovo.isalpha():
        pocitadlo["sum"] += 1

for slovo in vycistena_slova:
    if slovo.isupper():
        pocitadlo["uppercase"] += 1

for slovo in vycistena_slova:
    if slovo.islower():
        pocitadlo["lowercase"] += 1

soucet = list()
for slovo in vycistena_slova:
    if slovo.isdigit():
        pocitadlo["num"] += 1
        soucet.append(int(slovo))

pocitadlo["sumnum"] = sum(soucet)

print(f"""There are {pocitadlo["sum"]} words in the selected text.
There are {pocitadlo["titlecase"]} titlecase words.
There are {pocitadlo["uppercase"]} uppercase words.
There are {pocitadlo["lowercase"]} lowercase words.
There are {pocitadlo["num"]} numeric strings.
The sum of all the numbers {pocitadlo["sumnum"]}.""")
print(oddelovac)

# výskyty pro každé slovo
delky_slov = dict()

for slovo in vycistena_slova:
    if len(slovo) not in delky_slov:
        delky_slov.update({len(slovo): 1})
    elif len(slovo) in delky_slov:
        delky_slov[len(slovo)] += 1

# výpis výsledků
print(f"""LEN|    OCCURENCES    | NR.
{oddelovac}""")
for key, value in sorted(delky_slov.items()):
    print(f"""{key: ^3}|{value * "*": <17} | {value}""")