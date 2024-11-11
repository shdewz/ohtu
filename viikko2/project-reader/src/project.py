class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}\n"
            f"\nAuthors:\n- {'\n- '.join(self.authors) or ''}\n"
            f"\nDependencies:\n- {'\n- '.join(self.dependencies) or ''}\n"
            f"\nDevelopment dependencies:\n- {'\n- '.join(self.dev_dependencies) or ''}\n"
        )
