def enrich_ip(ip):
    # Simple classification
    if ip.startswith("192.168"):
        return "Private Network"
    elif ip.startswith("10.") or ip.startswith("172."):
        return "Private Network"
    else:
        return "Public Network"


def enrich_logs(logs):
    for log in logs:
        log["ip_type"] = enrich_ip(log["source_ip"])
    return logs