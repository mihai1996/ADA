import pika
from  Fibonacci import FibonacciCalc
from FileUtility import FileUtility
f = FileUtility()
fib = FibonacciCalc()

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()
channel.queue_declare(queue="hello")

def callback(ch, method, properties, body):
    #n = list()
    f_otput = "E:\\master\\ADA\\test.txt"
    num = int(body)
    #element = fib.busy_fibonacci(num)
    print(" [x] Received %r" % num)
    element = fib.busy_fibonacci(num)
    f.write_numbers_in_file(f_otput, element)




channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
