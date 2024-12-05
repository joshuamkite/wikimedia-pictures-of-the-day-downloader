# Wikimedia Pictures of the Day Downloader

A Python script that downloads all Pictures of the Day from Wikimedia Commons for a specified year page. The script automatically creates a year-based directory and downloads full-resolution images while preserving their original filenames.

**N.B.** It is common for pages to be limited to 200 images. You may need to go to 'next page' to get a second URL to get all images for the year.

## Features

- Downloads all Pictures of the Day from a specified year page
- Handles UTF-8 encoded filenames 
- Creates year-based directories automatically
- Skips already downloaded files
- Shows download progress
- Handles special characters in filenames

## Requirements

- Python 3.6 or higher
- Required Python packages:
  ```
  requests
  beautifulsoup4
  ```

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/wikimedia-pictures-of-the-day-downloader.git
   cd wikimedia-pictures-of-the-day-downloader
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script with the URL of the Pictures of the Day category for your desired year:

```bash
python3 main.py "https://commons.wikimedia.org/wiki/Category:Pictures_of_the_day_(2024)"
```

Note: Make sure to wrap the URL in quotes due to the parentheses in the URL.

The script will:
1. Create a directory named after the year (e.g., "2024")
2. Download all Pictures of the Day for that year
3. Save files with their original, properly decoded filenames
4. Skip any files that have already been downloaded

## Example URLs

- 2024: `https://commons.wikimedia.org/wiki/Category:Pictures_of_the_day_(2024)`
- 2023: `https://commons.wikimedia.org/wiki/Category:Pictures_of_the_day_(2023)`
- 2022: `https://commons.wikimedia.org/wiki/Category:Pictures_of_the_day_(2022)`

## Error Handling

- The script will continue downloading even if individual images fail
- Each error is logged to the console
- Existing files are skipped rather than re-downloaded
- Invalid URLs or years will produce helpful error messages

## Acknowledgments

- Thanks to Wikimedia Commons for providing these beautiful images