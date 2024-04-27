import curses
from curses import wrapper
from typingtest import TypingTest
from openai_text import get_text


def main(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the typing speed test")
    stdscr.addstr("\nWhat do you want to type about? ")
    stdscr.refresh()

    # Enable echo to make the user's input visible
    curses.echo()
    theme = stdscr.getstr().decode()
    # Disable echo after getting the user input
    curses.noecho()

    text = get_text(theme)

    # Split the text into lines
    lines = text.split("\n")

    while True:
        for line in lines:
            typing_test = TypingTest(stdscr, line, theme)
            stdscr.getkey()
            typing_test.test_wpm()
            stdscr.clear()
            stdscr.addstr(0, 0, f"Theme: {theme}", curses.color_pair(3))
            stdscr.addstr(1, 0, "")  # Add an empty line
            stdscr.addstr(2, 0, "Press any key to continue...")
            stdscr.refresh()
            stdscr.getkey()

        stdscr.addstr(2, 0, "Congratulations! You have completed the test!")
        stdscr.addstr(3, 0, "Press 'Esc' to exit or any other key to restart...")
        stdscr.refresh()
        key = stdscr.getkey()

        # Check if the key is a single character before using ord()
        if isinstance(key, str) and len(key) == 1:
            if ord(key) == 27:  # ASCII value for ESC
                break
        else:
            # Restart the test
            stdscr.clear()


if __name__ == "__main__":
    wrapper(main)
