str_len = "Hello world!"
#1.use the len method to print the length of the string
print(len(str_len))


#2.print the length of the string without using len function.
count = 0
for i in str_len:
  count+=1
  print(count)



#3.write python program to print vowel and consonants on the given string
user_str = input("Enter the string a-z: ")
vowel = ["a","e","i","o","u"]
for i in user_str:
   if i.lower() in vowel:
     print(user_str,"is vowel string")
   else:
    print(user_str,"is the consonant String")



#4.wap to extract first and last 2 character into new string,
#ex: input string = "my name is xyz" and output string = "myyz"
input_str = "my name is xyz"
ex_first = input_str[:2]
ex_last = input_str[-1:-3:-1]
print(ex_first + ex_last)


#5.Wap to get a single string from two given strings, separated by a space and swap the first two characters of each string.
  # ex: first_str = "first", second_str = "second" , output = "serst ficond"
first_str = "first"
second_str = "second"

print(second_str[:2]+first_str[2:])
print(first_str[:2]+second_str[2:])



#6.wap to remove the nth index chracter from a nonempty string. ask user to input non-empty string, and index.
  #eg :non-empty-str= "Hello world!"
user_string = input("Enter the String: ")
user_index = int(input("Enter the index of the char to remove: "))
output_str = " "
if user_index < len(user_string):
     for i, char in enumerate(user_string): #this enumerate() iterate over the user_string with index
      #  print(user_string)
        if i == user_index:
           continue
        output_str += char
     print(output_str)
else:
    print("Out of range")





