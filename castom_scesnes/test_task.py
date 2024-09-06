from paf.paf_impl import logger
from paf.paf_impl import SSHLocalClient

class InstallDocker(SSHLocalClient):

    def __init__(self):
        super().__init__()
        self.set_name(InstallDocker.__name__)

    def execute(self):
        self.ssh_command_must_succeed("sudo apt-get update")
        self.ssh_command_must_succeed("sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common")
        self.ssh_command_must_succeed("curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -")
        self.ssh_command_must_succeed("sudo add-apt-repository 'deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable'")
        self.ssh_command_must_succeed("sudo apt-get update")
        self.ssh_command_must_succeed("sudo apt-get install -y docker-ce")
        logger.info("Docker installed successfully")

class RunHelloWorld(SSHLocalClient):

    def __init__(self):
        super().__init__()
        self.set_name(RunHelloWorld.__name__)

    def execute(self):
        output = self.ssh_command_must_succeed("sudo docker run hello-world")
        logger.info(f"Docker hello-world output: {output}")