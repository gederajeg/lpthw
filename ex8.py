formatter = "{} {} {} {}" # variable placeholder

print(formatter.format(1, 2, 3, 4)) # format() is a function. Here it is given four arguments that are passed to and matched up with the four "{}" in the formatter variable. The "{}" in formatter now is replaced with the four arguments inside the format() function

print(formatter.format("one", "two", "three", "four"))

print(formatter.format(True, False, False, True))

print(formatter.format(formatter, formatter, formatter, formatter))

print(formatter.format(

"format() requires the same number of arguments",
"as specified in the variable from which",
"format() receives",
"its values; in this example, it is the `formatter` variable."
))

# the code below will throw error because the number of arguments of format() (only 2)
# do not match with the number of variable holders in formatter (i.e. 4)
## print(formatter.format(formatter, formatter))

## print(formatter.format(

#"My own text",
#"is here"

#))
