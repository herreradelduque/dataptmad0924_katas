import os
import json
import requests

# Environment variables for GitHub Actions
GITHUB_REPO = os.environ.get('GITHUB_REPOSITORY')  # 'owner/repo' format
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')  # The secret token

# Function to fetch closed pull requests
def fetch_pull_requests():
    url = f"https://api.github.com/repos/{GITHUB_REPO}/pulls?state=closed"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)  # Using headers for authentication
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

# Main function to process the pull requests and count merges
def main():
    pr_data = fetch_pull_requests()  # Fetch closed PRs
    pr_stats = {}
    detailed_prs = []  # To hold detailed PR info

    for pr in pr_data:
        user = pr['user']['login']  # Get the username of the PR author
        title = pr['title']          # Get the title of the PR
        merged_at = pr['merged_at']  # Get the date when PR was merged

        # Only count merged PRs
        if merged_at:
            # Collect additional information
            pr_details = {
                'title': title,
                'merged_at': merged_at,
                'url': pr['html_url'],  # Get the URL of the PR
                'user': user
            }
            detailed_prs.append(pr_details)

            # Count merges
            if user in pr_stats:
                pr_stats[user] += 1  # Increment the count for this user
            else:
                pr_stats[user] = 1  # Initialize count for this user

    # Write stats to a JSON file
    with open('src/scripts/pr_stats.json', 'w') as f:
        json.dump({'users': pr_stats, 'detailed_prs': detailed_prs}, f, indent=4)

if __name__ == "__main__":
    main()
