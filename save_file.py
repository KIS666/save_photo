import requests, json, time
from datetime import datetime
from tqdm import tqdm
TOKEN_VK=''
VK_USER_ID = ''

count = int(input('Введите кол-во фотографий - '))
def get_foto_data(offset=0, count=5):
	VK_api = requests.get("https://api.vk.com/method/photos.get", 
	params={
		'owner_id': VK_USER_ID,
		'access_token': TOKEN_VK,
		'album_id':'profile',
		'offset': offset,
		'extended': '1',
		'count': count,
		'photo_sizes': 0,
		'v': 5.103
	})
	return json.loads(VK_api.text)

data = get_foto_data()
count_foto = data["response"]["count"]
def named_file(data):
	fotos = []
	for files in data["response"]["items"]:
		file_url = files["sizes"][-1]["url"]
		date = (datetime.utcfromtimestamp(files["date"]).strftime('%d.%m.%Y'))
		filename = f'{files["likes"]["count"]}_{date}.jpeg'
		fotos.append(filename)
		time.sleep(0.1)
		api = requests.get(file_url)
		with open("images/%s" %filename, "wb") as file:
			file.write(api.content)
	for i in tqdm(fotos):
		time.sleep(1)	

def get_foto_max():
	i = 1
	while i <= count:
		if i != 0:
			data = get_foto_data(offset=i, count=count)
			named_file(data)
		i += count

def get_foto():
	data = get_foto_data(offset=0, count=count)
	named_file(data)

		
def main():
	if count > 5: 
		get_foto_max()
	else:
		get_foto()


if __name__ == "__main__":
	main()
	
