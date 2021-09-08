from .operation import insert_operation
from .for_each_api import start_execution
from .sql_to_mongo.for_each_month import project_for_a_month
from ..common.database_part import Mysql
from ..common.my_utils import get_error_message, print_error_info, print_info, print_warning


class ReadData:
    # set connection
    def __init__(self):
        try:
            self.Mysql = Mysql()
        except Exception as error:
            print_error_info(error)

    def read_data(self, project_id, raw_data):
        data = raw_data['data']['response']
        # Execution
        self.Mysql.close()
