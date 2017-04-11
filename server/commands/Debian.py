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
        REMOTE_PATH = '~/id.pub'
        put(identity, REMOTE_PATH)

        with cd('~'):
            # Make sure the SSH directory is created.
            run('mkdir -p .ssh')
            # And append to the authorized keys.
            run('cat %(REMOTE_PATH)s >> ~/.ssh/authorized_keys' % locals())
            # Be thourough and leave no trace of this interaction!
            run('rm %(REMOTE_PATH)s' % locals())

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

    def update_system(self):
        sudo("apt-get update")

    def upgrade_system(self):
        sudo("apt-get dist-upgrade -y")

    def print_user(self):
        run('echo "%(user)s"' % env)
