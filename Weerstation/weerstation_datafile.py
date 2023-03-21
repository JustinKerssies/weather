class Settings:

    def __init__(self):
        """Static data"""
        # Key and API data
        self.key = '0065e382c75e4980be4114743231603'
        self.base_url = 'http://api.weatherapi.com/v1/current.json'

        # Screen data
        self.fullscreen = False
        self.screen_width = 700
        self.screen_height = 500

        # Map data
        self.zoom = 10
        self.map_width = 400
        self.map_height = 400

        # Naming scheme
        self.required_data = {
            'name': 'Name',
            'country': 'Country',
            'lat': 'Latitude',
            'lon': 'Longitude',
            'localtime': 'Clock',
            'temp_c': 'Temperature (c)',
            'wind_kph': 'Wind speed (kph)',
            'pressure_mb': 'Air pressure (hPa)',
            'precip_mm': 'Rain (mm)',
            'cloud': 'Clouds (%)',
            'humidity': 'Humidity (%)',
            'feelslike_c': 'Feelings temp (c)',
            'gust_kph': 'Gust speed (kph)',
            'condition': 'Current weather'
        }
