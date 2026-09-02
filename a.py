#Write a Python program to take a word and count the number of vowels a,e,i,o,u.

#word = input("Enter a word: ")
#print(sum(ch in "aeiouAEIOU" for ch in word))

#Write a python program to take a sentence and replace all spaces with underscores.

#sentence = input("Enter a sentence: ")
#modified_sentence = sentence.replace(" ", "_")
#print("Modified sentence:", modified_sentence)


#Write a python program to take a sentence , detect double spaces,and replace them with single spaces.

#sentence = input("Enter a sentence: ")
#fixed_sentence = sentence.replace("  ", " ")
#print("Corrected sentence:", fixed_sentence)

#Write a python program to take a word and print it in reverse order using slicing . Also check weather it is the same forward and backward.

#word = input("Enter a word: ")
#reversed_word = word[::-1]
#print("Reversed word:", reversed_word)
#if word == reversed_word:
#    print("It is the same forward and backward (Palindrome).")
#else:
#    print("It is not the same forward and backward.")


#Write a python program to take first name and last name and print initials.


#first_name = input("Enter your first name: ")
#last_name = input("Enter your last name: ")
#initials = first_name[0].upper() + last_name[0].upper()
#print("Your initials are:", initials)



#Write a python program to take a word and print every second character.


#word = input("Enter a word: ")
#print("Every second character:", word[::2])


#Write a python program to take a password and check weather it contains @ and has at least 8 characters.


#pwd = input("Enter password: ")
#print("Valid" if "@" in pwd and len(pwd) >= 8 and "Password must contain 1 uppercase letter in starting" else "Invalid")



#Write a python program to take a string and separate characters prsent at even index positions and odd index positions.


#s = input("Enter a string: ")
#print("Even index characters:", s[::2])
#print("Odd index characters:", s[1::2])



#Take an email address and check weather it contains @ and .com.


#email = input("Enter an email address: ")
#if "@" in email and ".com" in email:
#else:
#    print("Invalid: missing '@' or '.com'")




#Take a sentence containing double spaces and unwanted spaces at the beginning or end . Clean the sentence.


#sentence = input("Enter a sentence: ")
#sentence = sentence.strip()
#while "  " in sentence:
#    sentence = sentence.replace("  ", " ")
#print("Cleaned sentence:", sentence)
