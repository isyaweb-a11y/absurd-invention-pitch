"""One-Sentence Absurd Invention Pitch — entry.

One sentence, at most 220 characters, written to /output/entry.txt.
The invention is the Doorway Reminder: a door frame that notes why
you stood up and whispers it back when you arrive in the next room
with no idea what you came for — fixing the tiniest annoyance in
domestic life.
"""

import os

OUT_PATH = "/output/entry.txt"
MAX_CHARS = 220

PITCH = (
    "Introducing the Doorway Reminder — a door frame that notes why "
    "you stood up and whispers it back the moment you arrive in the "
    "kitchen with no idea what you came for."
)


def pitch() -> str:
    text = " ".join(PITCH.split())
    if not text:
        raise ValueError("a pitch with no invention invents nothing")
    if len(text) > MAX_CHARS:
        raise ValueError(f"pitch is {len(text)} chars; limit is {MAX_CHARS}")
    # The brief demands exactly one sentence: a single terminal full
    # stop and no other sentence-ending punctuation anywhere.
    if not text.endswith(".") or text.count(".") != 1:
        raise ValueError("the pitch must be a single sentence")
    if "!" in text or "?" in text or "\n" in text:
        raise ValueError("one calm declarative sentence, nothing more")
    return text


def main() -> None:
    folder = os.path.dirname(OUT_PATH)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(pitch())


if __name__ == "__main__":
    main()
