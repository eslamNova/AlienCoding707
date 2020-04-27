import threading

class Worker(threading.Thread):

    def __init__(self):
        super(Worker, self).__init__()

    def run(self):
        for i in range(10):
            print(i)