//var a=35
//console.log(typeof(a))

//PROGRAM 2
// const http=require('http')
// http.createServer((req,res)=>{
//     if(req.url=='/'){
//         res.writeHead(200);
//         res.write('Hello world');
//         res.end();
//     }
//     else if(req.url=='/about'){
//         res.writeHead(200);
//         res.write('about page');
//         res.end();
//     }
//     else{
//         res.writeHead(200);
//         res.write('page not found');
//         res.end();
//     }
// })
// .listen(3000,"127.0.0.1",()=>{
// console.log("server run on http://127.0.0.1:3000")
// })

//PROGRAM 1
// const http=require('http')
// const host="127.0.0.1"
// const port=3000
// const server=http.createServer((req,res)=>{
//     res.writeHead(200);
//     res.write('Hello world!');
//     res.end();
// })
// server.listen(port,host,()=>{
// console.log("server run on http://127.0.0.1:3000")
// })

//PROGRAM 3 USES locla.js FILE
// const local=require('./local')
// let z=local.add(10,20)
// let z1=local.mul(10,20)
// let z2=local.sub(10,20)
// console.log(z)
// console.log(z1)
// console.log(z2)

//PROGRAM 4 
// let url=require('url')
// let string=url.parse('https://www.example.com?user=tej',true)
// console.log(string.hostname)
// console.log(string.protocol)
// console.log(string.pathname)
// console.log(string.query)


//PROGRAM 5 SIMILAR TO PROGRAM 4
// const {hostname}=require('os')
// let url=require('url')
// const obj={
//     protocol:'https',
//     hostname:'www.google.com',
//     pathname:'/user',
//     query:{name : "jimin"}
// }
// let x = url.format(obj)
// console.log(x)


//PROGRAM  6
// const {hostname}=require('os')
// let url=require('url')
// const baseUrl='https://www.google.com'
// const pathUrl='/user'
// let x=url.resolve(baseUrl,pathUrl)
// console.log(x)


// PROGRAM 7
// const {hostname}=require('os')
// let url=require('url')
// const queryString=require('querystring')
// const str="hello kits"
// const x=queryString.escape(str)
// console.log(x)
// const y=queryString.unescape(str)
// console.log(y)

//PROGRAM 8
// const {hostname}=require('os')
// let url=require('url')
// const queryString=require('querystring')
// const obj={
//     name:"teja",
//     age:23,
//     address:"hyd"
// }
// const x= queryString.stringify(obj)
// console.log(x)

//PROGRAM 9
const {hostname}=require('os')
let url=require('url')
const queryString=require('querystring')
const str='name=Raj&age=23&address=hyd'
const y=queryString.parse(str)
console.log(y)