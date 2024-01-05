from datetime import datetime
import sys

def analyze_user_logs(log_file_path):
    user_sessions_data = {}
    earliest_time_recorded = None

    with open(log_file_path, 'r') as log_data:
        for line in log_data:
            line = line.strip()
            if not line:
                continue  
            try:
                time_str, current_user, user_action = line.split()
                timestamp = datetime.strptime(time_str, '%H:%M:%S')

                if earliest_time_recorded is None:
                    earliest_time_recorded = timestamp

                if user_action == 'Start':
                    if current_user not in user_sessions_data:
                        user_sessions_data[current_user] = [(timestamp, None)]
                    else:
                        user_sessions_data[current_user].append((timestamp, None))
                elif user_action == 'End':
                    user_sessions = user_sessions_data.get(current_user, [])
                    for i, (start_time, end_time) in enumerate(user_sessions):
                        if end_time is None:
                            user_sessions[i] = (start_time, timestamp)
                            break
                    else:
                        user_sessions.append((earliest_time_recorded, timestamp))
                    user_sessions_data[current_user] = user_sessions

            except ValueError:
                pass

    for user, sessions in user_sessions_data.items():
        total_duration = sum((end - start).seconds if end else 0 for start, end in sessions)
        print(f'{user} {len(sessions)} {total_duration}')

    return user_sessions_data

def main():
    if len(sys.argv) != 2:
        print("Command: python3 script.py <path_to_log_file>")
        sys.exit(1)

    log_file_path = sys.argv[1]
    analyze_user_logs(log_file_path)

main()