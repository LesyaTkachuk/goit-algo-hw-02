import time
from queue import Queue
from random import randint


class Client:
    def __init__(self, number):
        self.number = number


class Service:
    def __init__(self):
        self.applications = Queue()

    def generate_request(self, client: Client):
        new_application = f"Client with number {client.number} come to the window number {randint(1,10)}"
        self.applications.put(new_application)

    def process_request(self):
        if not self.applications.empty():
            application = self.applications.get()
            print(application)
            print("Processing ...")
            time.sleep(3)
            return True
        else:
            print("There is no more applications in the queue")
            return False


queue = Service()
is_processing = True

for _ in range(20):
    queue.generate_request(Client(randint(1, 100)))

while is_processing:
    is_processing = queue.process_request()
