import os
from datetime import datetime, timedelta
import random

# Set your GitHub user details
os.system('git config user.name "zacker-zxz"')
os.system('git config user.email "tejastayade4@gmail.com"')  # <-- Change this

start_date = datetime.now() - timedelta(days=120)

languages = {
    'js': 'script.js',
    'css': 'style.css',
    'ts': 'main.ts',
    'py': 'main.py',
    'html': 'index.html',
    'c': 'main.c'
}

commit_messages = [
    "Refactored core logic 🚀",
    "Optimized performance 🔧",
    "Updated UI styling 🎨",
    "Fixed bug in module ⚙️",
    "Improved error handling ❗",
    "Code cleanup and reorg ✨",
    "Added comments for clarity 📘",
    "Enhanced responsiveness 📱",
    "Minor tweak to layout 📐",
    "Adjusted config values 🔧"
]

# Loop over 100 days with 1–4 commits/day
for day_offset in range(100):
    day = start_date + timedelta(days=day_offset)
    for _ in range(random.randint(1, 4)):
        lang = random.choice(list(languages.keys()))
        filename = languages[lang]
        commit_msg = random.choice(commit_messages)
        date_str = day.strftime('%Y-%m-%dT%H:%M:%S')

        # Comment style based on file type
        if filename.endswith(('.js', '.ts', '.c')):
            content_line = f"// {commit_msg}"
        elif filename.endswith('.py'):
            content_line = f"# {commit_msg}"
        elif filename.endswith('.html'):
            content_line = f"<!-- {commit_msg} -->"
        else:
            content_line = f"/* {commit_msg} */"

        # Write to file
        with open(filename, 'a', encoding='utf-8') as f:

            f.write(content_line + '\n')
 

        os.system(f'git add {filename}')
        os.system(f'git commit --date="{date_str}" -m "{commit_msg}"')

os.system('git push origin main')
