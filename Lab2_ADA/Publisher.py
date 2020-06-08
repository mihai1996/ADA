import pika
from FileUtility import FileUtility
from  Fibonacci import FibonacciCalc

class Publisher:

    def send_messages(self, message):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

        channel = connection.channel()
        channel.queue_declare(queue="hello")
        channel.basic_publish(exchange='', routing_key='hello', body=message)

        print(" [x] Sent 'Hello World!'")
        connection.close()

if __name__ == '__main__':

    f_input = r"E:\master\ADA\input.txt"
    #f_otput = "E:\\master\\ADA\\test.txt"

    test = Publisher()
    file = FileUtility()
    fib = FibonacciCalc()

    a = file.read_numbers_from_file(f_input)
    for el in a:
        test.send_messages(str(el))



