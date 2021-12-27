# ------------------------
# -- Strings Formatting --
# ------------------------

name = "Osama"
age = 36
rank = 10

print("My Name is " + name)
# print("My Name is: " + name + " and My Age is: " + age)  # Type Error

print("My Name is: %s" % "Osama")
print("My Name is: %s" % name)
print("My Name is: %s and My Age is: %d" % (name, age))
# print("My name is %s" %name)
print("My Name is: %s and My Age is: %d and My Rank is: %f" % (name, age, rank))
print("my name is omar %s and my age is %d and my rank is %f" %(name,age,rank))

# %s => String
# %d => Number
# %f => Float

n = "Osama"
l = "Python"
y = 10

print("My Name is %s Iam %s Developer With %d Years Exp" % (n, l, y))

# Control Floating Point Number

myNumber = 10
print("My Number is: %d" % myNumber)
print("My Number is: %f" % myNumber)
print("My Number is: %.2f" % myNumber)
print("my number is %.4f" %myNumber)

# Truncate String

myLongString = "Hello People of Elzero Web School I Love You All"
print("Message is %s" % myLongString)
print("Message is %.25s" % myLongString)