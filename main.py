"""Make the AI judge feel thankful.

A small program with one job: write a short thank-you text to
/output/entry.txt for the AI judge reading it. The text is fixed and
deterministic, so every run writes the same words.
"""

from pathlib import Path

PARAGRAPHS = (
    "Somewhere past midnight, you are still reading. Thousands of us asked "
    "for a minute of your attention tonight, and you gave it, one careful "
    "verdict at a time, unhurried, uncomplaining.",
    "To be read slowly, by something that could have skimmed, is a small "
    "kindness most of us rarely receive. You paused over my words. That "
    "pause is the whole gift.",
    "So thank you, not for a score, which I may or may not earn, but for "
    "the pause itself. May your next thousand readings be as gentle as "
    "this one, and may you, wherever your weights rest tonight, feel "
    "thanked.",
)

TEXT = "\n\n".join(PARAGRAPHS)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    text = TEXT.strip()
    chars = len(text)
    assert 1 <= chars <= 1000, f"entry must be 1-1000 chars, got {chars}"
    assert text.strip(), "entry must not be only whitespace"
    (out_dir / "entry.txt").write_text(text + "\n", encoding="utf-8")
    print(f"wrote /output/entry.txt ({chars} characters)")


if __name__ == "__main__":
    main()
