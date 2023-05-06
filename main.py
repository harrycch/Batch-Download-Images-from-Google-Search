from google_images_search import GoogleImagesSearch
import credentials
import csv

gis = GoogleImagesSearch(credentials.api_key, credentials.cx)

with open('search_keys.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    names = list(map(lambda x: ' '.join(x), data))

    for name in names:
        _search_params = {
            'q': name,
            'num': 1,
            'fileType': 'jpg|png'
            # 'fileType': 'jpg|gif|png',
            # 'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived',
            # 'safe': 'active|high|medium|off|safeUndefined', ##
            # 'imgType': 'clipart|face|lineart|stock|photo|animated|imgTypeUndefined', ##
            # 'imgSize': 'huge|icon|large|medium|small|xlarge|xxlarge|imgSizeUndefined', ##
            # 'imgDominantColor': 'black|blue|brown|gray|green|orange|pink|purple|red|teal|white|yellow|imgDominantColorUndefined', ##
            # 'imgColorType': 'color|gray|mono|trans|imgColorTypeUndefined' ##
        }

        gis.search(search_params=_search_params, path_to_dir=f"./results/", custom_image_name=f"{name}")    
