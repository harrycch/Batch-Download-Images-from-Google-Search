from google_images_search import GoogleImagesSearch
import credentials

gis = GoogleImagesSearch(credentials.api_key, credentials.cx)

names = [
'Emma Watsons'
]

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
