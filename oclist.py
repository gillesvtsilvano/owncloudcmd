# coding: utf-8
s={"data":{"directory":"\/","files":[{"id":"655005","parentId":"655003","date":"March  5, 2015 16:21","mtime":1425572475000,"icon":"\/core\/img\/filetypes\/folder.svg","name":"documents","permissions":31,"mimetype":"httpd\/unix-directory","size":"23383","type":"dir","etag":"54f8827f8f180"},{"id":"655007","parentId":"655003","date":"March  5, 2015 16:21","mtime":1425572476000,"icon":"\/core\/img\/filetypes\/folder.svg","name":"music","permissions":31,"mimetype":"httpd\/unix-directory","size":"3764804","type":"dir","etag":"54f8827f8f4e8"},{"id":"655009","parentId":"655003","date":"March  5, 2015 16:21","mtime":1425572478000,"icon":"\/core\/img\/filetypes\/folder.svg","name":"photos","permissions":31,"mimetype":"httpd\/unix-directory","size":"678556","type":"dir","etag":"54f8827f8f86e"},{"id":"714167","parentId":"655003","date":"March  9, 2015 19:51","mtime":1425930688000,"icon":"\/core\/img\/filetypes\/folder.svg","name":"testewal","permissions":31,"mimetype":"httpd\/unix-directory","size":"0","type":"dir","etag":"54fdf9c0f2129"},{"id":"714175","parentId":"655003","date":"March  9, 2015 19:54","mtime":1425930853000,"icon":"\/core\/img\/filetypes\/folder.svg","name":"testewal2","permissions":31,"mimetype":"httpd\/unix-directory","size":"823614","type":"dir","etag":"54fdfa65e5da9"},{"id":"655004","parentId":"655003","date":"March  5, 2015 16:21","mtime":1425572475000,"icon":"\/core\/img\/filetypes\/application-pdf.svg","name":"ownCloudUserManual.pdf","permissions":27,"mimetype":"application\/pdf","size":"1761471","type":"file","etag":"54f8827f8ed61"}],"permissions":31},"status":"success"}
s
s['data']
for i in s['data']:
    print i
    
s['data']['files'][0]
s['data']['files'][1]
s['data']['files'][2]
for i in s['data']['files']:
    print i
    
for i in s['data']['files']:
    print i['name']
    
for i in s['data']['files']:
    print i['name'], i['type']
    
for i in s['data']['files']:
    print i['name'] + '\t' + i['type']
    
for i in s['data']['files']:
    print i['type'] + '\t' + i['name']
    
#get_ipython().magic(u'save list_owncloud')
#get_ipython().magic(u'save')
#get_ipython().magic(u'save help')
#get_ipython().magic(u'save')
#get_ipython().magic(u'save %help')
#get_ipython().magic(u'save oclist 1-26')
