from app.services.user_service import get_user_by_id
from app.models.user import User

def test_get_user_by_id(db):
    # Arrange
    user = User(username="aziz", email="aziz@test.com", password_hash="hashedpwd", role_id=1)
    db.add(user)
    db.commit()
    db.refresh(user)

    # Act
    result = get_user_by_id(db, user.id)

    # Assert
    assert result is not None
    assert result.username == "aziz"
    assert result.email == "aziz@test.com"
