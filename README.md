# API Data Analyzer CLI

A modular, command-line tool for fetching, analyzing, and exporting data from public APIs.
Built with clean architecture principles to demonstrate real-world API handling, data processing, and CLI design in Python.

---

## 🚀 Features

* Fetch data from REST APIs using `requests`
* Support for multiple endpoints (`posts`, `comments`, `users`)
* Query-based filtering (e.g., filter by `userId`)
* Summary statistics generation
* Clean and readable terminal output
* Export results to JSON files
* Modular, scalable project structure

---

## 🧠 Project Motivation

This project demonstrates how to move from simple API scripts to a **structured, production-style CLI tool**.

It showcases:

* API client design
* Data processing and aggregation
* Separation of concerns (fetch, analyze, format, export)
* CLI-based workflows

---

## 🏗️ Project Structure

```
api-data-analyzer-cli/
│
├── main.py
├── requirements.txt
├── README.md
│
├── data/
│   └── (exported JSON files)
│
├── toolkit/
│   ├── __init__.py
│   └── analyzer.py
│
└── utils/
    ├── __init__.py
    ├── api_client.py
    ├── formatter.py
    └── file_handler.py
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/sum1tbarua/api-data-analyzer-cli.git
cd api-data-analyzer-cli
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Basic command

```bash
python main.py --endpoint posts
```

---

### Limit results

```bash
python main.py --endpoint posts --limit 3
```

---

### Filter by user

```bash
python main.py --endpoint posts --user 1
```

---

### Show summary

```bash
python main.py --endpoint posts --summary
```

---

### Export data to JSON

```bash
python main.py --endpoint posts --export data/posts.json
```

---

### Combine features

```bash
python main.py --endpoint posts --user 2 --limit 2 --summary --export data/user2_posts.json
```

---

## 📊 Example Output

```
SUMMARY
------------------------------
total_posts: 100
unique_users: 10

RECORDS
------------------------------
ID: 1
User: 1
Title: sunt aut facere repellat...
------------------------------
```

---

## 🔧 Supported Endpoints

| Endpoint | Description       |
| -------- | ----------------- |
| posts    | Blog-style posts  |
| comments | Comments on posts |
| users    | User profiles     |

---

## 🧩 Architecture Overview

The project follows a modular design:

* **main.py** → CLI orchestration
* **api_client.py** → API requests and error handling
* **analyzer.py** → data analysis and summaries
* **formatter.py** → terminal output formatting
* **file_handler.py** → JSON export functionality

---

## 📈 Example Analysis

### Posts

* Total number of posts
* Number of unique users

### Comments

* Total comments
* Unique email count

### Users

* Total users
* Unique companies

---

## 🛠️ Technologies Used

* Python 3
* requests
* argparse
* JSON

---

## 📌 Future Improvements

* Logging system
* Retry mechanisms for API calls
* Support for authenticated APIs
* Pagination handling
* Unit testing
* CLI subcommands (e.g., `fetch`, `analyze`, `export`)

---

## 👤 Author

**Sumit Barua**

M.S. Computer Science, Western Michigan University

---

## ⭐ Acknowledgements

* JSONPlaceholder API for providing mock data
* Open-source Python ecosystem

📄 License

This project is open-source and available under the MIT License.
