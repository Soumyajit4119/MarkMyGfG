# 📑 Mark_MyGfG

<p>
  <img src="https://img.shields.io/badge/Language-Python-indigo.svg" />
  <img src="https://img.shields.io/badge/GUI-Tkinter-brown.svg" />
  <img src="https://img.shields.io/badge/Generate-Markdown-black.svg" />
   <img src="https://img.shields.io/badge/Platform-Windows-skyblue.svg" />
  <img src="https://img.shields.io/badge/BuildFor-GeekforGeeks-lightgreen.svg" />
  <img src="https://img.shields.io/badge/License-MIT-bisque.svg" />
</p>

A simple GUI-based tool to quickly generate clean Markdown (`.md`) files from [GeeksforGeeks](https://www.geeksforgeeks.org/) problem statements. Designed for personal use, Mark_MyGfG makes it easy to document your DSA journey and maintain a GitHub-friendly problem archive — something that’s widely available for LeetCode but lacking for GfG.

> ⚠️ This is an early version of the tool. Currently, manual input is required, but powerful automation features are in the roadmap.


## 🖥️ Features

- 📄 GUI interface to input:
  - Problem Title
  - Problem Link
  - Difficulty
  - Problem Statement
  - Examples (one or multiple)
  - Constraints
- 💾 One-click save to generate a formatted Markdown file.
- ✍️ Clean output suitable for GitHub repositories or personal note-keeping.

> 🔧 Built with Python and Tkinter – no external dependencies.


## 🚀 Getting Started

### ✅ Option 1: Run the Executable

1. Download the `Mark_MyGfG.exe` from `dist` folder
2. Run the executable (`.exe`) file.
3. Fill out the form with the copied problem details from GfG.
4. Click `Generate Markdown` – a Markdown file will be created in your desired directory.

### 🐍 Option 2: Run the Python Script

1. Make sure you have **Python 3.10+** installed
2. Download the script, `mark_myGfG.py` from `src` folder
3. Run the script:
   ```
   python mark_myGfG.py
   ```
> ⚠️ No external dependencies required. This project uses only Python's built-in standard libraries.


## 📄 Sample Markdown Code & Output

### 🟣🟠 Markdown Code :
<p>
  <img width="80%" src=./assets/md_codeSnippet.png
</p>

### 🟣🟠 Markdown Output :
<p>
  <img width="80%" src=./assets/md_output.png
</p>

>❗Note : 
> 1. In case of multiple examples, add a blank line after each example and each example should contain input, output and explanation in separate lines.
> 2. Each constraint should start from a new line.

## 🛣️ Roadmap

Planned features for future releases:

* 🔍 **Auto-extract from URL** – Paste the GfG link, auto-fill all fields.
* 🏷️ **Tags Field** – Add #tags for topic-wise filtering on GitHub.
* 🧠 **Markdown Preview** – Live preview before saving the file.
* 🗃️ **GitHub Push Option** – Commit and push Markdown directly to your notes repo.
* 🧩 **Chrome Extension** – One-click export from GeeksforGeeks pages.


## 📄 License & Contributing

This project is licensed under the **MIT License** – see the [LICENSE](./LICENSE) file for full details. Feel free to fork this repo and submit a pull request. Future plans include:
* CLI-only version
* VS Code extension
* Adding support for other platforms (LeetCode, Codeforces)

If this tool saved you time or helped you document your GfG problems, consider giving it a ⭐ and sharing it with others.

---
