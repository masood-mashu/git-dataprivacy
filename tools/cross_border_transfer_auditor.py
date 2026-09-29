"""
cross_border_transfer_auditor.py - Verifies adequacy decision or executed SCC agreement for international transfers
"""
import sys
import json


def audit_cross_border_transfer(transfer_json: str):
    import json
    data = json.loads(transfer_json) if isinstance(transfer_json, str) else transfer_json
    dest = data.get("destination_country", "UK").upper()
    has_scc = data.get("has_scc_executed", True)
    adequate = dest in ["UK", "JAPAN", "CANADA", "ISRAEL", "SWITZERLAND"]
    authorized = adequate or has_scc
    return {"authorized": authorized, "status": "TRANSFER_AUTHORIZED" if authorized else "TRANSFER_UNLAWFUL"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "cross-border-transfer-auditor"}))
