# RAM Monitor 🖥️

A lightweight RAM monitoring tool built for Android/Termux.
Tracks memory usage and alerts when RAM is critically high.

## Why I Built This

Running a development environment on a Samsung SM-T585
means dealing with limited RAM. This tool helps me monitor
memory usage and avoid System UI crashes.

## Features

- Real-time RAM usage monitoring
- Critical usage alert at 85%
- Shows total, available, and used memory

## Requirements

- Termux
- Python 3
- psutil

## Installation

```bash
pkg install python-psutil
git clone https://github.com/bodamiruSE/ram-monitor.git
cd ram-monitor
python test_ram.py
```

## Output Example

```
⚠️ your ram in 85% usage!
Total:     1819.78 MB
Available: 205.14 MB
Percent:   88.7% used
```

## License
