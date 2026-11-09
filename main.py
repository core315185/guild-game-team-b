"""A tiny text adventure. Grow this world with your team!"""

ROOMS = {
    "hall": {
        "description": "You are in a quiet hall. A door leads north.",
        "exits": {"north": "garden"},
    },
    "garden": {
        "description": "You are in a garden full of strange flowers. The hall is to the south.",
        "exits": {"south": "hall"},
    },
}
ERRORS = {
    "no_exit": "You cannot go '{direction}' from here. Look at the room description for the exits.",
    "no_command": "No command has been entered. Please read the text and check for the command.",
    "error_command": "That command does not exist. Please read the text and check the command.",
}

COMMANDS = {
    "go <direction>": "move to the next room, like 'go north'",
    "quit": "exit the game",
    "help": "display available commands"
}
def main():
    current = "hall"
    print("Welcome! Type 'go <direction>' to move, or 'quit' to stop.")
    while True:
        print()
        print(ROOMS[current]["description"])
        command = input("> ").strip().lower()
        if command == "quit":
            print("Goodbye!")
            break
        if command.startswith("go "):
            direction = command[3:]
            next_room = ROOMS[current]["exits"].get(direction)
            if next_room:
                current = next_room
            else:
                print(ERRORS["no_exit"].format(direction=direction))
        elif command == "help":
            print("Available commands:")
            for cmd, description in COMMANDS.items():
                print(f"  {cmd}: {description}")
        else:
            print("No command has been entered. Please read the text and check for the command.")
    else:
        print("That command does not exist. Please read the text and check the command.")



if __name__ == "__main__":
    main()
