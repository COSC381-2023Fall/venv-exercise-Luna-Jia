import requests
from bs4 import BeautifulSoup

# Function to fetch the content of a web page
def fetch_webpage(url):
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
    return response.text

# Function to extract and print first 5 headings (h1 tags) from the HTML content
def print_headings(html_content):
    soup = BeautifulSoup(html_content, 'lxml')  # Using lxml parser
    headings = soup.find_all('h1')[:5]  # Getting the first 5 h1 tags
    for idx, heading in enumerate(headings, start=1):
        print(f"Heading {idx}: {heading.get_text().strip()}")

# URL to be scraped (using example.com as a placeholder)
url = 'https://www.bbc.com/'

# Main function
def main():
    try:
        # Fetch the web page content
        html_content = fetch_webpage(url)

        # Print the headings
        print_headings(html_content)

    except requests.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except requests.RequestException as e:
        print(f"An error occurred while fetching the web page: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()
