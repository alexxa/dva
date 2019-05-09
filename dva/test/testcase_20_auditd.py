""" This module contains testcase_20_auditd test """
from testcase import Testcase
from distutils.version import LooseVersion


class testcase_20_auditd(Testcase):
    """
    Check auditd:
    - service should be on
    - config files shoud have specified checksums
    """
    stages = ['stage1']
    applicable = {'platform': '(?i)RHEL|BETA', 'version': r'5\..*|6\..*|7\..*|8\..*'}
    tags = ['default']
    not_applicable = {'product': '(?i)ATOMIC'}

    def test(self, connection, params):
        """ Perform test """
        version = LooseVersion(params['version'])

        if version < '6.0':
            # RHEL5.x
            auditd_rules_checksum = 'f9869e1191838c461f5b9051c78a638d'
            auditd_checksum = '612ddf28c3916530d47ef56a1b1ed1ed'
            auditd_sysconf_checksum = '123beb3a97a32d96eba4f11509e39da2'
            self.ping_pong(connection, 'md5sum /etc/sysconfig/auditd  | cut -f 1 -d \' \'', auditd_sysconf_checksum)
        elif version < '7.0':
            # RHEL6.x
            auditd_rules_checksum = 'f9869e1191838c461f5b9051c78a638d'
            if '6.0' <= version <= '6.5':
                if version <= '6.1':
                    # RHEL6.0, .1
                    auditd_checksum = '612ddf28c3916530d47ef56a1b1ed1ed'
                    auditd_sysconf_checksum = '123beb3a97a32d96eba4f11509e39da2'
                else:
                    # RHEL6.2, .3, .4, .5
                    auditd_checksum = 'e1886162554c18906df2ecd258aa4794'
                    auditd_sysconf_checksum = 'd4d43637708e30418c30003e212f76fc'
            else:
                if version >= '6.9':
                    auditd_checksum = '306e13910db5267ffd9887406d43a3f7'
                    auditd_sysconf_checksum = '0825f77b49a82c5d75bcd347f30407ab'
                # RHEL6.6, ...
                else:
                    auditd_checksum = 'e1886162554c18906df2ecd258aa4794'
                    auditd_sysconf_checksum = '0825f77b49a82c5d75bcd347f30407ab'
            self.ping_pong(connection, 'md5sum /etc/sysconfig/auditd  | cut -f 1 -d \' \'', auditd_sysconf_checksum)
        elif version < '8.0':
            # RHEL7.x
            if version <= '7.2':
                auditd_checksum = 'e1886162554c18906df2ecd258aa4794'
                auditd_rules_checksum = 'd5985c09d6c150e433362eca9d59e8fe'
            elif version == '7.3':
                auditd_checksum = '643fcb75e59e330539c91678a2bb6454'
                auditd_rules_checksum = '6b6d7a773a63a2cef32341993ad66c8c'
            elif version == '7.4':
                auditd_checksum = '643fcb75e59e330539c91678a2bb6454'
                auditd_rules_checksum = 'f1c2a2ef86e5db325cd2738e4aa7df2c'
            else:
                auditd_checksum = '29f4c6cd67a4ba11395a134cf7538dbd'
                auditd_rules_checksum = 'f1c2a2ef86e5db325cd2738e4aa7df2c'
        elif version < '9.0':
            # RHEL8.x
            auditd_checksum = '7bfa16d314ddb8b96a61a7f617b8cca0'
            auditd_rules_checksum = '795528bd4c7b4131455c15d5d49991bb'
            
        self.ping_pong(connection, 'md5sum /etc/audit/auditd.conf | cut -f 1 -d \' \'', auditd_checksum)
        self.ping_pong(connection, 'md5sum /etc/audit/audit.rules | cut -f 1 -d \' \'', auditd_rules_checksum)
        return self.log
