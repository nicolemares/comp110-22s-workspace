"""Demonstrations of dictionary capabilities"""


# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# Set a key value pairing in dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NC State"] = 26150

# print a dictionary literal representation
print(schools)

# Acess a value by its key -- "lookup"
print("UNC has (schools['UNC']) students")

# remove a key value from dictionary from key
schools.pop("Duke")

# test for exist\ence of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: (is_duke_present)")

# update key value
schools["UNC"] = 20000
schools["NC State"] += 200

# Demonstartion of dictionary literals

# empty dictionary literal
schools = {} # same as dict()
print(schools)

# Alternatively, intitailize key- vale paire
schools = ("UNC": 19400, "Duke": 6717, "NC State": 26150)
print(schools)

# Example looping over the keys of a dict
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")
