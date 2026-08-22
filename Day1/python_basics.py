name = "Aniket"
skills = ["Python", "SQL", "ETL", "PostgreSQL"]

print("Name:", name)
print("Skills:", skills)

for skill in skills:
    print("Learning:", skill)


    #create a function to add a new skill to the skills list
    def introduce(name, skills):
        print(f"My name is {name}")
    print("My Data Engineering skills:")

    for skill in skills:
        print("-", skill)


introduce(name, skills)

