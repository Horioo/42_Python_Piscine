import time
import os
import sys


def ft_tqdm(lst: range) -> None:
    """
    Reproduction of the tqdm function

    This function yields each element from the iterable `lst`
    and prints a progress bar on the terminal line

    The bar updates every `mininterval` seconds or on the last iteration
    The size dynamically adapts to the terminal width to prevent wrapping
    The speed is capped to avoid unrealistic values

    Args:
        lst(iterable): An iterable (e.g, range, list)

    Yields:
        item: each element from `lst` in original order

    Notes:
        - The bar adjusts to terminal width
        - The function doesnt return a value;
    """
    try:
        start = time.perf_counter()
        total = len(lst)

        terminal_width = os.get_terminal_size().columns + 2
        reserved = 5 + (len(str(total)) * 2 + 1) + 30
        bar_size = max(10, terminal_width - reserved)

        last_print_time = start
        mininterval = 0.1

        for i, item in enumerate(lst, 1):
            progress = i / total

            elapsed_time = time.perf_counter() - start
            velocity = i / max(elapsed_time, 0.01)
            velocity = min(velocity, 999.99)
            eta = (total - i) / velocity

            filled = int(progress * bar_size)
            bar = "█" * filled + ' ' * (bar_size - filled)

            percent = int(progress * 100)

            minutes = int(elapsed_time // 60)
            seconds = int(elapsed_time % 60)
            remaining_minutes = int(eta // 60)
            remaining_seconds = int(eta % 60)

            velocity_str = f"{velocity:6.2f}"

            now = time.perf_counter()
            if now - last_print_time >= mininterval or i == total:
                line = (
                    f"\r{percent:3d}%|{bar}| {i:3d}/{total} "
                    f"[{minutes:02}:{seconds:02}"
                    f"<{remaining_minutes:02}:{remaining_seconds:02}, "
                    f"{velocity_str}it/s]"
                    )
                line = line[:terminal_width - 1]
                sys.stdout.write(line)
                sys.stdout.flush()
                last_print_time = now
            yield item

    except TypeError:
        total = None
        print()


def main():
    print()


if __name__ == "__main__":
    main()
