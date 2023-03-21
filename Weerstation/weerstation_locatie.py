from weerstation_API_response import api_response
import country_converter


class Location:
    """Set up the variables used"""

    def __init__(self, ws, location):
        # Retrieve the settings and location from the app_file
        self.ws = ws
        self.location = location

        # Set up both latitude and longitude to retrieve in the future for map creation
        self.lat = None
        self.lon = None
        self.time = ''

        # Create a data lib, for all the data retrieved from the API and sorted
        self.data = {}

        self.request_data()

        """Retrieve data from the API based on the the location given and the Settings file"""

    def request_data(self):
        response = api_response(self.ws, self.location)

        # Sort all the data retrieved from the API
        self.sort_data(response)

        """Time to sort all the data retrieved"""

    def sort_data(self, response):
        # Separate current data and simple location data
        for char in response:
            temp_dict = response[char]

            # 'item' is the definition of the data, while 'temp_dict[item]' is the variable retrieved from the API
            for item in temp_dict:

                # if 'item' is in the 'required data' lib, use required data as a definition, not the APIs definition
                if item in self.ws.required_data:
                    self.data[self.ws.required_data[item]] = temp_dict[item]

                    # Separate the 'country' definition to search for a country code, to add to the self.data
                    if item == 'country':
                        country_name = temp_dict[item]
                        print(country_name)
                        # Try retrieving the ISO2 and ISO3 codes from the given country
                        try:
                            code1 = country_converter.convert(names=country_name, to='ISO2')
                            code2 = country_converter.convert(names=country_name, to='ISO3')
                            self.data['Country code'] = f'{code1} / {code2}'
                        # If there is an AttributeError, give the country's name in the terminal
                        # And give the value 'MISSING'
                        except AttributeError:
                            print(country_name)
                            self.data['Country code'] = 'MISSING'

                    # Because 'condition' is a lib, not a value, retrieve the 'text' value instead of the entire lib
                    if item == 'condition':
                        self.data[self.ws.required_data['condition']] = temp_dict['condition']['text']

                    # Save the latitude and longitude in self for future mapping purposes
                    if item == 'lat':
                        self.lat = temp_dict['lat']
                    if item == 'lon':
                        self.lon = temp_dict['lon']

                    # Save the time
                    if item == 'localtime':
                        time = temp_dict['localtime'][-5:]
                        time = time.replace(':', 'h')
                        self.time = time
