# ------------------------
# -- Dictionary Methods --
# ------------------------

# clear()

user = {
  "name": "Osama"
}
print(user)
user.clear()
print(user)

print("=" * 50)

# update()

member = {
  "name": "Osama"
}
print(member)
member["age"] = 36
member["omar"] = "Developer"
print(member)
# member.update({"country": "Egypt"})
member.update({"skills" :"html , css" })
print(member)

print("=" * 50)

# copy()

main = {
  "name": "Osama"
}
c =["omar" , "samir"]
c.append("omar")
print(c)

b = main.copy()
print(b)
main.update({"skills": "Fighting"})
print(main)
print(b)

# keys() + values()

print(main.keys())
print(main.values())