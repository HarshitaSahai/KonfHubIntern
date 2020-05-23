const apiCallFromNode = require('./NodeJsCall')

const http = require('http')

http.createServer((req, res) => {
        
        if(req.url === "/node"){
            apiCallFromNode.callApi(function(response)
            {
                res.write(response);
                res.end();
               
            });
        }
        
        // res.end();
}).listen(3000);

console.log("service running on 3000 port....");