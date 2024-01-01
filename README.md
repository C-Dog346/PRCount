# PRCount

A technical test assignment for an internship application.

## Overview 

PRCount is a Python command-line interface (CLI) tool designed to access the GitHub API and count the number of open pull requests in a specified repository. This tool provides a simple way to monitor the activity in your GitHub repositories by fetching the relevant data from GitHub's API.

## Prerequisites

Before using PR Count, ensure that you have the following:

**Python**: Make sure you have Python installed on your system. If not, you can download and install it from python.org.

**Requests Library**: PR Count uses the requests library to make HTTP requests. If you haven't installed it yet, you can install it using the following command:

*DISCLAIMER - this application was developed on Windows and has not been tested on MacOS. It should work on both but you never know...*

```bash
pip install requests 
```

## How to Use PR Count

1. **Clone the Repository**:

```bash
git clone https://github.com/C-Dog346/PRCount
```

2. **Navigate to the Project Directory**:

```bash
cd PRCount
```

3. **Run the CLI**:
```bash
python pr_count.py
```
*Alternatively, you could run the code through an IDE or similarly appropriate application of your choice*


4. **Follow the Prompts**:

- Enter the repository owner's username when prompted.
- Enter the repository name when prompted.
- PRCount will query the specified GitHub repository for open pull requests and display the total number of open pull requests.

## Code Overview
The pr_count.py script in this repository accesses the GitHub API to fetch open pull requests from a specified repository. It does this across multiple pages of pull requests to ensure that all pull requests are counted.

The script prompts the user for the repository owner's username and the repository name. It then queries the GitHub API and prints the total number of open pull requests in the specified repository.
