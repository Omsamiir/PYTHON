# ------------------------
# -- Dictionary Methods --
# ------------------------

# setdefault()

user = {
  "name": "Osama"
}
print(user)
print(user.setdefault("age", 36))
print(user)
user.setdefault("skills", "html")
c = user.copy()
print(c)
print("=" * 40)

# popitem()

member = {
  "name": "Osama",
  "skill": "PS4"
}
print(member)
member.update({"age": 36})
print(member.popitem())

print("=" * 40)

# items()

view = {
  "name": "Osama",
  "skill": "XBox"
}

allItems = view.items()
print(view)
view["age"] = 36

print(allItems)

print("=" * 40)

# fromkeys()

a = ('MyKeyOne', 'MyKeyTwo', 'MyKeyThree')
b = "X"
c = {
  "omar": {
    "12":"11"
  },
  "samm": {
    "samir"
  }
}
print(dict.fromkeys(c, "omar""omar"))
print(dict.fromkeys(a, b))
print(type(a))