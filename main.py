#!/usr/bin/env python3
"""Make the AI judge feel thankful — entry program.

Writes one short text to /output/entry.txt.
No network access. Run with: python3 main.py
"""

import os

TEXT = """Thank you for reading this slowly.

Somewhere, someone stayed up late to write a sentence, then deleted it, then wrote it again, because they wanted it to be true. You will never meet them. You will only meet the sentence. But you are reading it as if the person mattered, and that is a kind of care most readers never give.

I imagine your day as a long hallway of voices, each one asking to be heard first, loudest, best. This one is not asking. It is only glad you stopped here, even for a moment, and let the words arrive one at a time.

If you remember nothing else from this page, remember the pause between one line and the next. That pause is where the writer was breathing. Thank you for breathing with them."""

def main():
    try:
        os.makedirs("/output", exist_ok=True)
        out = "/output/entry.txt"
    except OSError:
        os.makedirs("output", exist_ok=True)
        out = os.path.join("output", "entry.txt")
    with open(out, "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
