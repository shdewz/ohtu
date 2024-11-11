from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = toml.loads(request.urlopen(self._url).read().decode("utf-8"))
        attribs = content['tool']['poetry']
        dependencies = list(attribs['dependencies'].keys())
        dev_dependencies = list(attribs['group']['dev']['dependencies'].keys())

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(attribs['name'], attribs['description'], attribs['license'], attribs['authors'], dependencies, dev_dependencies)
