def make_correct_ending(number, word):
    '''Makes the correct word ending for "ночь" or "тур" depending on n'''
    night = {
        '1': 'ночь',
        '2': 'ночи', '3': 'ночи', '4': 'ночи',
        '5': 'ночей', '6': 'ночей', '7': 'ночей', '8': 'ночей', '9': 'ночей', '0': 'ночей',
    }
    tour = {
        '1': 'тур',
        '2': 'тура', '3': 'тура', '4': 'тура',
        '5': 'туров', '6': 'туров', '7': 'туров', '8': 'туров', '9': 'туров', '0': 'туров',
    }

    number, ending = str(number), night if word == 'night' else tour
    if number not in ('11', '12', '13', '14'):
        return f"{number} {ending[number[-1]]}"
    else:
        return f"{number} ночей" if word == 'night' else f"{number} туров"
