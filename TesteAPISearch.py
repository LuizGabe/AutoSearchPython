import requests

params = {
    'access_key': 'dfa4d9bf53d2e05be9c09d4c7927733d',
    'query': 'mcdonalds'
}
url = "https://kgsearch.googleapis.com/v1/entities:search?query=Bill%20Gates&key=[YOUR_API_KEY] HTTP/1.1"



api_result = requests.get('https://api.serpstack.com/search', params)

api_response = api_result.json()

print("Total results: ", api_response['search_information']['total_results'])

for number, result in enumerate(api_response['organic_results'], start=1):
    print("%s. %s") % (number, result['title'])