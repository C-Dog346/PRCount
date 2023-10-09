"""used to access api"""
import requests

def count_open_pull_requests(owner, repo):
    """count number of open prs at a given repo"""
    page = 1
    total_pull_requests = 0

    while True:
        url = f'https://api.github.com/repos/{owner}/{repo}/pulls?state=open&page={page}'
        response = requests.get(url, timeout=5)
               
        if response.status_code == 200:
            pull_requests = response.json()
            num_pull_requests = len(pull_requests)
            # If there are no more pull requests on the current page, exit the loop
            if num_pull_requests == 0:
                break

            total_pull_requests += num_pull_requests

            # Move to the next page for the next iteration
            page += 1
        else:
            print(f'Failed to retrieve data from GitHub API. Status code: {response.status_code}')
            break

    print(f'Total number of open pull requests: {total_pull_requests}')

if __name__ == '__main__':
    print('Welcome to Multitudes CLI! Let’s process some Github Data! Enjoy the dog')
    print('''
          ^..^      /
          /_/\_____/
             /\   /\\
            /  \ /  \\
            ''')


    ownerInput = input('Who is the repo owner?\n\t')
    repoInput = input('What is the repo name?\n\t')

    print(f'Excellent! Querying {ownerInput}/{repoInput} for open PRs!')

    count_open_pull_requests(ownerInput, repoInput)
