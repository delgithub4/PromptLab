from services.template_service import TemplateService


class PromptService:

    def __init__(self):

        self.template = TemplateService()

    def get_prompt(
        self,
        name
    ):

        return {

            "name": name,

            "prompt": self.template.load(name)

        }
