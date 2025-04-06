# BeautifulSoup


# Installing and Using BeautifulSoup on Linux Mint

## Step 1: Install Python and pip

Linux Mint comes with Python pre-installed, but you can update it and ensure `pip` is installed:

```bash
sudo apt update
sudo apt install python3 python3-pip
```

## Step 2: Install BeautifulSoup and Dependencies

Use `pip` to install BeautifulSoup and `lxml` (a recommended parser):

```bash
pip install beautifulsoup4 lxml
```

Alternatively, if you need `html.parser`, it's included with Python, but you can install `html5lib` for better HTML handling:

```bash
pip install html5lib
```

## Step 3: Verify Installation

Run Python and try importing BeautifulSoup:

```python
from bs4 import BeautifulSoup
print("BeautifulSoup is installed successfully!")
```

