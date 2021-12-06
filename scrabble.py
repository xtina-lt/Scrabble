# process some data
# organize plaryers, words, points

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

'''Build Dictionary'''
# combine with zip
letter_to_points = {k: v for [k, v] in zip(letters, points)}

# add an element to take into account blank tiles
letter_to_points[""] = 0
print(letter_to_points)

'''Score word'''


def score_word(word):
    point_total = 0
    cap_check = word.upper()
    # iterate through capital word
    for l in cap_check:
        # if letter matches key: add value to total
        for k, v in letter_to_points.items():
            if l == k:
                point_total += v
    return(point_total)
#test: print(score_word('brownie')) == 15


'''Add a word'''


def play_word(player, word):
    player_to_words[player].append(word)
    print(player_to_words['player1'])
    print(score_word(word))


'''Score game'''
player_to_words = {
    'player1': ['BLUE', 'TENNIS', 'EXIT'],
    'wordNerd': ['EARTH', 'EYES', 'MACHINE'],
    'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'],
    'Prof Reader': ['ZAP', 'COMA', 'PERIOD']
}


def update_point_totals():
    player_to_points = {}
    # iteratet thgrough player_to_words
    for k, v in player_to_words.items():
        # track player points
        player_points = 0
        # iterate through values
        for i in v:
            # update points
            player_points += score_word(i)
        # add 'key'player: 'value'points to player_to_points dictionary
        player_to_points[k] = player_points

    return print(player_to_points)


'''PLAY'''
# get score
update_point_totals()
# play new word
play_word('player1', 'brownie')
# see update
update_point_totals()


'''output'''
# {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 4, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10, '': 0}
# {'player1': 29, 'wordNerd': 32, 'Lexi Con': 31, 'Prof Reader': 31}
# ['BLUE', 'TENNIS', 'EXIT', 'brownie']
# 15
# {'player1': 44, 'wordNerd': 32, 'Lexi Con': 31, 'Prof Reader': 31}
