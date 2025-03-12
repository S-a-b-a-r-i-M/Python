import base64
import hashlib
import hmac
from datetime import datetime, timedelta

import secrets

# Generate a strong random key (32 bytes = 256 bits)
SIGNED_HEADER_SECRET_KEY = "a98ba8ac55eb5d15bafb731dd6641c067351cf327867e442ea70986b0b01beb3"

def generate_signature(user_id: int, role: str, expiry_minutes: int = 60):
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
    sig = f"{expiry_str}|{signature}"
    return base64.b64encode(sig.encode()).decode()
    

def verify_signature(signature: str, user_id: str, role: str) -> int:
    """Verify the signed signature from internal headers."""
    # Parse the signature header value
    try:
        decoded_signature = base64.b64decode(signature).decode()
        expiry_str, received_signature = decoded_signature.split("|")
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

# print(verify_signature(
#   "MjAyNS0wMy0wNlQxNzoyNjoxNi44MTM2ODZ8MTVjZGUyMmJjN2MzODIyZjBkNjc2YjQ1NDIwMjM0NWYwNDMzNTA3YTZkY2RhMjAwN2M0ZWE0YWU1NTEyMDRiYg==",
#   1,
#   "admin"
# ))

print(generate_signature(8, "admin"))