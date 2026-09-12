import module.converter as converter

answer = input("select for converting to kg or lbs :")
if answer == "kg" or "kgs":
    converter.lbs_to_kg()
elif answer == "lbs":
    converter.kg_to_lbs()
else:
    print("please enter correctly !!!")
