import requests
from collections import defaultdict

# Configuration
GITHUB_TOKEN = 'YOUR_GITHUB_TOKEN'  # Replace with your GitHub token
GITHUB_REPO = 'herreradelduque/dataptmad0924_katas'  # Replace with your repository

# GitHub API endpoint for closed pull requests
BASE_URL = f'https://api.github.com/repos/{GITHUB_REPO}/pulls'
HEADERS = {'Authorization': f'token {GITHUB_TOKEN}'}

# Function to fetch pull requests with pagination handling
def fetch_pull_requests():
    pr_data = []
    page = 1
    per_page = 100  # Set to maximum items per page

    while True:
        response = requests.get(f"{BASE_URL}?state=closed&page={page}&per_page={per_page}", headers=HEADERS)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()

        if not data:
            break  # Exit loop if no more data
        
        pr_data.extend(data)
        page += 1  # Move to the next page

    return pr_data

# Function to process pull requests and count merged pull requests
def process_pull_requests(pr_data):
    pr_stats = defaultdict(int)  # Store counts of merged PRs
    detailed_prs = []
    unmerged_prs = []  # Store unmerged PRs

    for pr in pr_data:
        user = pr['user']['login']
        merged_at = pr.get('merged_at')

        if merged_at:  # Only count merged PRs
            pr_stats[user] += 1
            detailed_prs.append({
                'title': pr['title'],
                'merged_at': merged_at,
                'url': pr['html_url'],
                'user': user
            })
        else:  # Capture unmerged PRs as well
            unmerged_prs.append({
                'title': pr['title'],
                'url': pr['html_url'],
                'user': user
            })

    return pr_stats, detailed_prs, unmerged_prs

# Main function
def main():
    print("Fetching pull requests...")
    pr_data = fetch_pull_requests()
    pr_stats, detailed_prs, unmerged_prs = process_pull_requests(pr_data)

    # Print results
    print("\nPull Request Statistics:")
    for user, count in pr_stats.items():
        print(f"{user}: {count} merged PRs")

    print("\nDetailed Merged Pull Requests:")
    for pr in detailed_prs:
        print(f"{pr['title']} by {pr['user']} was merged at {pr['merged_at']}. URL: {pr['url']}")

    print("\nUnmerged Pull Requests:")
    for pr in unmerged_prs:
        print(f"{pr['title']} by {pr['user']}. URL: {pr['url']} (Not merged)")

if __name__ == "__main__":
    main()
