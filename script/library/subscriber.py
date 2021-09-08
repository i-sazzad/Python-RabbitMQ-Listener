#!/usr/bin/env python
import json
import pika
import time
from .data import ReadData
from ..common.my_utils import print_error_info, print_info, print_warning


class RabbitMqServer:
    # set connection
    def __init__(self, server):
        while True:
            try:
                self.server = server

                self.connection = pika.BlockingConnection(
                    pika.ConnectionParameters(self.server.host, self.server.port, self.server.vhost,
                                              self.server.credentials))
                self.channel = self.connection.channel()

                # result = self.channel.queue_declare('', exclusive=True)
                # self.queue_name = result.method.queue

                # self.channel.queue_declare(self.server.queue_name, durable=True) self.channel.queue_bind(
                # exchange=self.server.exchange_name, queue=self.server.queue_name,
                # routing_key=self.server.routing_key) self.channel.exchange_declare(
                # exchange=self.server.exchange_name, exchange_type=self.server.exchange_type, durable=True)
                break

            except Exception as error:
                time.sleep(60)
                print('Connection closed')
                print_warning('Connection closed')
                print_error_info(error)

    def receiver(self):
        while True:
            try:
                print('[' + self.server.queue_name + '] Waiting for data. To exit press CTRL+C')

                self.channel.basic_qos(prefetch_count=1)
                self.channel.basic_consume(
                    queue=self.server.queue_name,
                    on_message_callback=self.callback,
                    auto_ack=True
                )

                self.channel.start_consuming()

            except Exception as error:
                print_error_info(error)
                self.__init__(self.server)

    def callback(self, ch, method, properties, payload):
        print("Data received")
        print_info("Data received")

        raw_data = json.loads(payload)
        project_id = self.server.project_id

        ReadData().read_data(project_id, raw_data)
