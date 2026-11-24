balance = 1410
game1 =
yes = ("yes", "y", "yeah", "yea", "ok")
no = ("no", "na", "n")

answer = input("Welcome to the game of Poker: Texas Hold'em! Do you know how to play this game? ").strip().lower()
if answer in no:
    start = input("""That's ok. Here are the basic rules: 
Setup and Blinds
• Players and deck: Typically played with 2 to 10 players using a standard 52-card deck.
• Dealer button: A dealer marker rotates clockwise after every hand to show dealing order and betting position.
• Blinds: Before cards are dealt, the player immediately left of the dealer posts the small blind (usually half the minimum bet) 
and the next player left posts the big blind (the full minimum bet) to seed the pot.

How a Hand Plays Out
1. Pre-flop: Every player gets two face-down hole cards. Betting starts with the player to the left of the big blind and moves clockwise.
2. The flop: Three community cards are dealt face up. Betting starts with the first active player left of the dealer button.
3. The turn: A fourth community card is dealt face up, followed by another round of betting.
4. The river: The fifth and final community card is dealt face up, followed by the last betting round.
5. Showdown: If two or more players remain after the river betting round, remaining players reveal their hole cards and the highest five-card 
hand wins the pot (split evenly on a tie). If everyone else folds at any point, the last player standing wins without showing their cards.

Betting Actions
• Check: Pass the action without betting when no bet has been made in the current round.
• Bet: Place the first wager in a betting round.
• Call: Match the current highest bet.
• Raise: Increase the current bet (opponents must match or raise again to stay in).
• Fold: Give up your cards and forfeit any chips already put in the pot.

Hand Rankings (Strongest to Weakest)
• Royal / Straight flush: Five consecutive cards of the same suit (ace-high straight flush is a royal flush).
• Four of a kind: Four cards of the same rank.
• Full house: Three of a kind plus a pair.
• Flush: Any five cards of the same suit, not in sequence.
• Straight: Five consecutive cards of mixed suits.
• Three of a kind: Three cards of the same rank.
• Two pair: Two different pairs.
• One pair: Two cards of the same rank.
• High card: No matching ranks or flush/straight; highest card plays (ace is high).

Do you know understand how to play the game? """).strip().lower()
    if answer in no:
        print("Please read the game manual provided, or search online. Once you understand, please restart game.")
        #loop statement, skip to line 44 or 4?
else:
    start = input("Great! Should we start the game? ").strip.lower()
    if answer in no:
        print("Ok. Please restart the game when ready.")
    else:

