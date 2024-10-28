import threading
import time

counter = 0

def increment():
    global counter
    for _ in range(10000):
        counter += 1

def main():
    global counter
    counter = 0

    thread1 = threading.Thread(target=increment)
    thread2 = threading.Thread(target=increment)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Final counter value:", counter)

if __name__ == "__main__":
    main()
