student_data={"id1":{"Name":"sara", "class":"V","subject_intergation":"English,math,science"},
    "id2":{"Name":"David", "class":"V","subject_intergation":"English,math,science"},
    "id3":{"Name":"sara", "class":"V","subject_intergation":"English,math,science"},
    "id4":{"Name":"suriya", "class":"V","subject_intergation":"English,math,science"},}
results={}
seen_keys=[]
for student_id,details in student_data.items():
    unique_key=(details["Name"] ,details["class"] ,details["subject_intergation"])
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        results [student_id]=details
for k,v in results.items():
    print(k,":",v)