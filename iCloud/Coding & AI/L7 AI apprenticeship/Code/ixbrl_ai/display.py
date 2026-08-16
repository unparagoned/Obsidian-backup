from IPython.display import display, Markdown
import polars as pl


def display_markdown(x: str) -> None:
    display(Markdown(x))

def heading(heading: str, level: int=2) -> None:
    display(Markdown(f"{level * '#'} {heading}"))

def display_wide(x, rows: int=20) -> None:
    with pl.Config(tbl_rows=rows, tbl_width_chars=1_000, fmt_str_lengths=1_000):
        display(x)

