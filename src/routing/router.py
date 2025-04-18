from fastapi import APIRouter

from src.services.base_services import main_service

router=APIRouter()

@router.get('/')
def main():
    return main_service()
