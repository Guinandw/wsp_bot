import os

from flask import Blueprint, jsonify, render_template, request

from .whatsapp import send_whatsapp_text

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return render_template("index.html")


@main_bp.get("/webhook")
def verify_webhook():
    verify_token = os.getenv("WHATSAPP_VERIFY_TOKEN", "")
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == verify_token:
        return challenge or "", 200
    return "Verification token mismatch", 403


@main_bp.post("/webhook")
def receive_webhook():
    payload = request.get_json(silent=True) or {}
    changes = []

    for entry in payload.get("entry", []):
        changes.extend(entry.get("changes", []))

    for change in changes:
        value = change.get("value", {})
        messages = value.get("messages", [])
        for msg in messages:
            from_number = msg.get("from")
            text = (msg.get("text") or {}).get("body", "")
            if from_number and text:
                # Echo basico para validar envio + recepcion.
                send_whatsapp_text(from_number, f"Recibido: {text}")

    return jsonify({"status": "ok"}), 200


@main_bp.post("/send")
def send_message():
    data = request.get_json(silent=True) or {}
    to = data.get("to")
    text = data.get("text")

    if not to or not text:
        return jsonify({"error": "Missing 'to' or 'text'"}), 400

    response = send_whatsapp_text(to, text)
    return jsonify(response), 200
