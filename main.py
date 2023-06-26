"""
the most popular news viewer application at cnnindonesia.com
"""
from mostpopularnewscnn import data_extraction, show_data

if __name__ == '__main__':
    print('Main Application')
    result = data_extraction()
    show_data(result)
