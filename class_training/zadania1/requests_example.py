import requests


def run_example():
    try:
        response = requests.get("https://github.com/adadasd")
    except requests.RequestException as error:
        print(f"Blad przy polaczeniu: {error}")
        return

    try:
        response = response.raise_for_status()
    except requests.HTTPError as error:
        print(f"Zadanie zakonczone niepowodzeniem: {error}")
        return

    print(response.text)

if __name__ == '__main__':
    run_example()
