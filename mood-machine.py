questions = {"Did you sleep well last night? (yes/no):": "" , "are you hangry?(yes/no)": "","are you happy ?(yes/no)":"" }
for question in questions : 
    request = input(question)
    if request == "yes" :
        print ( "you are good")
    else :
        print("you are not good") 

