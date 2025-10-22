# 1.inbuild function

sentence="Emma-is-a-data-scientist"
words=sentence.split("-")
for w in words:
    print(w)

# 1.without inbuild function


sentence="Emma-is-a-data-scientist"
word=""
for c in sentence:
    if c!="-":
        word=word+c
    else:
        print(word)
        word=""
print(word)



# 2.inbuild function

str1 = "Python"
reverse =(reversed(str1))
join=''.join(reverse)
print(join)



# 2.without inbuild function

str1 = "Python"
print(str1[::-1])


# 3. question


sentence = "Hello World"
count = 0
for c in sentence.lower():  
    if c not in "aeiou ":
        count += 1
print("Number of consonants:", count)



# 4. question

sentence = "Python is awesome"
empty_space=""
for c in sentence:
    if c !=" ":  
        empty_space=empty_space + c
print(empty_space)



# 5. question

password = input("Enter your password: ")
special_char = "!@#$%^&*"
if len(password) >= 8 and any(char in special_char for char in password):
    print("Password is strong")
else:
    print("Password is not strong")