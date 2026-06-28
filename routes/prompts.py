from fastapi import APIRouter

from services.prompt_service import PromptService

router = APIRouter(
    prefix="/prompts",
    tags=["Prompts"]
)

service = PromptService()


@router.get("/{name}")
def prompt(
    name: str
):

    return service.get_prompt(
        name
    )
