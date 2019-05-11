import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    wl = w.lower()
    if wl in data:
        return data[w]
    elif w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = raw_input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0]).rstrip()
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = raw_input("Enter word: ").rstrip()
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
