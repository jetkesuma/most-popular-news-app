import requests
from bs4 import BeautifulSoup


def data_extraction():
    """
    1. SBY tidak masalah jika Jokowi tidak suka dengan anies baswedan
    2. Video: Bangunan 13 lantai Runtuh di Mesir, 4 Orang Terluka
    3. Prabowo mendadak dipanggil jokowi, Gelar pertemuan Tertutup di Istana
    4. Surya Paloh yakin anies tak akan jadi tersangka jelang pilpres 2024
    5. Bahas Politik, Prabowo ditanya jokowi soal rencana ke depan
    6. Erick thohir Ungkap kekurangan JIS untuk Venue Piala Dunia U-175
    :return:
    """
    try:
        content = requests.get('https://www.cnnindonesia.com/')
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        one = soup.find('div', {'class': 'headline__terpopuler-list'})

        result = dict()
        result['one'] = one.text


        return result
    else:
        return None


def show_data(result):
    if result is None:
        print("Cant Show data")
        return
    print('Most Popular News at CNN Indonesia Update')
    print(f"Most Popular News at CNN Indonesia is {result['one']}")
