from pathlib import Path


class TemplateService:

    def load(
        self,
        name
    ):

        path = Path("prompts") / f"{name}.txt"

        return path.read_text()
