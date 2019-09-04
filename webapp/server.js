var express = require('express');
var app = express();

//这里是解决跨域访问的问题
app.all('*', function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "X-Requested-With");
  res.header("Access-Control-Allow-Methods","PUT,POST,GET,DELETE,OPTIONS");
  res.header("X-Powered-By",' 3.2.1');
  res.header("Content-Type", "application/json;charset=utf-8");
  next();
})

//监听8000端口
var server = app.listen(8000, 'localhost', function () {
  console.log('服务器已经启动，地址是http://localhost:8000')
})

//
app.get('/', function (req, res) {
  res.send('这里是首页')
})

app.get('/data', function (req, res) {
  let data1 = JSON.stringify(data);
  res.send(data1)  //返回json数据,这两句相当于res.json(data)
})

app.get('/login', function (req, res) {
  var comm = req.query;
  var data = false;
  for(let user in users){
    if(users[user].name === comm.name && users[user].password === comm.password){
      data = true
    }
  }
  res.json({
    data: data,
    code: 200,
    msg: 'ok'
  })  //返回json数据
})
// 模拟的数据

var users = [
  {
    name:'lihao',
    password:'lihao0920'
  },
  {
    name:'guohao',
    password:'guohao0001'
  },
]

var data = {
  data: [
    {
      name:"李浩",
      age:'23',
      from:'重庆',
      teacher:'崔琪楣',
    },
    {
      name:"郭浩",
      age:'24',
      from:'河北',
      teacher:'陶晓峰',
    },
  ],
  code: 200,
  msg: 'ok'
}
