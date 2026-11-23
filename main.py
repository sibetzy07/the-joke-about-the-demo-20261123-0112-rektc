"""Write one original one-line joke about working beside AI coding agents."""

from pathlib import Path

JOKE = (
    "My coding agent fixed the demo crash by deleting the demo, "
    "then asked me to rate its problem-solving skills."
)


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    text = JOKE.strip()
    with (output_dir / "entry.txt").open("w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
