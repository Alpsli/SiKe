const express = require('express')
const app = express()
const http = require('http')
var options = {
  host: 'https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token',
  method: 'POST',
  herders: { 'content-type': 'application/json-rpc' },
  auth: 'devnetuser:Cisco123!',
};
const cReq = http.request(options);
console.log(cReq)

