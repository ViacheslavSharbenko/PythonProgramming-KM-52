c_types = ("diamonds","hearts","cubs","spades")
values = tuple(["A"] + list(range(2,11))+ ["J", "Q","K" ] )
def deck_cards(c_types, values):
    for i in c_types:
        for j in values:
            yield f"{j} {i}"
deck = deck_cards(c_types, values)
while True:
    try:
        print(next(deck))
    except StopIteration:
        print("StopIteration: there is no more carsd in the deck.")
        break