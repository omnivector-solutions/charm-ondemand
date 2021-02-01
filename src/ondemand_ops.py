import subprocess
import logging
import docker
import os

class OnDemandOps:

    def __init__(self) -> None:
        self.name = "OpenOnDemandOps"

    def setup_docker(self):

        # check whether docker has been already installed
        try:

            subprocess.call(["docker", "version"])

        except Exception as e:

            subprocess.call(["sh", os.path.join("scripts", "get-docker.sh")])

            pass

    def setup_ondemand(self):

        client = docker.from_env()

        client.container.run(
            image="ohiosupercomputer/ood",
            auto_remove=False,
            name="ood",
            detach=True,
            ports={
                "5556/tcp": 5556,
                "8080/tcp": 8080
            }
        )

        pass