from cards import Deck

def deal_cards():
    deck = Deck()

    dealer_hand = []
    player_hand = []

    dealer_card = deck.draw()
    dealer_card.facing = "down"
    dealer_hand.append(dealer_card)

    player_hand.append(deck.draw())
    dealer_hand.append(deck.draw())
    player_hand.append(deck.draw())

    draw_table(dealer_hand, player_hand)

    while True:
        command = raw_input("What would you like to do? [s]tay, [h]it...")

        if command in ["hit", "h"]:
            player_hand.append(deck.draw())

            if calculate_total(player_hand) > 21:
                draw_table(dealer_hand, player_hand)
                print ""
                print "   YOU BUSTED  "
                print
                return

            else:
                draw_table(dealer_hand, player_hand)
                continue


        if command in ["stay", "s"]:
            pass




def draw_table(dealer_hand, player_hand):
    print "========================================"
    print "========================================"
    print "  Dealer has ", calculate_total(dealer_hand)
    for card in dealer_hand:
        print "    ", card
    print
    print " ~ ~ ~ ~ ~ ~ ~ ~ "
    print
    print "  Player has ", calculate_total(player_hand)
    for card in player_hand:
        print "    ", card
    print "========================================"
    print "========================================"


def calculate_total(hand):
    total = 0
    for card in hand:
        try:
            total += int(card.rank)
        except:
            if card.rank in ["jack", "queen", "king"]:
                total += 10
            elif card.rank == "ace":
                pass  # TODO

    return total


if __name__ == '__main__':
    deal_cards()