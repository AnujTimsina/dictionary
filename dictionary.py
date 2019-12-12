import json
from difflib import get_close_matches
data= json.load(open("data.json"))



def meaning(user_input):
    user_input=user_input.lower()
    if user_input in data.keys() :
        return data[user_input]
    elif len(get_close_matches(user_input,data.keys())) > 0:
        nearest_match= get_close_matches(user_input,data.keys(),cutoff= 0.8)[0]
        print("Nearest match found is  :",nearest_match )
        yn=input("Is that the actual word? \nPress Y for yes and N for no!! ->>>")
        if yn =="Y":
            return meaning(nearest_match)
        elif yn == "N":
            return "The word doesn't exist.Please, re-enter."
        else:
            return "The word doesn't exist."
    else:
        return "The word doesn't exist!!"

user_input= input("Enter word:")
print(meaning(user_input))



