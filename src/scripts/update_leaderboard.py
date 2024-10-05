import json
import os

# Obtain data from the secret
students = json.loads(os.environ['STUDENT_EMAIL_MAP'])

# Read pr_stats.json
with open('src/scripts/pr_stats.json', 'r') as f:
    stats = json.load(f)

# Prepare to find the top users while excluding 'herreradelduque'
filtered_users = {user: count for user, count in stats['users'].items() if user != 'herreradelduque'}

# Sort users by their merge count and get the top 5
top_users = sorted(filtered_users.items(), key=lambda x: x[1], reverse=True)[:5]

# Create leaderboard string
leaderboard_lines = ['## Ranking de PR Mergeados\n']
if top_users:
    for user, count in top_users:
        real_name = students.get(user, [None, user])[1]  # Get real name or use username
        leaderboard_lines.append(f'**{real_name}**: **{count}** merges\n')
else:
    leaderboard_lines.append('No hay merges registrados.\n')

# Write to leaderboard.md
with open('leaderboard.md', 'w') as f:
    f.write('\n'.join(leaderboard_lines))

