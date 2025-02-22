student={112:{"name":"Surubhi","Marks":450,"age":16},115:{"name":"sahil","Marks":470,"age":16}}
for key in student:
    print("Student roll no: ", key,":")
    print("Name:",str(student[key]["name"]))
    print("Marks: ",str(student[key]["Marks"]))
    print("Age:",str(student[key]["age"]))
