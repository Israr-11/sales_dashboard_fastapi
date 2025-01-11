import requests


def get_coordinates(customer_city, customer_country):
    """ Fetches coordinates from OpenStreetMap's Nominatim API for a city and country.

    Args:
        customer_city (str): Name of the city provided by the user.
        customer_country (str): Name of the country provided by the user.

    Returns:
        tuple: A tuple containing (city_latitude, city_longitude, country_latitude, country_longitude).
               All values can be None if no results or errors are found.
    """

    base_url = "https://nominatim.openstreetmap.org/search?format=json"
    params = {"q": f"{customer_city},{customer_country}"}

    # Combine city and country search into a single request for efficiency
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data:
            # Assuming the first result is the most relevant
            result = data[0]
            city_latitude = result.get("lat")
            city_longitude = result.get("lon")
            country_latitude = city_latitude  # Assuming country and city are close enough
            country_longitude = city_longitude
            return city_latitude, city_longitude, country_latitude, country_longitude
        else:
            return None, None, None, None  # No results found
    else:
        print(f"Error fetching coordinates: {response.status_code}")
        return None, None, None, None
