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
    result = dict()
    result['one'] = 'SBY tidak masalah jika Jokowi tidak suka dengan anies baswedan'
    result['two'] = 'Video: Bangunan 13 lantai Runtuh di Mesir, 4 Orang Terluka'
    result['three'] = 'Prabowo mendadak dipanggil jokowi, Gelar pertemuan Tertutup di Istana'
    result['four'] = 'Surya Paloh yakin anies tak akan jadi tersangka jelang pilpres 2024'
    result['five'] = 'Bahas Politik, Prabowo ditanya jokowi soal rencana ke depan'
    result['six'] = 'Erick thohir Ungkap kekurangan JIS untuk Venue Piala Dunia U-17'

    return result

def show_data(result):
    print('Most Popular News at CNN Indonesia')
    print(f"Most Popular News at CNN Indonesia Number 1 is {result['one']}")
    print(f"Most Popular News at CNN Indonesia Number 2 is {result['two']}")
    print(f"Most Popular News at CNN Indonesia Number 3 is {result['three']}")
    print(f"Most Popular News at CNN Indonesia Number 4 is {result['four']}")
    print(f"Most Popular News at CNN Indonesia Number 5 is {result['five']}")
    print(f"Most Popular News at CNN Indonesia Number 6 is {result['six']}")
