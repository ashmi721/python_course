l = lambda x: x*x*x
l(2)

'''  lambda with filter '''
l1 = [2,34,56,45,33,24,39,58]
list(filter(lambda x: (x%2==0),l1))


'''  lambda with map '''
l1 = [3,2,34,56,45,33,24,39,58]
list(map(lambda x: (x%2==0),l1))
l2 = [1,2,3,4,5,6]
list(map(lambda x:(x*x),l2))

''' lamba with reduce '''
from functools import reduce
# import functools
lis = [1, 3, 5, 6, 7,2]
sum = reduce(lambda a,b:a+b,lis)
print(f"The sum of the list using reduce is: {sum}")


largest= reduce(lambda a,b:a if a>b else b,lis)
print(f"Check the largest number using lambda and reduce funtion is: {largest}")
