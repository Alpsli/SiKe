const express = require('express')
const http = require('http')
const path = require('path')
const app = express()
const url = '192.168.174.171'
const myheaders = { 'content-type': 'application/json-rpc' }
const bodyParser = require('body-parser');
const exec = require('child_process').exec;
const payload = [
    {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
            "cmd": "conf t",
            "version": 1
        },
        "id": 1
    },
    {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
            "cmd": "no ip route 3.3.3.0/24 5.5.5.2",
            "version": 1
        },
        "id": 2
    },
    {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
            "cmd": "ip route 3.3.3.0/24 10.10.10.1",
            "version": 1
        },
        "id": 3
    },
    {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
            "cmd": "exit",
            "version": 1
        },
        "id": 4
    }
]

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

app.use(express.static(path.join(__dirname, 'public')));
app.post('/loginCL', function (req, res) {
    console.log(req.body);
    res.sendFile(path.join(__dirname, 'public', 'message.html'))
});

app.post('/data', function (req, res) {
    var options = {
        host: url,
        port: 80,
        path: '/ins',
        method: 'POST',
        herders: myheaders,
        auth: 'admin:eve',
    };
    const cReq = http.request(options);

    const speed = req.body.SPEED1;
    const bw1 = req.body.BandWidth1;
    const bw2 = req.body.BandWidth2;
    const bw3 = req.body.BandWidth3;

    delay1 = (1000 /
              (bw1 * 1000000 / 1488.0 -
               speed));
    delay2 =(1000 /
             (bw2 * 1000000 / 1488.0 -
              speed));
    delay3 = (1000 /
              (bw3 * 1000000 / 1488.0 -
              speed));


        if (delay1 < delay2 + delay3) {
            data = JSON.stringify(payload);
        }
        else {
            data = JSON.stringify(payload);
        }
        cReq.write(data);
        cReq.end();
    });

    res.send("数据发送成功");
    res.end();



app.listen(8080, () => {
    console.log('App listening at port 8080')
});
