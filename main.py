"""
the most popular news viewer application at cnnindonesia.com
"""
import mostpopularnewscnn

if __name__ == '__main__':
    print('Main Application')
    result = mostpopularnewscnn.data_extraction()
    mostpopularnewscnn.show_data(result)
