from fastapi import APIRouter


router = APIRouter()


@router.get('/')
def health():

    return {
        "api": {
            "is_up": True
        }
    }
