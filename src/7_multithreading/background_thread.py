import threading


def background_callable(name: str, age: int) -> None:
    # simulate taking some time within the background callable
    for i in range(999999999):
        continue
    print(f"{name} is {age} years old")


if __name__ == "__main__":
    print("main thread begins")
    # Create a background thread that runs in the background
    background_thread: threading.Thread = threading.Thread(
        target=background_callable, args=("Jason", 10)
    )
    background_thread.start()
    # Ensure that background thread ends before main thread ends
    background_thread.join()
    print("end of background thread")
