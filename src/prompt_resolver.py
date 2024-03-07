from liquid import BoundTemplate, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader(""))


class Prompt:

    def __init__(self, filename: str, body: str):
        self.name = filename
        self.body = body


class PromptResolver:

    def __init__(self):
        pass

    @staticmethod
    def find(filename: str) -> BoundTemplate:
        return env.get_template(filename)

    def make_prompt(self, filename: str, **kwargs) -> Prompt:

        text = self.render(filename, **kwargs)
        prompt = Prompt(filename=filename, body=text)

        return prompt

    def render(self, filename: str, **kwargs) -> str:
        template = self.find(filename)
        return template.render(**kwargs)
