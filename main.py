import csv
import json

from bs4 import BeautifulSoup

# Replace 'html_content' with your actual HTML content
HTML_CONTENT = """
<div class="members-3WRCEx......
"""

# Discord Status pruning
discord_statuses = ['Online', 'Idle', 'Do Not Disturb']
for status in discord_statuses:
    HTML_CONTENT = HTML_CONTENT.replace(f', {status}', '')

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(HTML_CONTENT, 'html.parser')

# Find all elements with the specified classes
id_elements = soup.find_all('div', class_='wrapper-3Un6-K')
nickname_elements = soup.find_all('span', class_='username-i5-wv-')

# Initialize lists to store the extracted data
discord_ids = []
discord_nicknames = []

# Extract Discord IDs
for element in id_elements:
    # Get the 'aria-label' attribute
    discord_id = element.get('aria-label')
    if discord_id:
        discord_ids.append(discord_id)

# Extract server nicknames
for element in nickname_elements:
    # Get the text inside the span element
    discord_nickname = element.text.strip()
    if discord_nickname:
        discord_nicknames.append(discord_nickname)

# Combine the IDs and nicknames
result = list(zip(discord_ids, discord_nicknames))


# Output the data in CSV format
with open('discord_users.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['ID', 'Nickname'])
    csv_writer.writerows(result)

# Output the data in JSON format
with open('discord_users.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(result, jsonfile, indent=4, ensure_ascii=False)

# Iterate over the result set
IDX = 1
for discord_id, discord_nickname in result:
    print(f"{IDX:0>2} | {discord_id}, {discord_nickname}")
    IDX += 1
