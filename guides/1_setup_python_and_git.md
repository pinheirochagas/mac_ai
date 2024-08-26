
# Getting Started with Python and Git

This guide provides step-by-step instructions for beginners to set up Python and Git/GitHub. Python is a popular programming language, and Git, along with GitHub, is essential for version control and collaboration in software development.

## Basic Python Setup

Before you begin, make sure you are following the instructions for your specific operating system: Windows, macOS, or Linux.

### 1. Installing oh-my-zsh (macOS/Linux only)
- For a better terminal experience, install [oh-my-zsh](https://ohmyz.sh/#install). Note: This step is optional and specifically for macOS and Linux users.
- Follow the instructions on the website. You might be prompted to install "Developer tools," which could take some time.
- After installation, open a new terminal window to see the changes.

### 2. Setting Up Anaconda
- Anaconda is a popular Python distribution for data science and machine learning. It simplifies package and version management, making it easier to manage dependencies for various projects. This is especially beneficial for projects that require specific versions of libraries and Python itself.
- Follow the directions for your operating system to [install Anaconda](https://docs.anaconda.com/anaconda/install/).
- Use the "Graphical install" directions if you are not familiar with the terminal, or the "Command line install" directions if you are familiar.

### 3. Installing VSCode
- Visual Studio Code (VSCode) is a lightweight but powerful source code editor.
- Download VSCode from [Visual Studio Code's official website](https://code.visualstudio.com/download).
- After installation, open VSCode to familiarize yourself with its interface.
- When working on a project, open a GitHub repository folder in a code window so you have everything you need at your fingertips.

### 4. Setting Up GitHub Copilot in VSCode (**No longer recommended for UCSF security reasons**)

- GitHub Copilot is an AI-powered code completion tool ($10/month) that can help you write code faster and learn new APIs and languages.

- **Install GitHub Copilot**:
  - In VSCode, go to the Extensions view by clicking on the square icon on the left sidebar.
  - Search for "GitHub Copilot" and install the extension.
  - Once installed, GitHub Copilot will start suggesting code completions as you type in supported languages and files.

- **Using GitHub Copilot**:
  - As you type in your code editor, Copilot will offer suggestions. Press `Tab` to accept a suggestion.
  - You can trigger Copilot manually by typing a comment describing the logic you want to implement and then pressing `Ctrl` + `Space` (or `Cmd` + `Space` on macOS) to get a code suggestion.

## Basic Git Setup

Git is a distributed version control system, essential for tracking changes in your code and collaborating with others.

### 1. Installing Git
- **macOS**: Use Homebrew, a package manager, to install Git easily.
  - Install Homebrew by following the instructions at [brew.sh](https://brew.sh/).
  - Once Homebrew is installed, enter `brew install git` in the Terminal to install Git.
- **Windows/Linux**: Follow the Git installation guide for your operating system from [Git's official website](https://git-scm.com/downloads).
  - This website provides detailed instructions for downloading and installing Git on Windows and Linux systems.

### 2. Requesting a GitHub Enterprise Account
- **What is GitHub?**
  - GitHub is a platform for version control and collaboration, used to host and manage code repositories.
- **Why Choose GitHub Enterprise?**
  - GitHub Enterprise is a more secure option than a personal GitHub account, especially for handling sensitive or proprietary information. It offers enhanced security features, including better control over access and more robust monitoring capabilities.
  - For UCSF-related projects, it is recommended to use a UCSF GitHub Enterprise account to ensure compliance with institutional policies and data protection standards.

- **How to Request a GitHub Enterprise Account**:
  - Visit the following [UCSF's IT services link](https://it.ucsf.edu/service/github-enterprise-cloud?check_logged_in=1).
  - Click on the “GitHub Account Request Form” link.
  - Choose the "User account on-premises" option to request access to the UCSF's secure GitHub Enterprise environment.

### 3. Setting up your GitHub Credentials
  - Set your Git username and commit email as per the guides on GitHub:
  - [Setting your username in Git](https://docs.github.com/en/get-started/getting-started-with-git/setting-your-username-in-git)
  - [Setting your commit email address](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address)
- Create and manage your personal access tokens as described [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

### 4. Cloning a GitHub Repository for the First Time
  - A GitHub repository is where you can store your code, files, and track changes.
  - Cloning is the process of creating a local copy of a remote repository to your own computer. When you clone a repository, you're copying all its contents—including the entire version history and all branches—to your local machine. This allows you to work on the project independently, make changes, and then sync those changes back with the remote repository when you're ready.
  - 1. Create a folder for your projects, e.g., `/Users/yourname/code`.
  - 2. Navigate to this folder in the Terminal with `cd code`.
  - 3. Find the repository on [GitHub](https://github.com/) or [UCSF GitHub](https://git.ucsf.edu/) that you need to clone, click the green "Code" button, and copy the HTTPS URL.
  - 4. Clone the repository locally with `git clone [paste your copied link here]`.

## Versa Chat and API

**Versa Chat** is a secure, UCSF-deployed chat platform that uses large language models for safe and efficient collaboration, even with sensitive data.

**Versa API** provides programmatic access to these large language models, which can be useful for automating data processing tasks or integrating natural language processing capabilities into your applications.

### 1. Requesting Access to UCSF Versa Chat and API
  - Visit the following [UCSF Versa Chat and API link](https://ai.ucsf.edu/platforms-tools-and-resources/versa-chat-and-api) and locate the section for "Request access now."
  - Complete the access request form to gain permissions to use these tools for UCSF-related projects, ensuring compliance with data security protocols.

### 2. You will be prompted to complete a short AI Safety Course, after which you will be granted access to the tools.

## Additional Resources
- For further learning, explore additional Python tutorials and Git/GitHub guides:
  - [Python Tutorials](https://docs.python.org/3/tutorial/)
  - [Git Tutorials](https://git-scm.com/doc)
  - [GitHub Learning Lab](https://lab.github.com/)
