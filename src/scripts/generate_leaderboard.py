import json

def main():
    # Load the JSON data from the file
    with open('pr_stats.json', 'r') as f:
        data = json.load(f)

    # Extract users and their merge counts
    users = data['users']

    # Determine the user with the most merges
    if users:
        top_user = max(users, key=users.get)  # Get the user with the highest count
        max_merges = users[top_user]  # Number of merges for the top user
    else:
        top_user = None
        max_merges = 0

    # Generate leaderboard markdown
    leaderboard = "# Ranking de PR Mergeados\n\n"
    if top_user:
        leaderboard += f"El estudiante con más PR mergeados es: {top_user} con {max_merges} merges.\n"
    else:
        leaderboard += "No hay merges registrados.\n"

    # Save leaderboard to a file
    with open('leaderboard.md', 'w') as f:
        f.write(leaderboard)

    # Print the leaderboard for verification
    print(leaderboard)

if __name__ == "__main__":
    main()
