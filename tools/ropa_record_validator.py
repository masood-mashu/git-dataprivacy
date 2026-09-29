"""
ropa_record_validator.py - Validates mandatory GDPR Article 30 required fields in processing activity record
"""
import sys
import json


def validate_ropa_record(ropa_entry_json: str):
    import json
    data = json.loads(ropa_entry_json) if isinstance(ropa_entry_json, str) else ropa_entry_json
    required = ["purpose", "data_categories", "recipients", "lawful_basis"]
    missing = [f for f in required if not data.get(f)]
    is_valid = len(missing) == 0
    return {"is_valid": is_valid, "missing_fields": missing, "status": "ROPA_COMPLIANT" if is_valid else "ROPA_DEFICIT"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "ropa-record-validator"}))
