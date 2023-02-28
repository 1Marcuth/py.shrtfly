from shrtfly import AsyncShrtFly, ADULT, MAINSTREAM

shortener = AsyncShrtFly("8d781f989cad1ad9b2a5a648ac5b7293")

# url_info = shortener.shorten(
#     url="https://marcuth.github.io/", # URL you want to shorten
#     alias="url-alias", # URL alias
#     is_text_format=False, # Whether the result from the server is going to be text
#     ads_type=MAINSTREAM # Ads type, you can define two types, there is no way to define banner and also you don't need to define if you want url with ads
# )

# url_info.get_raw_data() # Result of all 
# url_info.get_shortened_url() # Resulting URL
# url_info.get_status() # Resulting status ("success" | "error")

urls_data = shortener.run([
    ("https://google.com", None, False, None),
    ("https://youtube.com", None, False, None),
    ("https://facebook.com", None, False, None)
])

for url_data in urls_data:
    print(url_data.shortened_url)