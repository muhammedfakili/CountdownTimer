import time

def countdown_timer (seconds):
    while seconds > 0:
        print(f"time reaming: {seconds} seconds")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")


def main():
    try:
        seconds = int(input("Enter the countdown time in seceonds: "))
        countdown_timer(seconds)
    except ValueError:
        print("Invaild input. Please enter a vaild number of seconds.")

if __name__ == "__main__":
    main()