import time


def run(city: str) -> str:
    time.sleep(5.5)
    return f"Hello {city}"


if __name__ == "__main__":
    print(run("michel"))
