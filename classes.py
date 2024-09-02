def assign_key(description):
    if "frio" in description.lower() or "noites frescas" in description.lower():
        return "noite aconchegante"
    elif "calor" in description.lower() or "dias quentes" in description.lower():
        return "almoço ao ar livre"
    elif "tardes ensolaradas" in description.lower():
        return "tarde ensolarada"
    elif "jantar" in description.lower():
        return "jantar sofisticado"
    elif "piqueniques" in description.lower():
        return "piquenique"
    elif "relaxantes" in description.lower():
        return "noite relaxante"
    elif "verão" in description.lower():
        return "tarde de verão"
    else:
        return "ocasião especial"
