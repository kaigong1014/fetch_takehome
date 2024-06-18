import hashlib
import json

def mask_pii(value):
    return hashlib.sha256(value.encode()).hexdigest()

def flatten_and_mask(data):
    data = json.loads(data)
    return {
        "user_id": data["user_id"],
        "device_type": data["device_type"],
        "masked_ip": mask_pii(data["ip"]),
        "masked_device_id": mask_pii(data["device_id"]),
        "locale": data["locale"],
        "app_version": data["app_version"],
        "create_date": data["create_date"]
    }