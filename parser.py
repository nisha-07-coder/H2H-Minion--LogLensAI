import re
import os
from classifier import classify_logs

# Function to parse a single log line
def parse_log(log):
    pattern = r"SRC=(\S+)\s+PORT=(\d+)\s+ACTION=(\S+)"
    
    match = re.search(pattern, log)
    
    if match:
        return {
            "source_ip": match.group(1),
            "port": int(match.group(2)),
            "action": match.group(3)
        }
    else:
        return None


# Function to parse entire file
def parse_file(file_path):
    parsed_logs = []
    
    with open(file_path, "r") as file:
        for line in file:
            parsed = parse_log(line.strip())
            if parsed:
                parsed_logs.append(parsed)
    
    return parsed_logs


# Main execution
if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_dir, "data", "sample_logs.txt")

    logs = parse_file(file_path)
    logs = classify_logs(logs)

    print("Classified Logs:\n")

    for log in logs:
        print(log)