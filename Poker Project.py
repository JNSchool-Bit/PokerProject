balance = 1410
yes = ("yes", "y", "yeah", "yea", "ok", "sure")
no = ("no", "n", "nah", "nope")

start_game = False

print("Welcome to the game of Poker: Texas Hold'em!")

# Ask if the player understands the rules

while True:
    answer = input("Do you know how to play Texas Hold'em? ").strip().lower()

    if answer in yes:
        print("Great! You already know the rules.")
        break

    elif answer in no:
        print("""
Here are the basic rules of Texas Hold'em!

SETUP AND BLINDS
- The game has 1 human player and 1-3 computer bots.
- Each player starts with 1410 chips.
- The small blind is 5 chips, and the big blind is 10.
- The dealer button moves clockwise after every hand.
- With 3-4 players, the two players left of the dealer
  post the small and big blinds.
- With 2 players, the dealer posts the small blind.

HOW A HAND WORKS
1. PRE-FLOP: Each player receives 2 private cards.
   The first betting round takes place.
2. FLOP: The dealer burns 1 card and reveals
   3 community cards, followed by betting.
3. TURN: The dealer burns 1 card and reveals
   1 more community card, followed by betting.
4. RIVER: The dealer burns 1 card and reveals
   the final community card, followed by betting.
5. SHOWDOWN: Remaining players compare their best
   5-card hands. The strongest hand wins the pot.
   If everyone else folds, the last player wins.

BETTING ACTIONS
- CHECK: Continue without betting when allowed.
- BET: Place the first wager of a betting round.
- CALL: Match the current bet.
- RAISE: Increase the current bet.
- FOLD: Give up your hand.

HAND RANKINGS (Strongest to Weakest)
1. Royal Flush
2. Straight Flush
3. Four of a Kind
4. Full House
5. Flush
6. Straight
7. Three of a Kind
8. Two Pair
9. One Pair
10. High Card
""")

        # Check if the player understands after reading
        while True:
            answer = input("Do you understand the rules now? ").strip().lower()

            if answer in yes:
                print("Great! Let's continue.")
                break

            elif answer in no:
                print("Please review the game manual before playing.")
                break

            else:
                print("Invalid response. Please enter yes or no.")

        break

    else:
        print("Invalid response. Please enter yes or no.")


# Ask if the player wants to start

if answer in yes:

    while True:
        ready = input("Are you ready to start the game? ").strip().lower()

        if ready in yes:
            print("Starting Texas Hold'em!")
            start_game = True
            break

        elif ready in no:
            print("No problem! Come back when you're ready.")
            break

        else:
            print("Invalid response. Please enter yes or no.")


# Begin the actual game

if start_game:
    print("Your starting balance is:", balance)
    print("Preparing the poker table...")

    # The actual poker game will go here

# PLAYER SETUP

print("\n--- PLAYER SETUP ---")

# Ask for the human player's name
while True:
    player_name = input("Enter your name: ").strip()

    if player_name != "":
        break
    else:
        print("Please enter a valid name.")


# Ask how many bots the player wants
while True:
    bot_count = input(
        "How many bots would you like to play against? (1-3): "
    ).strip()

    if bot_count == "1" or bot_count == "2" or bot_count == "3":
        bot_count = int(bot_count)
        break
    else:
        print("Invalid response. Please enter 1, 2, or 3.")


# Create a list to store all players
players = []

# Create the human player
human = {
    "name": player_name,
    "balance": 1410,
    "hand": [],
    "folded": False,
    "bot": False
}

# Add the human to the players list
players.append(human)


# Create the computer-controlled players
for i in range(bot_count):

    bot = {
        "name": "Bot " + str(i + 1),
        "balance": 1410,
        "hand": [],
        "folded": False,
        "bot": True
    }

    players.append(bot)


# Display all players at the table
print("\n--- PLAYERS AT THE TABLE ---")

for player in players:
    print(player["name"], "-", player["balance"], "chips")

print("\nThere are", len(players), "players at the table.")
print("You will be playing against", bot_count, "bot(s).")

print("\nPlayer setup complete!")
