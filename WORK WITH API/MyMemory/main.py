import requests
import json


def get_trans(text):
    url = "https://translated-mymemory---translation-memory.p.rapidapi.com/api/get"

    querystring = {"langpair": "fr|ru", "q": f"{text}", "mt": "1", "onlyprivate": "0", "de": "a@b.c"}

    headers = {
        "X-RapidAPI-Host": "translated-mymemory---translation-memory.p.rapidapi.com",
        "X-RapidAPI-Key": "136e3b2ec2msh3ffcdf1cae7ee7dp1ae7e8jsnfa5735b6a15d"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text



if __name__ == '__main__':
    with open('french_books_reviews.json', 'r', encoding='utf-8') as file:
        out_file = []
        json_file = json.load(file)
        for book in json_file:

            reader_review = book['reader_review']
            print(reader_review)
            translated_text = json.loads(get_trans(reader_review))
            book['reader_review'] = translated_text['responseData']['translatedText']
            out_file.append(book)

            with open('json_data.json', 'w', encoding='utf-8') as outfile:
                outfile.write(str(out_file))

    # print(translated_text['responseData']['translatedText'])
