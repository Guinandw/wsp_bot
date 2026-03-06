def handle_text(user_id: str, text: str) -> str:
    t = (text or "").strip().lower()

    if t in ("hola", "buenas", "menu", "menú"):
        return (
            "Bienvenido a Marta Resto 🍽️\n"
            "1) Ver menú\n"
            "2) Reservar mesa\n"
            "3) Horarios\n"
            "Escribí el número."
        )

    if t == "1":
        return "📋 Menú:\n- Pizza\n- Hamburguesa\n- Ensalada"

    if t == "3":
        return "🕒 Horarios: Lun-Dom 19:00–00:00"

    return "No entendí. Escribí 'hola' o 'menu'."