STATUSES = ["draft", "qualified", "approved", "fulfilled"]
FIELD_SCHEMA = [
  {
    "key": "client",
    "label": "Client",
    "type": "text",
    "required": true
  },
  {
    "key": "value_estimate",
    "label": "Value Estimate",
    "type": "number",
    "required": true
  },
  {
    "key": "commercial_notes",
    "label": "Commercial Notes",
    "type": "textarea",
    "required": true
  }
]


def validate_payload(payload):
    if not isinstance(payload, dict):
        raise ValueError("payload must be an object")

    cleaned = {}
    for field in FIELD_SCHEMA:
        key = field["key"]
        value = payload.get(key)
        if isinstance(value, str):
            value = value.strip()
        if field["required"] and (value is None or value == ""):
            raise ValueError(f"{field['label']} is required")
        if field["type"] == "number" and value not in (None, ""):
            try:
                value = float(value)
            except ValueError as exc:
                raise ValueError(f"{field['label']} must be numeric") from exc
        cleaned[key] = value
    return cleaned
