# ex6: String and Text

types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"  # 二进制
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")  # 字符串中嵌入了一个字符串变量，这个字符串变量中还嵌套着另外一个字符串变量。
print(f"I also said:'{y}'")

hilarious = False  # 意思是 欢闹的。我经常喜欢把False错误的写成 Flase，从而造成错误。
joke_evaluation = "Isn't that joke so funny?! {}"  # 这是一种嵌入变量的新方式。

print(joke_evaluation.format(hilarious))  # .format()中引入了新的变量方法。

w = "This is the left side of ..."
e = "a string with a right side."

print(w+e)  # 通过+直接将两个字符串变量连接起来了。

# study drills

# ex6: String and Text

# Assign the string with 10 replacing the formatting character to variable 'x'
x = "There are %d types of people." % 10

# Assign the string with "binary" to variable 'binary'
binary = "binary"

# Assign the string with "don't" to variable 'do_not'
do_not = "don't"

# Assign the string with 'binary' and 'do_not' replacing the
# formatting character to variable 'y'
y = "Those who know %s and those who %s." % (binary, do_not)  # Two strings inside of a string

# Print "There are 10 types of people."
print(x)

# Print "Those who know binary and those who don't."
print(y)

# Print "I said 'There are 10 types of people.'"
print("I said %r." % x)  # One string inside of a string

# Print "I also said: 'Those who know binary and those who don't.'."
print("I also said: '%s'." % y)  # One string inside of a string

# Assign boolean False to variable 'hilarious'
hilarious = False

# Assign the string with an unevaluated formatting character to 'joke_evaluation'
joke_evaluation = "Isn't that joke so funny?! %r"

# Print "Isn't that joke so funny?! False"
print(joke_evaluation % hilarious)  # One string inside of a string

# Assign string to 'w'
w = "This is the left side of..."

# Assign string to 'e'
e = "a string with a right side."

# Print "This is the left side of...a string with a right side."
print(w + e)  # Concatenate two strings with + operator
