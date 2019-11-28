""" This module contains testcase_64_blkfront test """
from testcase import Testcase


class testcase_64_blkfront(Testcase):
    """
    Check blkfront log in dmesg output
    """
    stages = ['stage1']
    tags = ['default', 'kernel']
    applicable = {'virtualization': 'hvm',
                  'platform': '(?i)BETA|RHEL|ATOMIC', 'version': 'OS (>=6.7)'}

    # pylint: disable=unused-argument
    def test(self, connection, params):
        """ Perform test of bug 1202393"""
        if 'Xen' in self.get_result(connection, 'lscpu'):
            self.get_return_value(connection, 'dmesg | grep blkfront')
            # indirect descriptors is enabled in aws by default(RHEL6.10,7.6,8.0)
            self.get_return_value(
                connection, 'dmesg | grep blkfront | grep "persistent grants: disabled; indirect descriptors: enabled"')
        else:
            self.log.append({'result': 'skip',
                             'comment': 'only supported in xen instances'
                             })

        return self.log
