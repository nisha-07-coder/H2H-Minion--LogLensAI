import re
import os
from classifier import classify_logs
from anomaly import detect_anomalies

# Parse a single log
def parse_log(log):
    pattern = r"SRC=(\S+)\s+PORT=(\d+)\s+ACTION=(\S+)"
    
    match = re.search(pattern, log)
    
    if match:
        return {
            "source_ip": match.group(1),
            "port": int(match.group(2)),
            "action": match.group(3)
        }
    return None


# Parse file
def parse_file(file_path):
    parsed_logs = []

    with open(file_path, "r") as file:
        for line in file:
            parsed = parse_log(line.strip())
            if parsed:
                parsed_logs.append(parsed)

    return parsed_logs


# Main
if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_dir, "data", "sample_logs.txt")

    logs = parse_file(file_path)

    # Classification
    logs = classify_logs(logs)

    # Anomaly detection
    anomalies = detect_anomalies(logs)

    print("Classified Logs:\n")
    for log in logs:
        print(log)

    print("\nDetected Anomalies:\n")
    for a in anomalies:
        print(a)