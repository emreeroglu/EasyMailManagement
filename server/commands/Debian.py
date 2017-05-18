from fabric.api import local, put, hosts, settings, abort, cd, env, run, task, sudo, prompt
from fabric.contrib.console import confirm
#from fabric.operations import prompt


class Debian():
    def __init__(self):
        self.sh_path = '/bin/sh -l -c'
        self.bash_path = '/bin/bash -l -c'

        self.local_user = ''
        self.local_password = ''
        self.local_host = 'localhost'

        self.remote_user = ''
        self.remote_password = ''
        self.remote_host = ''
        self.root_user = 'root'

        env.user = self.remote_user
        env.password = self.remote_password
        env.hosts = []
        env.hosts.append(self.remote_host)
        env.host_string = self.remote_host
        env.abort_on_prompts = False

    def ssh_copy_id(self, identity='~/.ssh/id_rsa.pub'):
        env.shell = self.sh_path
        # Copy the key over.
        remote_path = '~/id.pub'
        put(identity, remote_path)

        with cd('~'):
            # Make sure the SSH directory is created.
            run('mkdir -p .ssh')
            # And append to the authorized keys.
            run('cat %(remote_path)s >> ~/.ssh/authorized_keys' % locals())
            # Be thourough and leave no trace of this interaction!
            run('rm %(remote_path)s' % locals())

    def install_sudo(self):
        try:
            with settings(prompts={"assword: ": self.remote_password}):
                run("su -c 'apt-get install sudo'")
        except Exception:
            print("Error")

    def add_user_to_sudoers(self):
        try:
            with settings(prompts={"assword: ": self.remote_password}):
                run("su -c 'usermod -aG sudo %s'" % self.remote_user)
        except Exception:
            print("Error")

    @staticmethod
    def update_system():
        sudo("apt-get update")

    @staticmethod
    def upgrade_system():
        sudo("apt-get dist-upgrade -y")

    @staticmethod
    def print_user():
        run('echo "%(user)s"' % env)
