<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">BOOK-RECOMMENDATION-SYSTEM</h1></p>
<p align="center">
	<img src="https://img.shields.io/github/last-commit/Yoyobun1/book-recommendation-system?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/Yoyobun1/book-recommendation-system?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/Yoyobun1/book-recommendation-system?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [🔰 Contributing](#-contributing)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

<text>This project implements a collaborative filtering-based book recommendation system, allowing users to receive personalized book suggestions based on their reading preferences and the preferences of similar users. By leveraging user-item interactions, this system aims to enhance the reading experience and help users discover new books they are likely to enjoy.</text>

---

## 👾 Features

- **Collaborative Filtering Algorithms:** 
  - Utilizes both user-based and item-based collaborative filtering techniques to generate personalized recommendations.

- **Data Collection:** 
  - Implements methods for collecting and preprocessing user ratings and book metadata, ensuring a clean dataset for analysis.

- **Model Training and Evaluation:** 
  - Includes steps for training the recommendation model and evaluating its performance using metrics such as Mean Absolute Error (MAE) and Root Mean Square Error (RMSE).

- **User Interface:** 
  - A simple command-line or web-based interface that allows users to input their book preferences and receive recommendations.

- **Visualizations:** 
  - Data visualizations to display user ratings distribution, recommended books, and model performance.

- **Scalability:** 
  - Designed to handle a growing dataset of users and books, with options to optimize performance.

- **Installation Instructions:** 
  - Detailed guidance on setting up the environment, installing dependencies, and running the system.


---

## 📁 Project Structure

```sh
└── book-recommendation-system/
    ├── Procfile
    ├── README.md
    ├── app.py
    ├── artifacts
    │   ├── book_names.pkl
    │   ├── book_pivot.pkl
    │   ├── final_rating.pkl
    │   └── model.pkl
    ├── datasets
    │   ├── BX-Book-Ratings.csv
    │   ├── BX-Books.csv
    │   └── BX-Users.csv
    ├── model.ipynb
    ├── requirements.txt
    ├── setup.py
    ├── setup.sh
    └── src
        └── __init__.py
```


### 📂 Project Index
<details open>
	<summary><b><code>BOOK-RECOMMENDATION-SYSTEM/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Yoyobun1/book-recommendation-system/blob/master/model.ipynb'>model.ipynb</a></b></td>
				<td><code>❯ Contains the implementation of the collaborative filtering model and training procedures.</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Yoyobun1/book-recommendation-system/blob/master/app.py'>app.py</a></b></td>
				<td><code>❯ The main application file that handles user input and displays book recommendations.
			<tr>
				<td><b><a href='https://github.com/Yoyobun1/book-recommendation-system/blob/master/Procfile'>Procfile</a></b></td>
				<td><code>❯ Defines the commands to run the application on a platform like Heroku</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Yoyobun1/book-recommendation-system/blob/master/setup.sh'>setup.sh</a></b></td>
				<td><code>❯ Script to set up the environment and install necessary dependencies.</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Yoyobun1/book-recommendation-system/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td><code>❯ Lists all the Python packages required to run the application.</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Yoyobun1/book-recommendation-system/blob/master/setup.py'>setup.py</a></b></td>
				<td><code>❯ Contains configuration for packaging and installing the application as a module.</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with book-recommendation-system, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip


### ⚙️ Installation

Install book-recommendation-system using one of the following methods:

**Build from source:**

1. Clone the book-recommendation-system repository:
```sh
❯ git clone https://github.com/Yoyobun1/book-recommendation-system
```

2. Navigate to the project directory:
```sh
❯ cd book-recommendation-system
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```




### 🤖 Usage
Run book-recommendation-system using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


### 🧪 Testing
Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```



## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/Yoyobun1/book-recommendation-system/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/Yoyobun1/book-recommendation-system/issues)**: Submit bugs found or log feature requests for the `book-recommendation-system` project.
- **💡 [Submit Pull Requests](https://github.com/Yoyobun1/book-recommendation-system/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/Yoyobun1/book-recommendation-system
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/Yoyobun1/book-recommendation-system/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=Yoyobun1/book-recommendation-system">
   </a>
</p>
</details>

---

## 🙌 Acknowledgments

- Find dataset at: https://www.kaggle.com/code/jirakst/book-recommendation/data
- Tutorial on the project: https://youtube.com/playlist?list=PLkz_y24mlSJa37r2xNDyEgt0Z4ilHtJ07&si=-jWmvczkGm_Z81Mq

---