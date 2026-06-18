# 📝 Modern To-Do List App

A simple and modern desktop To-Do List application built with Python and Tkinter.

## 🚀 Features

* Add new tasks
* Delete tasks
* Mark tasks as completed
* Automatically save tasks
* Load saved tasks on startup
* Clean and user-friendly GUI
* No external dependencies required

---

## 📸 Screenshot

Add a screenshot of your application here.

```text
screenshots/app.png
```

---

## 🛠️ Technologies Used

* Python 3
* Tkinter
* JSON

---

## 📂 Project Structure

```text
todo-app/
│
├── todo_gui.py
├── tasks.json
├── icon.ico
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/todo-app.git
cd todo-app
```

### Run Application

```bash
python todo_gui.py
```

---

## 📦 Create Executable

Install PyInstaller:

```bash
pip install pyinstaller
```

Build executable:

```bash
pyinstaller --onefile --windowed --icon=icon.ico todo_gui.py
```

The executable will be generated inside:

```text
dist/
```

---

## 💾 Data Storage

Tasks are stored locally in:

```text
tasks.json
```

This file is automatically created when the application runs.

---

## 🎯 Future Improvements

* Dark Mode
* Due Dates
* Task Categories
* Search Tasks
* Priority Levels
* Notifications
* Cloud Synchronization

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Created with Python and Tkinter.

If you like this project, give it a ⭐ on GitHub.
