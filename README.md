# 📑 MarkMyGfG

A simple GUI-based tool to quickly generate clean Markdown (`.md`) files from [GeeksforGeeks](https://www.geeksforgeeks.org/) problem statements. Designed for personal use, GfG-Markdownizer makes it easy to document your DSA journey and maintain a GitHub-friendly problem archive — something that’s widely available for LeetCode but lacking for GfG.

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

1. Download the `MarkMyGfG.exe` file
2. Run the executable (`.exe`) file.
3. Fill out the form with the copied problem details from GfG.
4. Click `Save` – a Markdown file will be created in your desired directory.

### 🐍 Option 2: Run the Python Script

1. Make sure you have **Python 3.10+** installed.
2. Run the script:
   ```
   python markmygfg.py
   ```
> ⚠️ No external dependencies required. This project uses only Python's built-in standard libraries.


## 📄 Sample Markdown Output

~~~
# [Rotate Array](https://www.geeksforgeeks.org/problems/rotate-array-by-n-elements-1587115621/1)

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange.svg)

_Generated on: 2025-06-24 00:00:00_

## 📝 Problem Statement

Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.

Note: Consider the array as circular.

## 📊 Examples

### ✅ Example 1

```
Input: arr[] = [1, 2, 3, 4, 5], d = 2
Output: [3, 4, 5, 1, 2]
Explanation: when rotated by 2 elements, it becomes 3 4 5 1 2.
```

### ✅ Example 2

```
Input: arr[] = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], d = 3
Output: [8, 10, 12, 14, 16, 18, 20, 2, 4, 6]
Explanation: when rotated by 3 elements, it becomes 8 10 12 14 16 18 20 2 4 6.
```

### ✅ Example 3

```
Input: arr[] = [7, 3, 9, 1], d = 9
Output: [3, 9, 1, 7]
Explanation: when we rotate 9 times, we'll get 3 9 1 7 as resultant array.
```

## 📌 Constraints

- 1 <= arr.size(), d <= 105  
- 0 <= arr[i] <= 105

~~~

## 💡 Why Use This?

* No more manual formatting.
* Makes it easy to document problems for revision or GitHub tracking.
* Minimalist but extensible.
* Ideal for students practicing DSA from GfG.


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
