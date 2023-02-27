from ShrtFly import ShrtFly, NO_ADS, INTERSTITIALS_ADS

shortener = ShrtFly("YOUR API TOKEN HERE")

url_info = shortener.shorten(
    url="https://marcuth.github.io/", # URL you want to shorten
    alias="url-alias", # URL alias
    is_text_format=False, # Whether the result from the server is going to be text
    ads_type=INTERSTITIALS_ADS # Ads type, you can define two types, there is no way to define banner and also you don't need to define if you want url with ads
)

url_info.get_raw_data() # Result of all 
url_info.get_shortened_url() # Resulting URL
url_info.get_status() # Resulting status ("success" | "error")
url_info.get_message() # Resulting message (if the api sent a message)