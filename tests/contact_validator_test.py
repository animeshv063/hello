import pytest
from src.contact_validator import is_valid_email, is_valid_phone, mask_email, normalize_phone


def test_is_valid_email_true():
    """Test a well-formed email."""
    # Arrange
    email = "student@lpu.in"

    # Act
    result = is_valid_email(email)

    # Assert
    assert result == True


def test_is_valid_email_type_error():
    """Test that a non-string input raises TypeError."""
    with pytest.raises(TypeError):
        is_valid_email(12345)


def test_is_valid_phone_true():
    """Test a well-formed phone number with dashes."""
    # Arrange
    phone = "555-123-4567"

    # Act
    result = is_valid_phone(phone)

    # Assert
    assert result == True


def test_is_valid_phone_type_error():
    """Test that a non-string phone raises TypeError."""
    with pytest.raises(TypeError):
        is_valid_phone(12345)


def test_is_valid_phone_false_on_invalid_length():
    """Test an invalid phone length returns False."""
    assert is_valid_phone("555-123") is False


def test_mask_email_basic():
    """Test masking a typical email address."""
    email = "priya@example.com"

    result = mask_email(email)

    assert result == "pr***@example.com"


def test_mask_email_invalid_raises_value_error():
    """Test invalid email input raises ValueError."""
    with pytest.raises(ValueError):
        mask_email("not-an-email")


def test_normalize_phone_true():
    """Test that a valid phone is normalized to digits only."""
    assert normalize_phone("555-123-4567") == "5551234567"


def test_normalize_phone_invalid_raises_value_error():
    """Test invalid phone input raises ValueError."""
    with pytest.raises(ValueError):
        normalize_phone("123")
