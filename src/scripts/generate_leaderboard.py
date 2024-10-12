import os
import json
import pandas as pd
import requests

# Use built-in GITHUB_TOKEN
GITHUB_REPO = os.getenv('GITHUB_REPOSITORY')
if GITHUB_REPO is None:
    raise ValueError("GITHUB_REPOSITORY environment variable not set.")

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
if GITHUB_TOKEN is None:
    print("Warning: GITHUB_TOKEN environment variable not set. Using default token.")

# Extract owner and repo
owner, repo = GITHUB_REPO.split('/')

# GitHub API URL for fetching PRs
GITHUB_API_URL = f"https://api.github.com/repos/{owner}/{repo}/pulls"

# Headers for the GitHub API request
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Parameters to retrieve merged PRs only, 100 per page (maximum allowed)
params = {
    "state": "all",
    "per_page": 100,
    "page": 1
}

# Dictionary to store PR data
merged_pr_data = {}

# Loop through all the pages to fetch PR data
while True:
    response = requests.get(GITHUB_API_URL, headers=headers, params=params)

    if response.status_code == 401:
        print("Unauthorized: Check your GitHub token.")
        break

    if response.status_code != 200:
        print(f"Failed to fetch PRs: {response.status_code}, Response: {response.text}")
        break

    prs_data = response.json()

    if not prs_data:
        break

    for pr in prs_data:
        if pr['user']['login'] != owner:
            user = pr['user']['login']
            merged_at = pr.get('merged_at')
            title = pr['title']

            if merged_at is not None:
                if user not in merged_pr_data:
                    merged_pr_data[user] = {'count': 0, 'pr_titles': []}

                merged_pr_data[user]['count'] += 1
                merged_pr_data[user]['pr_titles'].append(title)

    params['page'] += 1

# Create a DataFrame from the PR data
df = pd.DataFrame.from_dict(merged_pr_data, orient='index').reset_index()
df.columns = ['name', 'count', 'pr_titles']

# Sort the DataFrame by 'count' in descending order
df_sorted = df.sort_values(by='count', ascending=False).reset_index(drop=True)

def create_markdown(df_sorted):
    markdown = "| Rank | Name       | Count | PR Titles                                             |\n"
    markdown += "|------|------------|-------|-------------------------------------------------------|\n"

    for i, row in df_sorted.iterrows():
        pr_titles_str = '<br>'.join([f"- {title}" for title in row['pr_titles']]) or "No titles"
        markdown += f"| {i+1}    | {row['name']} | {row['count']}     | {pr_titles_str} |\n"
    
    return markdown

markdown_output = create_markdown(df_sorted)

output_file = "ranking_output.md"
with open(output_file, "w") as file:
    file.write(markdown_output)

print(f"Markdown file saved as '{output_file}'")
print(markdown_output)

# Function to fetch closed pull requests
def fetch_pull_requests():
    url = f"https://api.github.com/repos/{GITHUB_REPO}/pulls?state=closed"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def main():
    pr_data = fetch_pull_requests()
    pr_stats = {}
    detailed_prs = []

    for pr in pr_data:
        user = pr['user']['login']
        title = pr['title']
        merged_at = pr.get('merged_at')

        pr_details = {
            'title': title,
            'merged_at': merged_at,
            'url': pr['html_url'],
            'user': user
        }
        detailed_prs.append(pr_details)

        if user in pr_stats:
            pr_stats[user] += 1
        else:
            pr_stats[user] = 1

    with open('src/scripts/pr_stats.json', 'w') as f:
        json.dump({'users': pr_stats, 'detailed_prs': detailed_prs}, f, indent=4)

if __name__ == "__main__":
    main()
