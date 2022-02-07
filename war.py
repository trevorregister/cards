from cards import *

A = Owner("A")
B = Owner("B")
Board = Owner("Board")
deck = Deck()

deck.build()
deck.shuffle()

A.new_belonging("Hand", Pile())
A.new_belonging("Library", Pile())

B.new_belonging("Hand", Pile())
B.new_belonging("Library", Pile())

Board.new_belonging("Deck", deck)
Board.new_belonging("Sideboard", Pile())

shift_card(Board.belongings["Deck"], A.belongings["Library"], 26)
shift_card(Board.belongings["Deck"], B.belongings["Library"], 26)

turn_count = 0
A_win_count = 0
B_win_count = 0

def turn():
    winner = Board
    while winner == Board:
        if len(A.belongings["Library"].contents)==0 or len(B.belongings["Library"].contents)==0:
            return "Game Over"
        A.draw_card("Library", "Hand", 1)
        B.draw_card("Library", "Hand", 1)

        A_card = A.belongings["Hand"].contents[0]
        B_card = B.belongings["Hand"].contents[0]

        A_message = "A plays a "+ str(A_card.value) + " of "+A_card.suit + ". "
        B_message = "B plays a "+ str(B_card.value) + " of "+B_card.suit
        #print(A_message+B_message)

        if A_card.value > B_card.value:
            winner = A
        if A_card.value < B_card.value:
            winner = B
        
        shift_card(A.belongings["Hand"], Board.belongings["Sideboard"], 1)
        shift_card(B.belongings["Hand"], Board.belongings["Sideboard"], 1)

    shift_card(Board.belongings["Sideboard"], winner.belongings["Library"], len(Board.belongings["Sideboard"].contents))        

    #print (winner.name + " wins this round.")
    A.belongings["Library"].shuffle()
    B.belongings["Library"].shuffle()
    return winner

def main():
    turn_count = 0
    while turn() != "Game Over":
        turn()
        turn_count+=1
    print(turn_count)
    return turn_count

main()

    

    