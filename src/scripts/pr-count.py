import os
import requests
import json

def fetch_pull_requests():
    token = os.environ.get('GITHUB_TOKEN')  # Get the GitHub token from the environment
    headers = {'Authorization': f'token {token}'}
    # Adjust the URL with your repository name
    url = 'https://api.github.com/repos/herreradelduque/dataptmad0924_katas/pulls?state=closed'
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

def main():
    pr_data = fetch_pull_requests()  # Fetch closed PRs
    
    # Initialize a dictionary to hold merge counts
    merge_counts = {}
    
    for pr in pr_data:
        user = pr['user']['login']
        if pr['merged_at']:  # Check if the PR was merged
            merge_counts[user] = merge_counts.get(user, 0) + 1
            
    # Write the results to a JSON file
    with open('pr_stats.json', 'w') as f:
        json.dump({'users': merge_counts}, f, indent=4)

if __name__ == "__main__":
    main()
