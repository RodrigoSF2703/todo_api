from fastapi import APIRouter, Header, Depends
from app.services.auth import authenticate_user

router = APIRouter()


@router.post("/verify-token")
def verify_token(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=400, detail="Formato de token inválido")

    token = authorization.split(" ")[1]
    return authenticate_user(token)