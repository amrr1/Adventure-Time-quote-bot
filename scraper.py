import requests
import random
import re
from bs4 import BeautifulSoup

main_page_url = 'https://adventuretime.fandom.com/wiki/Category_talk%3ATranscripts'
response = requests.get(main_page_url)
soup = BeautifulSoup(response.text, 'html.parser')

main_page = soup.find(id='mw-content-text')


def get_episode_info(episode_table_row):
    # Table data has 2 parts
    table_data = episode_table_row.find_all('td')
    a_tag = table_data[0].a
    metadata = table_data[1].text
    
    # link to episode transcript
    try:
        link = main_page
        link += a_tag['href'] if a_tag['href'].startswith('/') else '/' + a_tag['href']
    except:
        link = None
        
    # title of episode
    try:
        title = a_tag['title']
    except:
        title = None
    
    # Metadata about transcript
    try:
        created_transcript = metadata.split('/')[0]
    except:
        created_transcript = None
    
    # All info
    episode_info = {
        'metadata': metadata,
        'transcript_link': link,
        'episode_title': title
    }
    return episode_info

web_links = soup.select('a')
episode_links = []

for web_link in web_links: 
    if web_link['href'][0:5] == '/wiki' and web_link['href'][-10:] == 'Transcript':
        episode_links.append(web_link['href']) 


#print(episode_links)

selected_episode = random.choice(episode_links)
print(selected_episode)
transcript_url = f'https://adventuretime.fandom.com{selected_episode}'
response = requests.get(transcript_url)
soup = BeautifulSoup(response.text, 'html.parser')

lines = []
try: 
    transcript_lines = soup.find_all('dl')
    for line in transcript_lines:
        line_str = line.find('dd').text.strip()
        
        lines.append(line_str)
except:
    transcript_lines = soup.find_all('p', text = True)
    for line in transcript_lines:
        line_str = line.find('p').text.strip()
        
        lines.append(line_str)




i = 0
while i == 0: 
    line_print = random.choice(lines)
    if line_print[0] != '[': 
        i += 1
        person = line_print[0:line_print.find(':')]
        line_print = line_print[line_print.find(':') + 1:]
        line_print = re.sub("[\(\[].*?[\)\]]", "", line_print)

print(line_print)