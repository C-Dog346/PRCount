# Multitudes CLI 

## Overview 

Multitudes CLI is a Python command-line interface (CLI) tool designed to access the GitHub API and count the number of open pull requests in a specified repository. This tool provides a simple way to monitor the activity in your GitHub repositories by fetching the relevant data from GitHub's API.

## Prerequisites

Before using Multitudes CLI, ensure that you have the following:

**Python**: Make sure you have Python installed on your system. If not, you can download and install it from python.org.

**Requests Library**: Multitudes CLI uses the requests library to make HTTP requests. If you haven't installed it yet, you can install it using the following command:

```bash
pip install requests 
```

## How to Use Multitudes CLI

1. **Clone the Repository**:

```bash
git clone <repository-url>
```

2. **Navigate to the Project Directory**:

```bash
cd multitudes-cli
```

3. **Run the CLI**:
```bash
python multitudes.py
```
*Alternatively, you could run the code through an IDE or similarly appropriate application of your choice*


4. **Follow the Prompts**:

- Enter the repository owner's username when prompted.
- Enter the repository name when prompted.
- Multitudes CLI will query the specified GitHub repository for open pull requests and display the total number of open pull requests.

## Code Overview
The multitudes.py script in this repository accesses the GitHub API to fetch open pull requests from a specified repository. It does this across multiple pages of pull requests to ensure that all pull requests are counted.

The script prompts the user for the repository owner's username and the repository name. It then queries the GitHub API and prints the total number of open pull requests in the specified repository.