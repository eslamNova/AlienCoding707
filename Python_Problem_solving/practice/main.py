import threading

from Worker import Worker

def main():

    thread1 = Worker()
    thread2 = Worker()
    thread3 = Worker()
    thread1.start()
    thread2.start()
    thread3.start()

if __name__ == "__main__":
    main()
