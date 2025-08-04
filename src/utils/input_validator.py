def get_valid_input(prompt, min, max):
    """Get a valid integer input from the user between man and max."""
    while True:
        try:
            user_input = int(input(prompt))
            if min <= user_input <= max:
                return user_input
            else:
                print(f"Please enter a number between {min} and {max}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
