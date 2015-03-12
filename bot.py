#!/usr/bin/env python

import mechanize

domain='cloud.iip.ufrn.br'

br = mechanize.Browser()

br.open('https://' + domain)

#br.form.name = 'https://cloud.iip.ufrn.br/index.php/apps/files/?dir=%2F'
br.select_form(name='login')
br.form['user'] = 'registration'
br.form['password'] = '123'

br.submit()

#for f in br.forms():
#	print f

#br.form.pop()

for i in br.response().read().split('\n'):
	if 'data-requesttoken' in i:
		token = i.split('=')[2][1:-2]

br.select_form(nr=0)

br.form.controls.pop()
br.form.new_control('text', 'Accept', {})
br.form['Accept'] = '*/*'
br.form.new_control('text', 'requesttoken', {})
br.form['requesttoken'] = token
br.form.new_control('text', 'Refer', {})
br.form['Refer'] = 'https://cloud.iip.ufrn.br/index.php/app/files/'
br.form.new_control('text', 'X-Requested-With', {})
br.form['X-Requested-With'] = 'XMLHttpRequest'
#br.form.new_control('text', 'dir', {})
#br.form['dir'] = u'/'
#br.form.new_control('text', 'foldername', {})
#br.form['foldername'] = 'PACHECO'
br.form.action = 'https://cloud.iip.ufrn.br/index.php/apps/files/ajax/list.php?dir=%2F&soft=name&sortdirection=asc'
br.form.method = 'GET'
br.form.new_control('text', 'dir', {})
br.form['dir'] = u'/'

br.submit()

for i in br.response().read().split('\n'):
	if '\"data\":' in i:
		print i

"""
for i in br.response().read().split('\n'):
	if 'data-requesttoken' in i:
		token = i.split('=')[2][1:-2]

br.select_form(nr=0)

br.form.controls.pop()
br.form.new_control('text', 'Accept', {})
br.form['Accept'] = '*/*'
br.form.new_control('text', 'requesttoken', {})
br.form['requesttoken'] = token
br.form.new_control('text', 'Refer', {})
br.form['Refer'] = 'https://cloud.iip.ufrn.br/index.php/app/files/'
br.form.new_control('text', 'Origin', {})
br.form['Origin'] = 'https://cloud.iip.ufrn.br'
br.form.new_control('text', 'X-Requested-With', {})
br.form['X-Requested-With'] = 'XMLHttpRequest'
br.form.new_control('text', 'Content-Type', {})
br.form['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
br.form.new_control('text', 'dir', {})
br.form['dir'] = u'/'
br.form.new_control('text', 'foldername', {})
br.form['foldername'] = 'PACHECO'
br.form.action = 'https://cloud.iip.ufrn.br/index.php/apps/files/ajax/newfolder.php'

for line in br.response().read().split('\n'):
	print line

#br.submit()


for i in br.response().read().split('\n'):
	if 'data-requesttoken' in i:
		token = i.split('=')[2][1:-2]
br.select_form(nr=0)
br.form.controls.pop()
br.form.new_control('text', 'Accept', {})
br.form['Accept'] = '*/*'
br.form.new_control('text', 'requesttoken', {})
br.form['requesttoken'] = token
br.form.new_control('text', 'Refer', {})
br.form['Refer'] = 'https://cloud.iip.ufrn.br/index.php/app/files/'
br.form.new_control('text', 'Origin', {})
br.form['Origin'] = 'https://cloud.iip.ufrn.br'
br.form.new_control('text', 'X-Requested-With', {})
br.form['X-Requested-With'] = 'XMLHttpRequest'
br.form.new_control('text', 'Content-Type', {})
br.form['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
br.form.new_control('text', 'dir', {})
br.form['dir'] = u'/'
br.form.new_control('text', 'foldername', {})
br.form['foldername'] = 'PACHECO'
br.form.action = 'https://cloud.iip.ufrn.br/index.php/apps/files/ajax/newfolder.php'

print br.form

br.submit()
"""

br.close()
