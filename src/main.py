import os
import random
import time
import schedule
from datetime import datetime, timedelta

REPO_PATHS = [
    os.path.expanduser("~/Desktop/next_js_projects/ezylearn/"),
    os.path.expanduser("~/Desktop/next_js_projects/printouts/"),
    os.path.expanduser("~/Desktop/next_js_projects/stonks/"),
    os.path.expanduser("~/Desktop/next_js_projects/nhce-clubs/"),
]

COMMIT_MESSAGES = [
    "Refactor code",
    "Update Readme",
    "Add Comments",
    "UI changes",
    "Improved authentication",
    "Build error solved",
    "Fix Typo",
    "Improved Logic",
]

def make_change(repo_path):
    change_file = os.path.join(repo_path, "activity_log.txt")
    with open(change_file, "a") as f:
        f.write(f"Commit activity at {datetime.now()}\n")
    print(f"Changes made to {change_file}")

def random_commit():
    repo_path = random.choice(REPO_PATHS)
    os.chdir(repo_path)
    make_change(repo_path)
    os.system("git add .")
    commit_message = random.choice(COMMIT_MESSAGES)
    os.system(f'git commit -m "{commit_message}"')
    os.system("git push")
    print(f"Committed: {commit_message} at {datetime.now()}")
    print("\n**************************************************\n")

def schedule_commits():
    num_commits = random.randint(2, 3)  # Randomly choose 2 or 3 commits
    print(f"\nDate: {datetime.now().strftime('%Y-%m-%d')}")
    print(f"Scheduling {num_commits} commits for today:\n")

    hours = random.sample(range(9, 23), num_commits)
    schedule_times = []  

    for hour in hours:
        minute = random.randint(0, 59)
        commit_time = f"{hour:02d}:{minute:02d}"
        schedule_times.append(commit_time)
        schedule.every().day.at(commit_time).do(random_commit)

    for commit_time in sorted(schedule_times):
        print(f"- Commit scheduled at {commit_time}")
    print("\n")

while True:
    today = datetime.now().date()
    schedule_commits()  

    next_day = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
    time_until_next_day = (next_day - datetime.now()).total_seconds()
    print(f"Waiting {time_until_next_day / 3600:.2f} hours for the next day's schedule...\n")

    while time_until_next_day > 0:
        schedule.run_pending()
        time.sleep(30)
        time_until_next_day -= 30
