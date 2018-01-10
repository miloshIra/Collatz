import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(word):
  # word = word.lower() moze i vaka mesto .lower() na input
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == 'N':
            return "The word does not exist please check your spelling."
        else:
            return "We didin't understand your entry."
    else:
        return "The word does not exist please check your spelling."

word = input("Enter word: ").lower()

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)


    

