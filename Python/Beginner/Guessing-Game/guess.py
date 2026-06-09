import random
import time


def choose_difficulty():
    """Choose game difficulty."""

    while True:

        print("\n=== Difficulty Levels ===")
        print("1. Easy   (1-50, 10 guesses)")
        print("2. Medium (1-100, 5 guesses)")
        print("3. Hard   (1-500, 3 guesses)")

        choice = input("Choose difficulty (1-3): ")

        if choice == "1":
            return 50, 10

        elif choice == "2":
            return 100, 5

        elif choice == "3":
            return 500, 3

        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


def get_guess(max_number):
    """Validate user input."""

    while True:

        user_input = input(
            f"\nGuess the number (1-{max_number})\n"
            f"Enter -1 for cheat mode\n"
            f"Enter q to quit\n"
            f"Your guess: "
        ).lower()

        if user_input == "q":
            return "quit"

        if user_input == "-1":
            return -1

        try:
            guess = int(user_input)

            if 1 <= guess <= max_number:
                return guess

            print(f"Please enter a number between 1 and {max_number}.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def play_game():
    """Play one round of the game."""

    max_number, guesses_left = choose_difficulty()

    number = random.randint(1, max_number)

    start_time = time.time()
    paused_time = 0

    while guesses_left > 0:

        guess = get_guess(max_number)

        # Quit game
        if guess == "quit":
            print("You quit the game.")
            return None

        # Cheat mode
        if guess == -1:

            pause_start = time.time()

            print("\n=== CHEAT MODE ACTIVATED ===")
            print(f"The secret number is: {number}")

            input("Press Enter to continue...")

            pause_end = time.time()

            paused_time += pause_end - pause_start

            continue

        # Correct guess
        if guess == number:

            finish_time = time.time()

            elapsed_time = round(
                finish_time - start_time - paused_time,
                2
            )

            score = (guesses_left * 10)

            print("\n🏆 Congratulations!")
            print(f"You guessed the number: {number}")
            print(f"Time: {elapsed_time} seconds")
            print(f"Round Score: {score}")

            return score

        # Wrong guess
        guesses_left -= 1

        if guess < number:
            print("Higher ↑")
        else:
            print("Lower ↓")

        if guesses_left > 0:

            if guesses_left == 1:
                print("You have 1 guess left.")
            else:
                print(f"You have {guesses_left} guesses left.")

    print(f"\n❌ Game Over! The number was {number}")
    return 0


def main():

    total_score = 0

    print("🎯 Welcome to the Number Guessing Game!")

    while True:

        result = play_game()

        if result is None:
            break

        total_score += result

        print(f"\n⭐ Total Score: {total_score}")

        play_again = input(
            "\nDo you want to play again? (yes/no): "
        ).lower()

        if play_again not in ["yes", "y"]:
            break

    print("\nThanks for playing!")
    print(f"Final Score: {total_score}")


main()