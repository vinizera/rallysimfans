from bs4 import BeautifulSoup
import pandas as pd
import requests


# function to get stage name and its data
def get_stage(url):
    response = requests.get(url)
    txt = response.text
    soup = BeautifulSoup(txt, features="html.parser")

    # Define a dictionary with the attributes you want to match
    attributes = {
        'valign': 'top',
        'align': 'justify',
        'class': 'szdb',
        'style': 'padding:5px; text-align: justify; font-size: 12px;'
    }

    # Use the find() method to find the <td> element with the specified attributes
    td = soup.find('td', attrs=attributes)

    table = td.findAll('table')[1]
    rows = table.findAll('tr')

    data = []

    for row in rows:
        cells = row.findAll('td')
        row_data = [cell.get_text(strip=True) for cell in cells]
        data.append(row_data)

    stage_title = data[0].copy()[0]
    headers = data[1]
    data = data[2:]
    stage = pd.DataFrame(data, columns=headers)
    return stage_title, stage
