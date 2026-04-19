def correlate_incidents(anomalies):
    incidents = []

    ip_events = {}

    # Group anomalies by IP
    for a in anomalies:
        ip = a["ip"]
        if ip not in ip_events:
            ip_events[ip] = []
        ip_events[ip].append(a["type"])

    # Create incidents
    for ip, events in ip_events.items():
        if "Brute Force Attack" in events and "Port Scan" in events:
            incidents.append({
                "ip": ip,
                "incident": "Coordinated Attack",
                "detail": "Brute force attempts followed by port scanning"
            })
        else:
            for e in events:
                incidents.append({
                    "ip": ip,
                    "incident": e,
                    "detail": "Single suspicious behavior"
                })

    return incidents