""" This module contains testcase_36_3_cmdline_crashkernel test """
from testcase import Testcase


class testcase_36_3_cmdline_crashkernel(Testcase):
    """
    should not load nouveau in EC2 instances
    """
    stages = ['stage1']
    applicable = {'virtualization': 'hvm'}
    tags = ['default']

    # pylint: disable=W0613
    def test(self, connection, params):
        """ Perform test """

        self.get_return_value(connection, 'grep \'crashkernel=auto\' /proc/cmdline')
        return self.log
