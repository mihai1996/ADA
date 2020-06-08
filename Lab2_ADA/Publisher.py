import pika
from FileUtility import FileUtility
from  Fibonacci import FibonacciCalc

class Publisher:

    def send_messages(self, message):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

        channel = connection.channel()
        channel.queue_declare(queue="hello", durable=False)
        #channel.basic_publish(exchange='', routing_key='hello', body=message)
        channel.basic_publish(
            exchange='',
            routing_key='hello',
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            ))

        #print(" [x] Sent 'Hello World!'")
        #print(" [x] Sent %r" % message)
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