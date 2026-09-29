"""
retention_schedule_enforcer.py - Flags records exceeding lawful maximum retention duration in days
"""
import sys
import json


def enforce_retention_schedule(asset_retention_json: str):
    import json
    data = json.loads(asset_retention_json) if isinstance(asset_retention_json, str) else asset_retention_json
    age = data.get("age_days", 100)
    allowed = data.get("max_allowed_days", 365)
    expired = age > allowed
    return {"expired": expired, "days_over": max(age - allowed, 0), "status": "ASSETS_PURGED" if not expired else "RETENTION_EXCEEDED"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "retention-schedule-enforcer"}))
