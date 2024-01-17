# Getting Started with Python and Git

This guide provides step-by-step instructions for beginners to set up Python and Git/GitHub. Python is a popular programming language, and Git, along with GitHub, is essential for version control and collaboration in software development.

## Basic Python Setup

Before you begin, make sure you are following the instructions for your specific operating system: Windows, macOS, or Linux.

### 1. Checking Python Installation
- **All Operating Systems**: Open the Terminal (or Command Prompt in Windows) and enter `python --version`. This checks if Python is already installed and displays the installed version.
  - If Python is not installed, download it from [Python's official website](https://www.python.org/downloads/).
  - During installation, ensure to select "Add to PATH" if prompted.
  - After installation, verify the installation by typing `python --version` in the terminal again.

### 2. Installing oh-my-zsh (macOS/Linux)
- For a better terminal experience, install [oh-my-zsh](https://ohmyz.sh/#install). Note: This step is optional and specifically for macOS and Linux users.
  - Follow the instructions on the website. You might be prompted to install "Developer tools," which could take some time.
  - After installation, open a new terminal window to see the changes.

### 3. Setting Up Anaconda
- Anaconda is a popular Python distribution for data science and machine learning. It simplifies package and version management, making it easier to manage dependencies for various projects. This is especially beneficial for projects that require specific versions of libraries and Python itself.
  - Download Anaconda from [here](https://www.anaconda.com/download).
  - After installation, open the Terminal and type `conda init` to initialize your conda environment each time you open a terminal window.

### 4. Installing VSCode
- Visual Studio Code (VSCode) is a lightweight but powerful source code editor.
  - Download VSCode from [Visual Studio Code's official website](https://code.visualstudio.com/download).
  - After installation, open VSCode to familiarize yourself with its interface.

### 5. Setting Up GitHub Copilot in VSCode

- GitHub Copilot is an AI-powered code completion tool ($10/month) that can help you write code faster and learn new APIs and languages.

- **Install GitHub Copilot**:
  - In VSCode, go to the Extensions view by clicking on the square icon on the left sidebar.
  - Search for "GitHub Copilot" and install the extension.
  - Once installed, GitHub Copilot will start suggesting code completions as you type in supported languages and files.

- **Using GitHub Copilot**:
  - As you type in your code editor, Copilot will offer suggestions. Press `Tab` to accept a suggestion.
  - You can trigger Copilot manually by typing a comment describing the logic you want to implement and then press `Ctrl` + `Space` (or `Cmd` + `Space` on macOS) to get a code suggestion.


## Basic Git Setup

Git is a distributed version control system, essential for tracking changes in your code and collaborating with others.

### 1. Installing Git
- **macOS**: Use Homebrew, a package manager, to install Git easily.
  - Install Homebrew by following the instructions at [brew.sh](https://brew.sh/).
  - Once Homebrew is installed, enter `brew install git` in the Terminal to install Git.
- **Windows/Linux**: Follow the Git installation guide for your operating system from [Git's official website](https://git-scm.com/downloads).
  - This website provides detailed instructions for downloading and installing Git on Windows and Linux systems.

### 2. Setting Up GitHub
- GitHub is a platform for hosting and collaborating on Git repositories.
  - If you don't have a GitHub account, create one at [github.com/join](https://github.com/join).
  - Set your Git username and commit email as per the guides on GitHub:
    - [Setting your username in Git](https://docs.github.com/en/get-started/getting-started-with-git/setting-your-username-in-git)
      - *Note: Use your personal email so that you can continue using it as long as you need
    - [Setting your commit email address](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address)
  - Create and manage your personal access tokens as described [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

### Cloning a GitHub Repository
- A GitHub repository is where you can store your code, files, and track changes.
  - Create a folder for your projects, e.g., `/Users/yourname/code`.
  - Navigate to this folder in the Terminal with `cd code`.
  - Find a repository on [GitHub](https://github.com/), click the green "Code" button, and copy the HTTPS URL.
  - Clone the repository locally with `git clone [paste your copied link here]`.

### Additional Resources
- For further learning, explore additional Python tutorials and Git/GitHub guides:
  - [Python Tutorials](https://docs.python.org/3/tutorial/)
  - [Git Tutorials](https://git-scm.com/doc)
  - [GitHub Learning Lab](https://lab.github.com/)

### Feedback and Contributions
- Your feedback is valuable to improve this guide. Feel free to contribute or suggest changes by contacting us or submitting a pull request if this guide is hosted on a platform like GitHub.

### Security Best Practices
- Remember to use strong, unique passwords for your accounts and enable two-factor authentication (2FA) for GitHub for added security.

## Congrats, you have successfully set up Python and Git/GitHub on your computer!
