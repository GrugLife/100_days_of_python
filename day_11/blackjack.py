import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def hit_stay(player):
    move = "hit"
    while move == "hit":
        move = input("hit or stay: ")
        if move == "hit":
            player.append(random.choice(cards))
            print(player)
            if sum(player) > 21:
                if 11 in player:
                    player.remove(11)
                    player.append(1)
                else:
                    return sum(player)

    return sum(player)


def dealer_draw(dealer):
    while sum(dealer) < 17:
        dealer.append(random.choice(cards))
        print(dealer)
    return sum(dealer)


def won(player, dealer):
    if player > dealer:
        return f"You win: {player} vs {dealer}"
    elif player < dealer:
        return f"You Lose: {player} vs {dealer}"
    else:
        return f"Push: both have {player}"


def deal(cards):
    player_cards = []
    dealer_cards = []

    for n in range(2):
        player_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))

    print(f"Your hand:   {player_cards}")
    print(f"Dealer hand: {dealer_cards[0]}")

    return player_cards, dealer_cards


def main():
    player_cards, dealer_cards = deal(cards)
    if sum(player_cards) == 21:
        return "You win with a blackjack"
    elif sum(dealer_cards) == 21:
        print(dealer_cards)
        return "Dealer wins with a blackjack"

    player_score = hit_stay(player_cards)
    if player_score > 21:
        return f"You bust with a {player_score}"

    print(f"Dealer is showing: {dealer_cards}")
    dealer_score = dealer_draw(dealer_cards)
    if dealer_score > 21:
        return f"You win, dealer bust with a {dealer_score}"
    winner = won(player_score, dealer_score)

    return winner


while input("Do you want to play a game of Blackjack? Type 'y' or 'no': ") == "y":
    print(main())
