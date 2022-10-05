import requests
import random
from bs4 import BeautifulSoup

episode_name = 'Slumber_Party_Panic'

transcript_url = f'https://adventuretime.fandom.com/wiki/{episode_name}/Transcript'
response = requests.get(transcript_url)
soup = BeautifulSoup(response.text, 'html.parser')

transcript_lines = soup.find_all('dl')

lines = []

for line in transcript_lines:
    line_str = line.find('dd').text.strip()
    
    lines.append(line_str)

line_print = random.choice(lines)
line_print = line_print[line_print.find(':') + 1:]