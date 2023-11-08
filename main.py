import scrapper

url = 'https://rallysimfans.hu/rbr/rally_hotlap.php?centerbox=rsfhotlap&stageid=20'
name, data = scrapper.get_stage(url)
print(name)
print(data)
