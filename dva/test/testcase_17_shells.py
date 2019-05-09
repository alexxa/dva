""" This module contains testcase_17_shells test """
from testcase import Testcase
from distutils.version import LooseVersion

class testcase_17_shells(Testcase):
    """
    Check for bash/nologin shells in /etc/shells
    """
    stages = ['stage1']
    tags = ['default']

    # pylint: disable=W0613
    def test(self, connection, params):
        """ Perform test """
        version = LooseVersion(params['version'])
        
        self.get_return_value(connection, 'grep \'bin/bash$\' /etc/shells')
        if version < '7.6':
            self.get_return_value(connection, 'grep \'bin/nologin$\' /etc/shells')
        return self.log
