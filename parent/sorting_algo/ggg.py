import requests
from bs4 import BeautifulSoup

def decode_secret_message(url):
    """
    Retrieves coordinate data from a Google Doc and prints a 2D grid
    of characters to reveal a secret message.
    """
    # 1. Fetch the document content
    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching the URL: {e}")
        return

    # 2. Parse the HTML table data
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    
    if not table:
        print("No table found in the document.")
        return

    grid_data = {}
    max_x = 0
    max_y = 0

    # 3. Iterate through rows, skipping the header row
    rows = table.find_all('tr')[1:]
    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 3:
            try:
                # Extract coordinates and the character
                x = int(cells[0].get_text().strip())
                char = cells[1].get_text().strip()
                y = int(cells[2].get_text().strip())
                
                # Store in a dictionary for easy grid lookup
                grid_data[(x, y)] = char
                
                # Track the boundaries of our grid
                if x > max_x: max_x = x
                if y > max_y: max_y = y
            except (ValueError, IndexError):
                # Skip rows that don't contain valid numeric data
                continue

    # 4. Print the grid
    # We loop from the maximum Y down to 0 because Y=0 is the bottom row
    for y in range(max_y, -1, -1):
        line = ""
        for x in range(max_x + 1):
            # Get the character at (x, y), defaulting to a space if not found
            line += grid_data.get((x, y), " ")
        print(line)

decode_secret_message("https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub")
