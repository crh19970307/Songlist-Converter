# coding=utf-8
'''
@author: comwrg
@license: MIT
@time : 2017/05/25 14:12
@desc : 
'''
import requests, json

def getList(url):
    '''

    :param url: 
    :return: [(歌名, 歌手, 专辑), ...]
    '''
    headers = {'content-type': 'application/json',
			           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
    
    id = url[url.find('id=')+len('id='):]
    url = 'http://music.163.com/api/playlist/detail?id='+id
    r = requests.get(url,headers=headers)
    data = json.loads(r.text)
    l = []
    for track in data['result']['tracks']:
        songname = track['name']

        artistsname = ''
        for artist in track['artists']:
            artistsname += artist['name'] + '/'
        artistsname = artistsname[:-1]
        # print artistsname

        albumname = track['album']['name']
        l.append((songname, artistsname, albumname))
    return l



if __name__ == '__main__':
    print getList('http://music.163.com/#/playlist?id=98176052')
