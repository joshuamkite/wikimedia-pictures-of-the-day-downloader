import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, unquote
import re
import sys


def clean_filename(filename):
    """
    Decode URL-encoded filename to proper UTF-8.

    Args:
        filename (str): URL-encoded filename
    Returns:
        str: Decoded filename
    """
    # Decode URL-encoded characters to proper UTF-8
    decoded = unquote(filename)
    # Replace any remaining problematic characters
    return decoded.replace('/', '_').replace('\\', '_')


def download_pictures_of_the_day(category_url):
    """
    Downloads Pictures of the Day from Wikimedia Commons for a given year's category URL.

    Args:
        category_url (str): URL of the Pictures of the Day category page for a specific year
    """
    # Extract year from URL
    year_match = re.search(r'\((\d{4})\)', category_url)
    if not year_match:
        raise ValueError("Could not find year in URL. URL should contain year in parentheses (YYYY)")

    year = year_match.group(1)
    output_dir = year

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get the page content
    print(f"Fetching images for year {year}...")
    response = requests.get(category_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all gallery items
    gallery_items = soup.find_all('div', class_='gallerytext')

    if not gallery_items:
        print("No images found. The page structure might have changed or the URL might be incorrect.")
        return

    for item in gallery_items:
        try:
            # Find the link to the file
            file_link = item.find('a')
            if not file_link:
                continue

            file_page_url = urljoin('https://commons.wikimedia.org', file_link['href'])

            # Get the file page
            file_page = requests.get(file_page_url)
            file_soup = BeautifulSoup(file_page.content, 'html.parser')

            # Find the original file link
            original_file_div = file_soup.find('div', class_='fullMedia')
            if not original_file_div:
                continue

            original_link = original_file_div.find('a')
            if not original_link:
                continue

            image_url = urljoin('https://commons.wikimedia.org', original_link['href'])

            # Clean and decode the filename
            encoded_filename = os.path.basename(image_url)
            filename = clean_filename(encoded_filename)
            filepath = os.path.join(output_dir, filename)

            # Skip if file already exists
            if os.path.exists(filepath):
                print(f"Skipping {filename} (already exists)")
                continue

            # Download the image
            print(f"Downloading {filename}...")
            image_response = requests.get(image_url)

            # Save the image
            with open(filepath, 'wb') as f:
                f.write(image_response.content)

            print(f"Successfully downloaded {filename}")

        except Exception as e:
            print(f"Error downloading image: {str(e)}")
            continue


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py \"URL\"")
        print("Example: python3 main.py \"https://commons.wikimedia.org/wiki/Category:Pictures_of_the_day_(2024)\"")
        sys.exit(1)

    url = sys.argv[1]
    try:
        download_pictures_of_the_day(url)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()