from fastapi import APIRouter, status

router = APIRouter(
  prefix='/login',
  tags=['Login']
)

@router.post('/', status_code=status.HTTP_200_OK)
def user_login():
    # validate user
    
    # authorize login
    return {
      "status": "User Authenticated"
    }