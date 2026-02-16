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
                print("bust, you lose")
                return "BUST!"

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
    # 1. deal cards to player and dealer

    player_cards = []
    dealer_cards = []

    n = 0
    while n < 4:
        player_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))
        n += 2

    # 1.5 show cards after deal
    print(player_cards)
    print(dealer_cards[0])

    player_score = hit_stay(player_cards)
    dealer_score = dealer_draw(dealer_cards)
    winner = won(player_score, dealer_score)

    print(winner)


deal(cards)


# 2. calc score for player


# 3. ask to hit or stay


# 4. if hit, deal another card and cal score

# 5. if stay, move to dealers score

# 6. if dealer <17, deal a card

# 7. see who wins
