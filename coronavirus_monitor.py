import requests


class Monitor:
    def __init__(self):
        self.country_name = ''
        self.total_cases = ''
        self.new_cases = ''
        self.active_cases = ''
        self.total_deaths = ''
        self.new_deaths = ''
        self.total_recovered = ''
        self.serious_critical = ''
        self.region = ''
        self.total_cases_per1m = ''
        self.record_date = ''
        self.record_time = ''

    def get_update_by_country(self, country_name: str):
        url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/latest_stat_by_country.php"
        querystring = {"country": country_name}
        headers = {
            'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
            'x-rapidapi-key': "a5a7ccac10msh7975ebe5e85309ep1a3bb9jsnab9757a4c710"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        self.country_name = response.json()['latest_stat_by_country'][0]['country_name']
        self.total_cases = response.json()['latest_stat_by_country'][0]['total_cases']
        self.new_cases = response.json()['latest_stat_by_country'][0]['new_cases']
        self.active_cases = response.json()['latest_stat_by_country'][0]['active_cases']
        self.total_deaths = response.json()['latest_stat_by_country'][0]['total_deaths']
        self.new_deaths = response.json()['latest_stat_by_country'][0]['new_deaths']
        self.total_recovered = response.json()['latest_stat_by_country'][0]['total_recovered']
        self.serious_critical = response.json()['latest_stat_by_country'][0]['serious_critical']
        self.region = response.json()['latest_stat_by_country'][0]['region']
        self.total_cases_per1m = response.json()['latest_stat_by_country'][0]['total_cases_per1m']
        self.record_date, self.record_time = response.json()['latest_stat_by_country'][0]['record_date'].split(' ')

    def print_data_on_console(self):
        print(f'''
            Country: {self.country_name}
            Total cases: {self.total_cases}
            New Cases: {self.new_cases}
            Active Cases: {self.active_cases}
            Total Deaths: {self.total_deaths}
            New Deaths: {self.new_deaths}
            Total Recovered: {self.total_recovered}
            Seriously critical: {self.serious_critical}
            Region: {self.region}
            Total Cases Per Million: {self.total_cases_per1m}
            Recorded Data: {self.record_date}
            Recorded Time: {self.record_time}
        ''')

    def return_data_as_string(self):
        return f'''
            Country: {self.country_name}
            Total cases: {self.total_cases}
            New Cases: {self.new_cases}
            Active Cases: {self.active_cases}
            Total Deaths: {self.total_deaths}
            New Deaths: {self.new_deaths}
            Total Recovered: {self.total_recovered}
            Seriously critical: {self.serious_critical}
            Region: {self.region}
            Total Cases Per Million: {self.total_cases_per1m}
            Recorded Data: {self.record_date}
            Recorded Time: {self.record_time}
        '''

    def return_data_as_list(self):
        return [
            self.country_name,
            self.total_cases,
            self.new_cases,
            self.active_cases,
            self.total_deaths,
            self.new_deaths,
            self.total_recovered,
            self.serious_critical,
            self.region,
            self.total_cases_per1m,
            self.record_date,
            self.record_time
        ]
