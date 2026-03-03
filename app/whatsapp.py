import os

import requests


def send_whatsapp_text(to: str, text: str) -> dict:
    token = os.getenv("WHATSAPP_TOKEN", "")
    phone_number_id = os.getenv("WHATSAPP_PHONE_NUMBER_ID", "")
    version = os.getenv("WHATSAPP_API_VERSION", "v21.0")

    if not token or not phone_number_id:
        return {
            "ok": False,
            "error": "Missing WHATSAPP_TOKEN or WHATSAPP_PHONE_NUMBER_ID",
        }

    url = f"https://graph.facebook.com/{version}/{phone_number_id}/messages"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    payload = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": to,
        "type": "text",
        "text": {"preview_url": False, "body": text},
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=20)
        body = response.json() if response.content else {}
        return {
            "ok": response.ok,
            "status_code": response.status_code,
            "response": body,
        }
    except requests.RequestException as exc:
        return {"ok": False, "error": str(exc)}