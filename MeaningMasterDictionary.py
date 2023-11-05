import requests

def get_word_definition(word, api_key):
    url = f'https://www.dictionaryapi.com/api/v3/references/sd4/json/{word}?key={api_key}'
    #url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

    print(f"Getting url")

    response = requests.get(url)

    if response.status_code == 200:
        #print(response.content)
        data = response.json()
        print(f"Got data back")
        if isinstance(data, list):
            # print(f"Data is a list")
            if data:
                # Print the first definition for the word
                print(f"Definition of '{word}': {data[0]['shortdef'][0]}")
            else:
                print(f"No definition found for '{word}'.")
        else:
            print("An unexpected response was received from the API.")
    else:
        print(f"Error: Could not retrieve the definition for '{word}'. Status code: {response.status_code}")

if __name__ == "__main__":
    api_key = "Your API key here"
    word = input("Enter a word to look up: ")
    get_word_definition(word, api_key)
