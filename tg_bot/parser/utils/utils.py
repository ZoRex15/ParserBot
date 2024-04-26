
def convert_json_filter(querys: list[str]) -> list[dict]:
    dicts = []
    for row_sertificate in querys:
        dicts.append(
            {
        'name': 'number',
        'search': row_sertificate,
        'type': 9,
    }
        )

    return dicts