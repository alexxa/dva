from testcase import Testcase


class testcase_70_ena(Testcase):
    """
    Check that the network driver is ena
    """
    stages = ['stage1']
    tags = ['default']
    applicable = {"platform": "(?i)RHEL|BETA", "version": "OS (>=7.4)",  'cloudhwname': 'm4.16xlarge|x1.16xlarge|m5.xlarge'}
    not_applicable = {'product': '(?i)ATOMIC'}

    # pylint: disable=unused-argument
    def test(self, connection, params):
        self.get_return_value(connection, 'ethtool -i eth0 | grep "driver: ena"')
        return self.log
