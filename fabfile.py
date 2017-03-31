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
        # And append to the authrized keys.
        run('cat %(REMOTE_PATH)s >> ~/.ssh/authorized_keys' % locals())
        # Be thourough and leave no trace of this interaction!
        run('rm %(REMOTE_PATH)s' % locals())


def install_sudo():
    print("dememe0")
    try:
        deneme = 'dene'
        with settings(prompts={deneme: ""}):
            print("dememe1")
            test = prompt(deneme)
            print("dememe2")
            print(test)
            run("su -")
            run("apt-get install sudo")
    except SystemExit:
        print("Error")


def switch_user(user_name):
    run("su - %s" % user_name)


def update_system():
    sudo("apt-get update")


def print_user():
    run('echo "%(user)s"' % env)

install_sudo()