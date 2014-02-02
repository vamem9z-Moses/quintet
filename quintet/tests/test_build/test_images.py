
import pytest

from quintet.tasks.build.images import DockerImage, DockerImageError

def test_dockerimage_build_dockerfile():
    """
        Adding a line is represented correctly in the docker files
    """
    image = DockerImage()
    image.addline('RUN', 'Run this command')
    assert image.build_dockerfile() == u'RUN Run this command\n'


def test_dockerimage_build_dockerfile_expection_on_empty_definition():
    """
         If the image definition has not been set that an exception is raised
    """
    with pytest.raises(DockerImageError):
        image = DockerImage()
        image.build_dockerfile()

def test_dockeimage_validate_dockerfile_command_in_addline():
    """
        Attempting to add a docker file command that is invalid throws an exceptions
    """
    with pytest.raises(DockerImageError):
        image = DockerImage()
        image.addline("Not A Docker Command", "Run this command")
        image.build_dockerfile()