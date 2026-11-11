# File Integrity Monitor

This is a Python project I built to practice file integrity monitoring and understand how SHA-256 hashing can be used to detect unauthorized changes to files.

## Features

- Calculate SHA-256 hashes for files.
- Create an initial baseline hash.
- Monitor files continuously.
- Check file integrity every 3 seconds.
- Detect unauthorized modifications.
- Display a critical alert when a change is detected.
- Read files in chunks to handle large files efficiently.

## Requirements

- Python 3.x

No external libraries are required.

## How to Run

Clone the repository:

```bash
git clone https://github.com//file-integrity-monitor.git
```

Move into the project directory:

```bash
cd file-integrity-monitor
```

Run the script:

```bash
python file_integrity_monitor.py
```

Enter the path of the file you want to monitor when prompted.

## How It Works

The program calculates the SHA-256 hash of the selected file and stores it as the baseline.

It then checks the file every 3 seconds by calculating its hash again and comparing it with the original baseline.

If the hashes do not match, the program displays a critical security alert indicating that the file has been modified.

## Technologies Used

- Python
- hashlib
- SHA-256
- time
- File Handling

## Author

**Bashar Almadhaji**
