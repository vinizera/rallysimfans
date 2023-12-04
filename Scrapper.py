from bs4 import BeautifulSoup
import pandas as pd
import requests


class Stage:

    def __init__(self, url):
        self.response = requests.get(url)
        self.txt = self.response.text
        self.soup = BeautifulSoup(self.txt, features="html.parser")

        # Define a dictionary with the attributes you want to match
        attributes = {
            'valign': 'top',
            'align': 'justify',
            'class': 'szdb',
            'style': 'padding:5px; text-align: justify; font-size: 12px;'
        }

        # Use the find() method to find the <td> element with the specified attributes
        self.td = self.soup.find('td', attrs=attributes)

        self.table = self.td.findAll('table')[1]
        self.rows = self.table.findAll('tr')

        self.data = []

        for row in self.rows:
            self.cells = row.findAll('td')
            self.row_data = [cell.get_text(strip=True) for cell in self.cells]
            self.data.append(self.row_data)

        self.stage_title = self.data[0].copy()[0]
        self.headers = self.data[1]
        self.data = self.data[2:]
        self.stage = pd.DataFrame(self.data, columns=self.headers)

    def get_name(self):
        return self.stage_title

    def get_stage_data(self):
        return self.data
