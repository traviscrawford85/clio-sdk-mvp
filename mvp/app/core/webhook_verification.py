import hmac
import hashlib

def verify_clio_webhook(payload: bytes, signature: str, secret: str) -> bool:
    """
    Verify Clio webhook signature using HMAC SHA256.
    Args:
        payload (bytes): The raw request body.
        signature (str): The value from the 'X-Signature' header.
        secret (str): The Clio client secret.
    Returns:
        bool: True if signature is valid, False otherwise.
    """
    if not secret:
        return False
    computed = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(computed, signature)

def verify_qbo_webhook(payload: bytes, signature: str, secret: str) -> bool:
    """
    Verify QBO webhook signature using HMAC SHA256 (or your QBO method).
    Args:
        payload (bytes): The raw request body.
        signature (str): The value from the QBO signature header.
        secret (str): The QBO client secret.
    Returns:
        bool: True if signature is valid, False otherwise.
    """
    if not secret:
        return False
    computed = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(computed, signature)

def verify_slack_webhook(payload: bytes, timestamp: str, signature: str, secret: str) -> bool:
    """
    Verify Slack webhook signature using Slack's signing secret and signature scheme.
    Args:
        payload (bytes): The raw request body.
        timestamp (str): The value from the 'X-Slack-Request-Timestamp' header.
        signature (str): The value from the 'X-Slack-Signature' header.
        secret (str): The Slack signing secret.
    Returns:
        bool: True if signature is valid, False otherwise.
    """
    if not secret or not timestamp or not signature:
        return False
    import time
    # Slack recommends rejecting requests older than 5 minutes
    if abs(time.time() - int(timestamp)) > 60 * 5:
        return False
    basestring = f'v0:{timestamp}:{payload.decode()}'
    computed = 'v0=' + hmac.new(secret.encode(), basestring.encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(computed, signature)
