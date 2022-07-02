const http = require('http');
const fs = require('fs');
const url = require('url');



const data = fs.readFileSync('${__dirname}/dev-data/data.json','utf-8');
const dataObj = JSON.parse(data);

const server = http.createServer(function(req, res){
    const pathName = req.url;
    if(pathName === '/' || pathName === '/overview')
        res.end('This is the OVERVIEW');
    elseif (pathName = '/product'){
        res.end('this is the PRODUCT');
    }else{
        res.writeHead(404, {
            'Content-type' : 'text/html' ,
            'my-own-header' : 'hello-world'
        });
        res.end('<h1>Page not found</h1>');

    }
});

server.listen(8000, '127.0.0.1', function(){
    console.log('Listening to request on port : 8000');
});