# Find the count of vowels and consonants in the given string
string = input('enter a string')
# hello --> vowels=2, consonants=3
vowels = ['a', 'e', 'i', 'o', 'u']
vowelCount = 0
consonantCount = 0
for letter in string:
    if letter in vowels:
        vowelCount = vowelCount + 1
    elif letter.isalpha():
        consonantCount = consonantCount + 1

print('vowel count =',vowelCount)
print('consonant count =',consonantCount)