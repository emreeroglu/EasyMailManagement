from fabric.api import local, put, hosts, settings, abort, cd, env, run, task, sudo, prompt
from fabric.contrib.console import confirm
#from fabric.operations import prompt


sh_path = '/bin/sh -l -c'
bash_path = '/bin/bash'

local_user = ''
local_password = ''
local_host = 'localhost'

remote_user = ''
remote_password = ''
remote_host = ''
root_user = ''

env.user = remote_user
env.password = remote_password
env.hosts = []
env.hosts.append(remote_host)
env.host_string = remote_host
env.abort_on_prompts = False


def ssh_copy_id(identity='~/.ssh/id_rsa.pub'):
    env.shell = sh_path
    # Copy the key over.
    REMOTE_PATH = '~/id.pub'
    put(identity, REMOTE_PATH)

    with cd('~'):
        # Make sure the SSH directory is created.
        run('mkdir -p .ssh')
        # And append to the authorized keys.
        run('cat %(REMOTE_PATH)s >> ~/.ssh/authorized_keys' % locals())
        # Be thourough and leave no trace of this interaction!
        run('rm %(REMOTE_PATH)s' % locals())


def install_sudo():
    try:
        with settings(prompts={"assword: ": remote_password}):
            run("su -c 'apt-get install sudo'")
    except Exception:
        print("Error")


def add_user_to_sudoers():
    try:
        with settings(prompts={"assword: ": remote_password}):
            run("su -c 'usermod -aG sudo %s'" % remote_user)
    except Exception:
        print("Error")


def switch_user(user_name):
    run("su - %s" % user_name)


def update_system():
    sudo("apt-get update")


def upgrade_system():
    sudo("apt-get dist-upgrade -y")


def print_user():
    run('echo "%(user)s"' % env)
