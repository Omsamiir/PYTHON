# ----------------
# -- User Input --
# ----------------

fName = input('What\'s Is Your First Name?')
mName = input('What\'s Is Your Middle Name?')
lName = input('What\'s Is Your Last Name?')

fName = fName.lstrip().capitalize()
mName = mName.rstrip().capitalize()
lName = lName.rstrip().capitalize()

print(f"Hello {fName}    {mName:.1s} {lName} Happy To See You.")