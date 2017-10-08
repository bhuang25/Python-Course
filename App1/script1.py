import json
from difflib import get_close_matches

data = json.load(open("data.json", "r"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Y/N: " % get_close_matches(w, data.keys())[0])
        yn = yn.lower()
        if yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn =="n":
            return "The word doesn't exist. Please double check it"
        else:
            return "we didn't understand your response."
    else:
        return "The word doesn't exist. Please double check it"

word = input("What word do you want to look up? ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
