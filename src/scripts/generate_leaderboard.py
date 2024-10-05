import json

def main():
    # Load the JSON data from the file
    with open('src/scripts/pr_stats.json', 'r') as f:
        data = json.load(f)

    # Extract users and their merge counts
    users = data['users']

    # Exclude specified user
    excluded_user = "herreradelduque"
    filtered_users = {user: count for user, count in users.items() if user != excluded_user}

    # Sort users by the number of merges in descending order
    sorted_users = sorted(filtered_users.items(), key=lambda x: x[1], reverse=True)

    # Generate leaderboard markdown
    leaderboard = "# Ranking de PR Mergeados\n\n"
    
    # Generate the top 5 leaderboard
    for user, merge_count in sorted_users[:5]:
        leaderboard += f"**{user}**: {merge_count} merges\n"

    # Save leaderboard to a file
    with open('leaderboard.md', 'w') as f:
        f.write(leaderboard)

    # Print the leaderboard for verification
    print(leaderboard)

if __name__ == "__main__":
    main()
