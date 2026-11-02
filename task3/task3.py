import sys
def parse_log_line(line: str) -> dict:

    parts = line.strip().split(maxsplit=3)

    if len(parts) < 4:
        return {}

    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3]
    }


def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parsed = parse_log_line(line)
                if parsed:
                    logs.append(parsed)
    except FileNotFoundError:
        print(f"Error: File with path: {file_path} not found")
    return logs


def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        level = log.get("level")
        if level:
            counts[level] = counts.get(level, 0) + 1

    return counts


def filter_logs_by_level(logs: list, level: str) -> list:

    return [log for log in logs if log.get("level") == level.upper()]


def display_log_counts(counts: dict):

    col1_width = 16
    col2_width = 10

    print(f"{'Рівень логування':<{col1_width}} | {'Кількість':<{col2_width}}")

    print(f"{'-' * col1_width}-|{'-' * (col2_width + 2)}")

    for level, count in counts.items():
        print(f"{level:<{col1_width}} | {count:<{col2_width}}")

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Використання: python task3.py <шлях_до_файлу> [рівень_логування]")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)

    if not logs:
        sys.exit(1)

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) > 2:
        target_level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, target_level)

        print(f"\nДеталі логів для рівня '{target_level.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")