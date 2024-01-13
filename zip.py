
names = ['sabari','nithi','chithra','murugan']  # LIST
age = (21,11,43,45)  # TUPLE
profession = ['SDE','STU','Tyr','Writer']

# ZIP WILL RETURN A LIST OF TUPLE PAIRS
zip_items = list(zip(names, age))
print(zip_items)

zip_items = list(zip(zip_items,profession))
print(zip_items)