from scrapper.scrappercovid import get_instance_bot



htkbot = get_instance_bot()


htkbot.download_csv_page(False)
xd = htkbot.validate_config_csv()
print(xd)


