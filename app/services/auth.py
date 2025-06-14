from fastapi import HTTPException, status

STATIC_TOKEN = "secret-token"  # Token estático conforme exigido

def authenticate_user(token: str):
    if token != "secret-token":  # Token estático
        raise HTTPException(
            status_code=401,
            detail="Token de autenticação inválido"
        )
    return {"user_id": 1}  # Retorna um usuário mockado