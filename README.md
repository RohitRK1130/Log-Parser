# Fair Billing

## Problem Statement

You are working for a hosted application provider that charges for the use of its application by the duration of sessions. The usage data comes from a log file that lists the time at which a session starts or stops, the name of the user, and whether this is the start or end of the session. Unfortunately, the log files may lack pairing information between start and end lines, and sessions may overlap the time boundaries of the log file. Your task is to process the log file, print out a report of users, the number of sessions, and the minimum possible total duration of their sessions in seconds consistent with the data in the file.

## Solution

### Approach:

The code reads the log file line by line, extracts relevant information (timestamp, username, and action), and processes the data to determine user sessions and their durations. Sessions with missing start or end markers are assumed to start at the earliest time in the file or end at the latest time. The code then prints a report for each user, including the number of sessions and the total duration.

### Code Flow:

1. Open the log file and iterate through each line.
2. Parse the timestamp, username, and action (Start or End) from each line.
3. Track the earliest timestamp in the file.
4. Process each line based on the action:
   - If the action is 'Start', update the user_sessions_data with a new session start.
   - If the action is 'End', find the corresponding start time and update the session end time.
5. Print a report for each user, including the number of sessions and total duration.

## Prerequisite

- Python 3.x installed on the system.

### How to Run

```sh
git clone https://github.com/RohitRK1130/Log-Parser.git -b main
cd Log-Parser
python3 log_parser.py logfile.txt
```

### Input Example 
```sh
14:02:03 ALICE99 Start
14:02:05 CHARLIE End
14:02:34 ALICE99 End
14:02:58 ALICE99 Start
14:03:02 CHARLIE Start
14:03:33 ALICE99 Start
14:03:35 ALICE99 End
14:03:37 CHARLIE End
14:04:05 ALICE99 End
14:04:23 ALICE99 End
14:04:41 CHARLIE Start
```

### Output Example(terminal)
```sh
ALICE99 4 240
CHARLIE 3 37
```

### Further notes

- The code assumes correctly ordered chronological data within a single day.
- Invalid or irrelevant lines in the log file are silently ignored.
- Sessions with missing start or end markers are handled as described in the problem statement.
