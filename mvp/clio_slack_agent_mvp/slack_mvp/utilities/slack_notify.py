def notify_acknowledgement(response_url: str, text: str):
    import httpx
    httpx.post(response_url, json={"text": text})
