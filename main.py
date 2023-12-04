import Scrapper

url = 'https://rallysimfans.hu/rbr/rally_hotlap.php?centerbox=rsfhotlap&stageid=20'
harwood_forest = Scrapper.Stage(url)

print(harwood_forest.get_stage_data())
