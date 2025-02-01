import os

from bs4 import BeautifulSoup
import requests
"""
Колись можно буде доробить :)
"""

class SetupFirstLastNames:
    path_first_male_names_usa = "male_names_usa.txt"
    path_first_female_names_usa = "female_names_usa.txt"
    path_surnames_usa = "surnames_usa.txt"

    path_first_male_names_polish = "male_names_usa.txt"
    path_first_frmale_names_polish = "female_names_usa.txt"

    def get_most_popular_names(self, path_site_names):
        page = requests.get(path_site_names)
        soup = BeautifulSoup(page.text, 'html.parser')

        male_names = []
        female_names = []

        list_of_tr_names = soup.find('table', class_='t-stripe').find('tbody').find_all('tr')

        for i, name in enumerate(list_of_tr_names):
            
            try:
                if i < len(list_of_tr_names) - 1:
                    male_name = name.find_all('td')[1].text
                    female_name = name.find_all('td')[3].text

                    male_names.append(male_name)
                    female_names.append(female_name)

            except Exception as e:
                print(e)
                continue
            
        return {"male_names": male_names, "female_names": female_names}
    

    def get_most_common_surnames(self, path_site_last_names):
        page = requests.get(path_site_last_names)
        soup = BeautifulSoup(page.text, 'html.parser')
        
        surnames = []

        list_of_tr_surnames = soup.find('table', id='myTable').find_all('tr')
        del list_of_tr_surnames[0]
        
        for surname in list_of_tr_surnames:
            try:
                surname = surname.find_all('td')[0].text
                surnames.append(surname)
            except Exception as e:
                print(e)
                continue
        
        return surnames


    def record_scrapping_results_in_file(self, strings, name_file):
        name_folder = "names_and_last_names"

        curent_directory = os.current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.abspath(os.path.join(curent_directory, ".."))
        file_path = os.path.join(parent_dir, name_folder, name_file)

        with open(file_path, "w") as file:
            for i, string in enumerate(strings):
                if i < len(strings) - 1:
                    file.write(string + "\n")
                else:
                    file.write(string)


    def run(self):
        names_usa = self.get_most_popular_names("https://www.ssa.gov/oact/babynames/decades/century.html")
        surnames_usa = self.get_most_common_surnames("https://names.mongabay.com/most_common_surnames.htm")

        self.record_scrapping_results_in_file(names_usa["male_names"], self.path_first_male_names_usa)
        self.record_scrapping_results_in_file(names_usa["female_names"], self.path_first_female_names_usa)
        self.record_scrapping_results_in_file(surnames_usa, self.path_surnames_usa)
        



if __name__ == "__main__":
    setup_first_last_names = SetupFirstLastNames()
    setup_first_last_names.run()