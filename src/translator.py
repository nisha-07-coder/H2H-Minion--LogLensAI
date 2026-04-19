def translate_anomalies(anomalies):
    insights = []

    for a in anomalies:
        if a["type"] == "Brute Force Attack":
            insights.append({
                "ip": a["ip"],
                "message": f"Multiple failed login attempts from {a['ip']} indicate a possible brute-force attack.",
                "recommendation": "Block IP or enable login rate limiting."
            })

        elif a["type"] == "Port Scan":
            insights.append({
                "ip": a["ip"],
                "message": f"{a['ip']} is accessing multiple ports, indicating a possible port scan.",
                "recommendation": "Restrict access and monitor traffic."
            })

        else:
            insights.append({
                "ip": a["ip"],
                "message": "Suspicious activity detected.",
                "recommendation": "Investigate further."
            })

    return insights