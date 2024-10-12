import os
import json
import pandas as pd
import requests

# Environment variables for GitHub Actions
GITHUB_REPO = os.getenv('GITHUB_REPOSITORY', 'owner/repo')  # Format: 'owner/repo'
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

# Replace with your repository owner and repository name
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

    # Check if the response is successful
    if response.status_code != 200:
        print(f"Failed to fetch PRs: {response.status_code}, Response: {response.text}")
        break

    prs_data = response.json()

    # Break if no more PRs are returned
    if not prs_data:
        break

    # Process each PR in the current page
    for pr in prs_data:
        if pr['user']['login'] != owner:
            user = pr['user']['login']
            merged_at = pr['merged_at']
            title = pr['title']

            # Only consider PRs that have been merged
            if merged_at is not None:
                if user not in merged_pr_data:
                    merged_pr_data[user] = {
                        'count': 0,
                        'pr_titles': []
                    }

                # Increment the count and add the PR title to the list for that user
                merged_pr_data[user]['count'] += 1
                merged_pr_data[user]['pr_titles'].append(title)

    # Move to the next page
    params['page'] += 1

# Create a DataFrame from the PR data
df = pd.DataFrame.from_dict(merged_pr_data, orient='index').reset_index()
df.columns = ['name', 'count', 'pr_titles']

# Sort the DataFrame by 'count' in descending order
df_sorted = df.sort_values(by='count', ascending=False).reset_index(drop=True)

# Generate markdown format for ranking
def create_markdown(df_sorted):
    markdown = "| Rank | Name       | Count | PR Titles                                             |\n"
    markdown += "|------|------------|-------|-------------------------------------------------------|\n"

    for i, row in df_sorted.iterrows():
        # Format the PR titles as a list with bullet points
        pr_titles_str = '<br>'.join([f"- {title}" for title in row['pr_titles']])
        markdown += f"| {i+1}    | {row['name']} | {row['count']}     | {pr_titles_str} |\n"
    
    return markdown

# Generate the markdown output
markdown_output = create_markdown(df_sorted)

# Save the markdown output as a .md file
output_file = "ranking_output.md"
with open(output_file, "w") as file:
    file.write(markdown_output)

# Print a confirmation message
print(f"Markdown file saved as '{output_file}'")

# Print the markdown for verification (optional)
print(markdown_output)
