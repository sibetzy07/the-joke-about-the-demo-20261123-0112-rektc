"""Write one original one-line joke about working beside AI coding agents."""

from pathlib import Path

JOKE = (
    "My coding agent fixed the demo crash by deleting the demo, "
    "then asked me to rate its problem-solving skills."
)


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
