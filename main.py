import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def total_score(cards):
    if sum(cards) == 21 and len(cards)== 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        print("Draw 🙃")
    elif user_score == 0:
        print("You Win! 😎")
    elif computer_score == 0:
        print("You lose 😭")
    elif user_score > 21:
        print("You lose 😭")
    elif computer_score > 21:
        print("You Win! 😎")
    elif user_score > computer_score:
        print("You Win! 😎")
    else:
        print("You lose 😭")


def play_game():
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    game_over = False

    for _ in range(2):
        new_card = deal_card()
        user_cards.append(new_card)
        computer_cards.append(new_card)
    while not game_over:
        from art import logo
        print(logo)
        user_score = total_score(user_cards)
        computer_score = (total_score(computer_cards))
        print(f"Your Cards: {user_cards}, Your Score: {user_score}")
        print(f"Computer cards: {computer_cards}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user = input("Do you want to play blackjack> Type 'yes' or 'no': ")
            if user == "yes":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = (total_score(computer_cards))

    print(f"Your final cards: {user_cards}, Final Score = {user_score}")
    print(f"Computer final cards: {computer_cards}, Final Score = {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play blackjack> Type 'yes' or 'no': ") == 'yes':
    print("\n" * 20)
    play_game()
