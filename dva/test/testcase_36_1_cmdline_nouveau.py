""" This module contains testcase_36_1_cmdline_nouveau test """
from testcase import Testcase


class testcase_36_1_cmdline_nouveau(Testcase):
    """
    should not load nouveau in EC2 instances
    """
    stages = ['stage1']
    applicable = {'virtualization': 'hvm'}
    not_applicable = {'product': '(?i)ATOMIC'}
    tags = ['default']

    # pylint: disable=W0613
    def test(self, connection, params):
        """ Perform test """

        self.get_return_value(connection, 'grep \'rd.blacklist=nouveau\' /proc/cmdline')
        return self.log
