from script.message_broker.server_config import RabbitMqServerConfig
from script.message_broker.subscriber import RabbitMqServer


def _subscriber(project_id):
    server_configure = RabbitMqServerConfig(project_id)
    RabbitMqServer(server=server_configure).receiver()
