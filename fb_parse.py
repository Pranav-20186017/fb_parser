import io
import re
from bs4 import BeautifulSoup
import os
import hashlib
import random
import wget
import shutil
def find_nth(haystack, needle, n=1):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

links = []
with io.open('fb.html', 'r', encoding='utf-8') as fp:
	soup = BeautifulSoup(fp, features="html.parser")

	scripts = soup.find_all('script')

	for script in scripts:
		content = script.getText()
		if 'hd_src' in content:
			times = content.count('hd_src')
			for i in range(1, times+1):
				index = find_nth(content, 'hd_src', i)
				# index = content.find('hd_src', i)
				# end_index = content[index : ].index('"', 2)
				# print()
				links.append(content[index : index+find_nth(content[index:], '"', 2)])


clinks = []
for i in links:
	if 'null' in i:
		clinks.append(i.replace('hd_src:null,sd_src:"',''))
	else:
		clinks.append(i.replace('hd_src:"',''))


new_dir = hashlib.md5(str(int(random.random() * 10 ** 7)).encode('utf-8')).hexdigest()
os.mkdir(new_dir)
os.chdir(new_dir)
dwd = hashlib.md5(str(int(random.random() * 10 ** 7)).encode('utf-8')).hexdigest()
for j in clinks:
	wget.download(j)
shutil.make_archive(dwd, 'zip', new_dir)
print('done')






