favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.") #Sarah's favorite language is C.

print("\n")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.") #Print all key-value pairs

friends = ['phil', 'sarah']
for name in favorite_languages.keys(): #Loop through keys
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!") #Print only friends

print("\n")

for name in sorted(favorite_languages.keys()):  #Loop through sorted keys (ALPHABETICAL ORDER)
    print(f"{name.title()}, thank you for taking the poll.") #Print sorted keys

print("\n")

print("The following languages have been mentioned:")
for language in favorite_languages.values(): #Loop through values
    print(language.title()) #Print all values

print("\n")

for language in set(favorite_languages.values()): #Loop through values (without repetition)
    print(language.title()) #Print all values

print("\n")

languages = {'python', 'rust', 'python', 'c'} #Build a set directy
print(languages) #{'rust', 'python', 'c'}

print("\n")

favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
"""
Jen's favorite languages are:
    Python
    Rust

Sarah's favorite languages are:
    C

Edward's favorite languages are:
    Rust
    Go

Phil's favorite languages are:
    Python
    Haskell
"""