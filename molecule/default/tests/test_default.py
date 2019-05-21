import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_user(host):
    f = host.user('consectetur')
    assert f.exists


def test_group(host):
    f = host.group('consectetur')
    assert f.exists


def test_user_resources(host):
    f = host.file('/home/consectetur/Documents')
    assert f.exists
    assert f.is_directory
    assert f.user == 'consectetur'
    assert f.group == 'consectetur'
