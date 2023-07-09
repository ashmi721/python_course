#1. wap that initializes non empty list of words with length=5 display longest word with its length
sample_list = ['Mango','Banana','Kiwi','Apple','grapes']

longest_word = ''
max_len = 0
for word in sample_list:
  print(len(word))
  if len(word) > max_len:
     max_len = len(word)
     longest_word = word

print(longest_word,max_len)


#2. wap to sum all the items in a list
sample_list = [1,2,3,4,5]
sum = 0
for i in sample_list:
  sum+=i
print("The sum of all items",sum)


#3. wap to get the largest number from a list
sample_list =  [10,20,30,100,40]
largest_num = 0
for item in sample_list:
   if item > largest_num:
      largest_num = item
print("largest num is :",largest_num)


#4. wap to get the smallest number from a list
sample_list = [-1,0,1,2]
smallest_num = 0
for item in sample_list:
  if item < smallest_num:
    smallest_num = item
print("smallest num is :",smallest_num)


#5. wap to count the number of strings where the strings length is
# 2 or more and the first and last chracter are same from a given list of strings

input_list = ['abc','xyz','aba','1221']
count = 0
for word in input_list:
 if len(input_list) >= 2:
  if word[0] == word[-1]:
    count += 1
print(count)


#6 wap to check a list is empty or not
list_item = ["Apple"]
if list_item == 0:
  print("list is empty")
else:
  print("list is not empty")



#7. wap to insert a given string at the beginning of all items in a list
list_item = [1,2,3,4]
str_to_insert = "emp"
for i in range(len(list_item)):
  list_item[i] = str_to_insert + str(list_item[i])
print(list_item)