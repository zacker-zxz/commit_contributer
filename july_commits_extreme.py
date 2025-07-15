import os
from datetime import datetime, timedelta
import random

os.system('git config user.name "zacker-zxz"')
os.system('git config user.email "tejastayade4@gmail.com"')

start_date = datetime(2025, 7, 1)
end_date = datetime(2025, 7, 15)
languages = {
    'js': 'script.js',
    'css': 'style.css',
    'ts': 'main.ts',
    'py': 'main.py',
    'html': 'index.html',
    'c': 'main.c',
}
commit_messages = [
    "Massive July update 💥",
    "Performance boost in core 🌐",
    "UI overhaul for testing 🧪",
    "Daily refactor madness 🔄",
    "Cleanup before deploy 🧹",
    "Tuned logic handling 🛠️",
    "Pre-release tweaks ⚒️",
    "Aggressive commits for July 🔥",
    "July sprint day complete ✅",
    "July domination begins 👑",
]

day = start_date
while day <= end_date:
    for _ in range(random.randint(10, 15)):
        lang = random.choice(list(languages.keys()))
        filename = languages[lang]
        commit_msg = random.choice(commit_messages)
        date_str = day.strftime('%Y-%m-%dT%H:%M:%S')
        if filename.endswith(('.js', '.ts', '.c')):
            content_line = f"// {commit_msg}"
        elif filename.endswith('.py'):
            content_line = f"# {commit_msg}"
        elif filename.endswith('.html'):
            content_line = f"<!-- {commit_msg} -->"
        else:
            content_line = f"/* {commit_msg} */"
        with open(filename, 'a', encoding='utf-8') as f: f.write(content_line + '\n')
        os.system(f'git add {filename}')
        os.system(f'git commit --date="{date_str}" -m "{commit_msg}"')
    day += timedelta(days=1)

os.system('git push origin main')