import subprocess
import logging
import docker
import os

class OnDemandOps:

    def __init__(self) -> None:
        self.name = "OpenOnDemandOps"

    def install_deps(self):
        """
        Utility method to install needed dependencies for running
        (docker)[https://pypi.org/project/docker/]
        """

        subprocess.call(["apt", "update"])

        subprocess.call([
            "apt", "install", "-y"
            "python3-distutils"
        ])

        # change permissions of the folder, so we can move
        # python3-distutils to that folder
        subprocess.call([
            "chmod", "ugo+w",
            "/var/lib/juju/agents/unit-ondemand-9/charm/venv/"
        ])

        subprocess.call([
            "cp", "-r",
            "/usr/lib/python3.7/distutils",
            "/var/lib/juju/agents/unit-ondemand-9/charm/venv/"
        ])

    def setup_docker(self):
        """
        Utility method to install and setup [docker](https://www.docker.com/)
        """

        # check whether docker has been already installed
        try:

            subprocess.call(["docker", "version"])

        except Exception as e:

            # install docker via bash script
            subprocess.call(["sh", os.path.join("scripts", "get-docker.sh")])

            pass

    def setup_ondemand(self):
        """
        Utility method to start ondemand container
        """

        client = docker.from_env()

        client.images.pull("ohiosupercomputer/ood")

        client.containers.run(
            image="ohiosupercomputer/ood",
            auto_remove=False,
            name="ood",
            detach=True,
            ports={
                "5556/tcp": 5556,
                "8080/tcp": 8080
            }
        )