import urllib.request

link = 'https://api.github.com/users/mycahh/repos'

urllib.request.urlretrieve(link, "./src/helpers/repositories.json")