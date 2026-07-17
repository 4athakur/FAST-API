import hashlib
import hmac
import json
import time


def get_delta_headers(api_key: str, api_secret: str, method: str, request_path: str, body: dict | str | None = None) -> dict:
    """Build Delta Exchange REST API authentication headers."""
    timestamp = str(int(time.time() * 1000))
    payload_body = ''

    if body is None:
        payload_body = ''
    elif isinstance(body, dict):
        payload_body = json.dumps(body, separators=(',', ':'), sort_keys=True)
    else:
        payload_body = str(body)

    payload = timestamp + method.upper() + request_path + payload_body
    signature = hmac.new(api_secret.encode('utf-8'), payload.encode('utf-8'), hashlib.sha256).hexdigest()

    return {
        'api-key': api_key,
        'signature': signature,
        'timestamp': timestamp,
        'Content-Type': 'application/json',
    }


# Example usage
if __name__ == '__main__':
    API_KEY = 'your_api_key'
    API_SECRET = 'your_api_secret'
    method = 'GET'
    path = '/api/v3/positions'

    headers = get_delta_headers(API_KEY, API_SECRET, method, path)
    print(headers)
