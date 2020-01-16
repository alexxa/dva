""" This module contains testcase_362_nvme_iotimeout test """
from testcase import Testcase
from os import path


class testcase_101_chrony_aws(Testcase):
    """
    Bug 1679763, [RFE] AWS AMI - Add Amazon Timesync Service
    """
    stages = ['stage1']
    tags = ['default']
    applicable = {'cloudhwname': 't3.large|m5.large|m5.xlarge', "version": "OS (>=7.7)"}
    not_applicable = {'product': '(?i)ATOMIC'}

    # pylint: disable=W0613
    def test(self, connection, params):
        """ Perform test """
        self.get_result(connection, 'cat /etc/chrony.conf', timeout=20)
        self.get_return_value(connection, 'grep \'server 169.254.169.123\' /etc/chrony.conf')
        return self.log
