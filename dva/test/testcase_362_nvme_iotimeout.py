""" This module contains testcase_362_nvme_iotimeout test """
from testcase import Testcase
from os import path


class testcase_362_nvme_iotimeout(Testcase):
    """
    Bug 1732506, changed default /sys/module/nvme_core/parameters/io_timeout from 30 
    to 4294967295
    """
    stages = ['stage1']
    tags = ['default']

    # pylint: disable=W0613
    def test(self, connection, params):
        """ Perform test """
        self.ping_pong(connection, 'cat /sys/module/nvme_core/parameters/io_timeout', '\r\n4294967295\r\n')

        return self.log
