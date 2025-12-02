# quant-trading-strat

## Project Context

This project was carried out as part of the course *Crypto-currencies and Bitcoin*, taught by Zhe Huang (2024-2025).

## Objective

This project focuses on developing, analyzing, and backtesting quantitative trading strategies for the cryptocurrency market. It aims to explore data-driven approaches to optimize trading performance, manage risk, and gain insights into market behavior.

## Setup / workflow guide (Using Git and `uv`)

This guide provides the necessary steps to set up your environment (`uv`) and outlines the daily workflow (Git).

### 1. First-Time Setup (Do this only once)

These steps configure your local development environment.

1.  **Install `uv`** on your machine
    > open your terminal, then :
    ```bash
    pip install uv
    ```

3.  **Clone the Repository**
    > get to the folder you want the repository to be in (use `cd`), then :
    ```bash
    git clone https://github.com/nphalier29/quant-trading-strat.git
    cd quant-trading-strat
    ```

5.  **Create the Virtual Environment**
    Create an isolated environment (`.venv`) for project dependencies.
    ```bash
    uv venv
    ```

6.  **Install Dependencies**
    Synchronize and install all project dependencies based on the configuration files (`pyproject.toml` or `uv.lock`).
    ```bash
    uv sync
    ```
### 2. Daily Workflow

These are the standard steps for developing and sharing your work with git and `uv`.

1.  **Update Your Code (Pull)**
    Before starting work, retrieve the latest changes from the remote repository.
    ```bash
    git pull
    ```

2. **Install Dependencies**
    Synchronize and install all project dependencies based on the configuration files (`pyproject.toml` or `uv.lock`).
    ```bash
    uv sync
    ```

3. **Add New Packages (If needed)**
    If your work requires a new library (e.g., `scikit-learn`), use `uv add`. This installs the package and updates your configuration files (`pyproject.toml` and `uv.lock`).

    ```bash
    uv add scikit-learn
    ```

4.  **Stage Files (Add)**
    Stage the modified or new files once you are done working on the project.
    ```bash
    git add .
    ```

5.  **Save Changes (Commit)**
    Create a local snapshot of your changes with a descriptive message.
    ```bash
    git commit -m "Briefly describe your changes here"
    ```

6.  **Share Your Work (Push)**
    Send your local changes to the central GitHub repository.
    ```bash
    git push
    ```
