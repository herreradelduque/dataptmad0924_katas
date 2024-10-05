import json
import os

# Obtener datos del secret
students = json.loads(os.environ['STUDENT_EMAIL_MAP'])

# Leer pr_stats.json
with open('src/scripts/pr_stats.json', 'r') as f:
    stats = json.load(f)

# Exclude the specified user
excluded_user = "herreradelduque"

# Create a new dict for users excluding the specified user
filtered_users = {user: count for user, count in stats['users'].items() if user != excluded_user}

# Sort users by the number of merges in descending order
sorted_users = sorted(filtered_users.items(), key=lambda x: x[1], reverse=True)

# Create leaderboard.md
with open('leaderboard.md', 'w') as f:
    f.write('## Ranking de PR Mergeados\n\n')
    
    # Limit to top 5 users
    top_n = 5
    for user, merge_count in sorted_users[:top_n]:
        user_name = students.get(user, [None, user])[1]  # Get real name or use username
        f.write(f'**{user_name}**: {merge_count} merges\n')
