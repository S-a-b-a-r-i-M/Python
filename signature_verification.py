import hashlib
import hmac
from datetime import datetime, timedelta

import secrets

# Generate a strong random key (32 bytes = 256 bits)
SIGNED_HEADER_SECRET_KEY = "a98ba8ac55eb5d15bafb731dd6641c067351cf327867e442ea70986b0b01beb3"

def create_signature(user_id: int, role: str, expiry_minutes: int = 60):
    """
    Generate a signed signature for authentication headers.
    
    Args:
        user_id: User identifier
        role: User role
        expiry_minutes: Minutes until signature expires
        
    Returns:
        String in format "expiry_timestamp|signature"
    """
    # Create expiry timestamp (ISO format)
    expiry = datetime.now() + timedelta(minutes=expiry_minutes)
    expiry_str = expiry.isoformat()

    message = f"{user_id}:{role}:{expiry_str}"
    # Generate signature
    signature = hmac.new(
        SIGNED_HEADER_SECRET_KEY.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()

    return f"{expiry_str}|{signature}"
    

def verify_signature(signature: str, user_id: str, role: str) -> int:
    """Verify the signed signature from internal headers."""
    # Parse the signature header value
    try:
        expiry_str, received_signature = signature.split("|")
    except ValueError:
        print("Malformed signature header")
        return -1

    # Check if signature has expired
    expiry = datetime.fromisoformat(expiry_str)
    if datetime.now() > expiry:
        print("Signature expired")
        return -1

    # Verify signature
    message = f"{user_id}:{role}:{expiry_str}"
    expected_signature = hmac.new(
        SIGNED_HEADER_SECRET_KEY.encode(), message.encode(), hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(received_signature, expected_signature):
        print()

    return int(user_id)


# print(create_signature(1, "admin"))

print(verify_signature(
  "2025-02-28T19:16:00.164342|9c51a78bdb33a860cab267aeb83d18710e0140bc2c151d3c7f26a5ec9ae8b697",
  1,
  "admin"
))
