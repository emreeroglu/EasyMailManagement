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

    def ssh_copy_id(self, identity='~/.ssh/id_rsa.pub', user_name='~'):
        env.shell = self.sh_path
        # Create .ssh directory
        run('mkdir -p /home/%s/.ssh' % user_name)
        # Fix permissions
        run("chown %(user_name)s:%(user_name)s /home/%(user_name)s/.ssh" % {'user_name':user_name})
        run("chmod 700 /home/%s/.ssh" % user_name)
        # Copy the key over.
        remote_path = ('/home/%s/.ssh/authorized_keys' % user_name)
        put(identity, remote_path)
        # Fix permissions
        run("chmod 600 /home/%s/.ssh/authorized_keys" % user_name)
        run("chown %(user_name)s:%(user_name)s /home/%(user_name)s/.ssh/authorized_keys" % {'user_name':user_name})

    '''def install_sudo(self):
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
            print("Error")'''

    @staticmethod
    def update_system_as_user():
        sudo("apt-get update")

    @staticmethod
    def upgrade_system_as_user():
        sudo("apt-get dist-upgrade -y")

    @staticmethod
    def print_user():
        run('echo "%(user)s"' % env)

    @staticmethod
    def add_user_as_root(user_name, password):
        try:
            with settings(prompts={"assword: ": password}):
                run("useradd %s" % user_name)
                run("passwd %s" % user_name)
                run("mkdir /home/emre")
        except Exception:
            print("Error when creating user %s passsword." % user_name)

    @staticmethod
    def update_system_as_root():
        run("apt-get update")

    @staticmethod
    def upgrade_system_as_root():
        run("apt-get dist-upgrade -y")

    @staticmethod
    def install_sudo_as_root():
        run("apt-get install sudo")

    @staticmethod
    def add_user_to_sudoers_as_root(user_name, password):
        try:
            with settings(prompts={"assword: ": password}):
                run("usermod -aG sudo %s" % user_name)
        except Exception:
            print("Error when adding user %s to sudoers." % user_name)

    @staticmethod
    def disable_root_login():
        sudo("sed -i 's/PermitRootLogin yes/PermitRootLogin no/g' /etc/ssh/sshd_config")

    @staticmethod
    def reload_ssh():
        sudo("systemctl restart ssh")
