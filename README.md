# Googly – Random Coding Questions CLI

Googly is a Python CLI tool that displays random coding questions from a dataset That have been asked in Google Interviews.
You can choose the number of questions and log your progress automatically.

---

## Installation

0. ** Docker Image : **
```shell
docker pull s3ika/googly:latest
```



2. **Clone the repository and navigate into it:**

```bash
git clone https://github.com/yourusername/Googly.git
cd Googly
```

2. **Install Python dependencies:**

```bash
pip install -r requirements.txt
```

3. **Ensure your dataset exists:**

Make sure `data/google_lcs.csv` is present in the `Googly/data` folder.

---

## Running the Script

Run directly using Python:

```bash
python main.py
```

You will be prompted to select the number of questions, and each question’s ID, title, and difficulty will be displayed. Logs are saved automatically.

---

## Using Googly Globally

You can make `googly` available as a global command on your system.

### Linux / macOS (Zsh, Bash)

1. **Create a launcher script:**

```bash
nvim ~/Googly/googly
```

Add the following:

```bash
#!/bin/zsh
source ~/Googly/env/bin/activate
python ~/Googly/main.py
```

2. **Make it executable:**

```bash
chmod +x ~/Googly/googly
```

3. **Add it to your global PATH or create a symbolic link:**

```bash
sudo ln -s ~/Googly/googly /usr/local/bin/googly
```

4. **Run from anywhere:**

```bash
googly
```

### Windows

1. Open Command Prompt or PowerShell as Administrator.
2. Add the Googly folder path to the system `PATH`.
3. Create a `.bat` file (e.g., `googly.bat`) with this content:

```bat
@echo off
call C:\path\to\Googly\env\Scripts\activate
python C:\path\to\Googly\main.py
```

4. Now you can run `googly` from any terminal window.

---

## Notes

- The CSV file and logs are handled relative to the script folder for global execution.
- Logs are stored in `logs.txt` inside the .googly/logs.txt
- Make sure your virtual environment is activated if running manually.

## Further Improvements
- Adding other companies would be nice
