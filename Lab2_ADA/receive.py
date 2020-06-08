import pika
from  Fibonacci import FibonacciCalc
from FileUtility import FileUtility
import time
f = FileUtility()
fib = FibonacciCalc()

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()
channel.queue_declare(queue="hello", durable=False)

def callback(ch, method, properties, body):
    n = list()
    f_otput = "E:\\master\\ADA\\output.txt"
    num = int(body)
    #element = fib.busy_fibonacci(num)
    print(" [x] Received %r" % num)
    time.sleep(body.count(b'.'))
    element = fib.busy_fibonacci(num)
    f.write_numbers_in_file(f_otput, element)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=2)

channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
