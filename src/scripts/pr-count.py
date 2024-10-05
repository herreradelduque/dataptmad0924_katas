import json
import requests

# Configuration
REPO_OWNER = 'your-username'  # Replace with your GitHub username
REPO_NAME = 'your-repo'        # Replace with your repository name
GITHUB_TOKEN = 'your_github_token'  # Replace with your GitHub token

def fetch_pull_requests():
    url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls?state=closed'
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

def count_merges(pr_data):
    stats = {'users': {}}
    
    for pr in pr_data:
        if pr['merged_at']:  # Only consider merged PRs
            user = pr['user']['login']
            if user not in stats['users']:
                stats['users'][user] = {'merge_count': 0}
            stats['users'][user]['merge_count'] += 1

    return stats

def save_pr_stats(stats):
    with open('pr_stats.json', 'w') as f:
        json.dump(stats, f, indent=4)

def main():
    pr_data = fetch_pull_requests()  # Fetch closed PRs
    stats = count_merges(pr_data)     # Count merges
    save_pr_stats(stats)               # Save to JSON

if __name__ == '__main__':
    main()
