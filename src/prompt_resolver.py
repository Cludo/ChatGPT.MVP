from liquid import BoundTemplate, Environment, FileSystemLoader

# configure Liquid environment
env = Environment(loader=FileSystemLoader(""))


class Prompt:
    """Prompt class to hold prompt information."""

    def __init__(self, filename: str, body: str):
        """
        Initializes a Prompt object.

        :param filename: filepath to the prompt template
        :param body: the text of the prompt
        """
        self.name = filename
        self.body = body


class PromptResolver:
    """PromptResolver class to resolve prompts from Liquid templates."""

    def __init__(self):
        pass

    @staticmethod
    def find(filename: str) -> BoundTemplate:
        """
        Load a Liquid template from a file.

        :param filename: filepath to the template
        :return: a Liquid template
        """
        return env.get_template(filename)

    def make_prompt(self, filename: str, **kwargs) -> Prompt:
        """
        Make a prompt from a Liquid template.

        :param filename: filepath to the template
        :param kwargs: keyword arguments to pass to the template
        :return: a Prompt object
        """

        text = self.render(filename, **kwargs)
        prompt = Prompt(filename=filename, body=text)

        return prompt

    def render(self, filename: str, **kwargs) -> str:
        """
        Render a Liquid template.

        :param filename: filepath to the template
        :param kwargs: keyword arguments to pass to the template
        :return: a rendered Liquid template
        """
        template = self.find(filename)
        return template.render(**kwargs)
