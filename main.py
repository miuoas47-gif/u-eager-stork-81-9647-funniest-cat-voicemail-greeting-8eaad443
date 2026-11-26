#!/usr/bin/env python3
"""The funniest voicemail greeting a cat would record.

Deterministic: prints exactly one line, every time, with no
time, randomness, or network involved.
"""

GREETING = (
    "You've reached Whiskers. I can't come to the phone right now "
    "\u2014 I'm sitting on it. Leave a message after the beep "
    "and I'll knock it off the table."
)


def main():
    print(GREETING)


if __name__ == "__main__":
    main()
