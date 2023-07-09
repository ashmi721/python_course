'''In python operator precedent
1 (Highest)	()	Parenthesis
2	**	Exponent
3	+x, -x ,~x	Unary plus, Unary Minus, Bitwise negation
4	*, /, //, %	Multiplication, Division, Floor division, Modulus
5	+, -	Addition, Subtraction
6	<<, >>	Bitwise shift operator
7	&	Bitwise AND
8	^	Bitwise XOR
9	|	Bitwise OR
10	==, !=, >, >=, <, <=	Comparison
11	is, is not, in, not in	Identity, Membership
12	not	Logical NOT
13	and	Logical AND
14 (Lowest)	or	Logical OR'''

num1 =float(input("Enter the first number :"))
num2 =float(input("Enter the second number :"))

add = num1 + num2
print("the sum is ",add)

sub = num1 - num2
print("the sub is ",sub)

mul = num1 * num2
print("the mul is ",mul)

div = num1 / num2
print("the div is ",div)

mod = num1 % num2
print("the mod is ",mod)

