import tkinter as tk
from tkinter import messagebox, filedialog, scrolledtext
from datetime import datetime
import re

def generate_markdown():
    title = entry_title.get()
    url = entry_url.get()
    difficulty = var_difficulty.get()
    statement = text_statement.get("1.0", tk.END).strip()
    constraint_lines = text_constraints.get("1.0", tk.END).strip().splitlines()
    example_lines = text_examples.get("1.0", tk.END).strip().split('\n\n')

    if not (title and url and difficulty and statement and example_lines):
        messagebox.showerror("Error", "Please fill out all fields before generating the markdown.")
        return

    examples = []
    for example in example_lines:
        parts = example.strip().split("\n")
        if len(parts) == 3:
            examples.append({
                "input": parts[0],
                "output": parts[1],
                "explanation": parts[2]
            })
        else:
            messagebox.showerror("Error", "Each example must have 3 lines: input, output, explanation.")
            return

    badge_url = f"https://img.shields.io/badge/Difficulty-{difficulty}-" + (
        "green" if difficulty.lower() == "easy" else "orange" if difficulty.lower() == "medium" else "red"
    ) + ".svg"

    md_lines = [f"# [{title}]({url})\n", f"![Difficulty]({badge_url})\n", f"\n_Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_\n",]

    md_lines.append("## 📝 Problem Statement\n")
    md_lines.append(statement + "\n")

    md_lines.append("## 📊 Examples\n")
    for i, ex in enumerate(examples, 1):
        md_lines.append(f"### ✅ Example {i}")
        md_lines.append("\n```\n" + ex["input"] + "\n" + ex["output"] + "\n" + ex["explanation"] + "\n```\n")

    md_lines.append("## 📌 Constraints\n")
    for c in constraint_lines:
        md_lines.append(f"- {c}  ")

    content = "\n".join(md_lines)

    file_path = filedialog.asksaveasfilename(
        defaultextension=".md", 
        filetypes=[("Markdown files", "*.md")], 
        initialfile=title.strip().replace("\n", "").replace("\r", "").replace(" ", "_") + ".md"
    )

    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        messagebox.showinfo("Success", f"Markdown file saved as: {file_path}")

app = tk.Tk()
app.title("GFG Problem Markdown Generator")

tk.Label(app, text="Title:").grid(row=0, column=0, sticky="e")
entry_title = tk.Entry(app, width=50)
entry_title.grid(row=0, column=1)

tk.Label(app, text="Problem URL:").grid(row=1, column=0, sticky="e")
entry_url = tk.Entry(app, width=50)
entry_url.grid(row=1, column=1)

tk.Label(app, text="Difficulty:").grid(row=2, column=0, sticky="e")
var_difficulty = tk.StringVar(value="Easy")
tk.OptionMenu(app, var_difficulty, "Easy", "Medium", "Hard").grid(row=2, column=1, sticky="w")

tk.Label(app, text="Problem Statement:").grid(row=3, column=0, sticky="ne")
text_statement = scrolledtext.ScrolledText(app, width=60, height=6)
text_statement.grid(row=3, column=1)

tk.Label(app, text="Examples:").grid(row=4, column=0, sticky="ne")
text_examples = scrolledtext.ScrolledText(app, width=60, height=8)
text_examples.grid(row=4, column=1)

tk.Label(app, text="Constraints:").grid(row=5, column=0, sticky="ne")
text_constraints = scrolledtext.ScrolledText(app, width=60, height=4)
text_constraints.grid(row=5, column=1)

tk.Button(app, text="Generate Markdown", command=generate_markdown).grid(row=6, column=1, pady=10)

app.mainloop()