const express = require('express');
const path = require('path');
const cookieParser = require('cookie-parser');
const logger = require('morgan');
const mongoose = require('mongoose');

mongoose.connect('mongodb://redesfull:xyz123@localhost:27017/redes3', { poolSize: 5 }).then(()=>{
    console.log('Se conecto a la base de datos')
}).catch((()=>{
    console.log('No se pudo conectar a la base de datos')
}))

const user = require('./src/routes/user');
const tabla4 = require('./src/routes/tabla4');

const app = express();

app.use((req, res, next) =>{
    res.header("Access-Control-Allow-Origin", "*")
    res.header(
        "Access-Control-Allow-Headers",
        "Origin, X-Requested-With, Content-Type, Accept, Authorization"
    );
    if (req.method === 'OPTIONS') {
        res.header("Access-Control-Allow-Methods", "PUT, POST, PATCH, DELETE, GET")
        return res.status(200).json({})
    }
    next()
})

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/user', user);
app.use('/tabla4', tabla4);

module.exports = app;
