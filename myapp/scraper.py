import requests
from bs4 import BeautifulSoup
from .models import Influencer

def parse_data(data):
    created = 0
    for li in data.find_all('li'):
        name = li.find('div', attrs={'class': 'User_vignette_info_name title'}).text
        handle = li.find('div', attrs={'class': 'User_vignette_info_bio'}).find('a').text

        profile_picture = li.find('img').get('src')

        followers = li.find('div', attrs={'class': 'title'}).text
        likes = li.find('div', attrs={'class': 'User_vignette_likes'}).text

        if Influencer.objects.filter(handle=handle).exists() == False:
            Influencer.objects.create(
                handle = handle,
                name = name,
                followers = followers,
                likes = likes,
                profile_picture = profile_picture
            )
            created += 1

    print(f"Job Done, {created} influencers added.")

def start_scrape(region="us"):
    print(f"Region: {region}")
    url = f"https://tokfluence.com/top?limit=100&country={region}"

    response = requests.get(url, timeout=20)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        data = soup.find('div', attrs={'class': 'Landing_influencer_list_element center'}).find('ul')
        parse_data(data)
        return True, "Data saved successfully."

    elif response.status_code == 400:
        return False, "Bad Request Error from API"
    
    elif response.status_code == 404:
        return False, "API source not found"

    elif response.status_code == 500:
        return False, "API Internal Server Error"
    
    return False, "Unknown Error from the API"