import pika
import os
from dotenv import load_dotenv
from .meta_class import Metaclass
from ..common.database_part import Mysql
from ..common.my_utils import print_error

load_dotenv()


# Server Config
class RabbitMqServerConfig(metaclass=Metaclass):
    def __init__(self, project_id=0):
        try:
            self.Mysql = Mysql()

            self.host = os.getenv("AMQP_HOST")
            self.port = os.getenv("AMQP_PORT")
            self.vhost = os.getenv("AMQP_VHOST")
            self.credentials = pika.credentials.PlainCredentials(os.getenv("AMQP_USERNAME"), os.getenv("AMQP_PASSWORD"), erase_on_connect=False)

            mq_config = self.Mysql.get_single_data_as_dict(f"select * from mq_config where project_id={project_id} and status=1")

            self.queue_name = mq_config['queue']
            self.exchange_name = mq_config['exchange']
            self.exchange_type = mq_config['exchange_type']
            self.routing_key = mq_config['route_key']
            self.project_id = project_id

            self.Mysql.close()

        except Exception as error:
            print_error(error)
