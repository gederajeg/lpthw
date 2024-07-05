print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10) # what'd that do? -- this code will print dots (".") ten times (`* 10`)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# Watch `end = ' '` at the end. Try removing it to see what happens.
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)

# GPWR's comment:
# 1. When the `end = ' '` part is present in line 20, the output of line 20 ("Cheese") and line 21 ("Burger") is joined into one line.
# Mary had a little lamb.
# Its fleece was white as snow.
# And everywhere that Mary went.
# ..........
# Cheese Burger <- here's the output

# 1. When the `end = ' '` part is absent in line 20, the output of line 20 ("Cheese") and line 21 ("Burger") is separated into different line.
# Mary had a little lamb.
# Its fleece was white as snow.
# And everywhere that Mary went.
# ..........
# Cheese
# Burger <- here's the output