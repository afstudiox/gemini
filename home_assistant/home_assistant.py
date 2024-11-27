def set_light_values(brightness: int, color_temperature: str) -> dict:
    """
    Ajusta a luminosidade e a temperatura de cor das luzes.
    """
    print(f"[INFO] set_light_values chamado com brightness={brightness}, color_temperature={color_temperature}")
    # Simula o ajuste de luzes
    return {"brightness": brightness, "color_temperature": color_temperature}

def intruder_alert() -> dict:
    """
    Ativa o alerta de intruso.
    """
    print("[INFO] intruder_alert chamado.")
    # Simula o alerta de intruso
    return {"alert": "Intruder alert activated"}

def start_music(energetic: bool, loud: bool, tempo: int) -> dict:
    """
    Inicia a reprodução de música com as características especificadas.
    """
    print(f"[INFO] start_music chamado com energetic={energetic}, loud={loud}, tempo={tempo}")
    # Simula o início da música
    return {"energetic": energetic, "loud": loud, "tempo": tempo}

def good_morning() -> dict:
    """
    Executa a rotina matinal.
    """
    print("[INFO] good_morning chamado.")
    # Simula a rotina matinal
    return {"routine": "Good morning routine started"}

def set_thermostat_temperature(temperature: float) -> dict:
    """
    Ajusta a temperatura do termostato.
    """
    print(f"[INFO] set_thermostat_temperature chamado com temperature={temperature}")
    # Simula o ajuste da temperatura do termostato
    return {"temperature": temperature}

def open_curtains() -> dict:
    """
    Abre as cortinas.
    """
    print("[INFO] open_curtains chamado.")
    # Simula a abertura das cortinas
    return {"curtains": "Curtains opened"}

__all__ = ["set_light_values", "intruder_alert", "start_music", "good_morning", "set_thermostat_temperature", "open_curtains"]