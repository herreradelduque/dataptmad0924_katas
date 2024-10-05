import json

def main():
    # Load the JSON data from the file
    with open('src/scripts/pr_stats.json', 'r') as f:
        data = json.load(f)

    # Extract users and their merge counts
    users = data['users']

    # Filter out 'herreradelduque' and sort users by their merge counts
    filtered_users = {user: count for user, count in users.items() if user != 'herreradelduque'}

    # Sort users and select the top 5
    sorted_users = sorted(filtered_users.items(), key=lambda x: x[1], reverse=True)[:5]

    # Generate leaderboard markdown
    leaderboard = "# Ranking de PR Mergeados\n\n"

    if sorted_users:
        for user, merges in sorted_users:
            leaderboard += f"{user}: {merges} merges\n"
    else:
        leaderboard += "No hay merges registrados.\n"

    # Save leaderboard to a file
    with open('leaderboard.md', 'w') as f:
        f.write(leaderboard)

    # Print the leaderboard for verification
    print(leaderboard)

if __name__ == "__main__":
    main()
