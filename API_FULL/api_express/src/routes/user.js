const express = require('express');
const mongoose = require('mongoose');
const router = express.Router();
const User = require('../model/user');

router.get('/', function(req, res, next) {
  User.find()
    .exec()
    .then(doc =>{
      res.status(200).json(doc)
    })
    .catch(err => {
      console.log(err)
      res.status(500).json({error: err})
    })
});

router.post('/newuser', (req, res, next) => {
  const user = new User({
    _id: new mongoose.Types.ObjectId(),
    nombres: req.body.nombres,
    apellidos: req.body.apellidos,
    correo: req.body.correo,
    numero: req.body.numero,
    pass: req.body.pass
  })
  user
    .save()
    .then(result =>{
      res.status(200).json(result)
    })
    .catch(err =>{
      console.log(err)
    })
})

router.post('/login', (req, res, next) =>{
  User
  .find({
    correo: req.body.correo,
    pass: req.body.pass
  })
  .exec()
  .then(result => {
    res.status(200).json(result)
  })
  .catch(err =>{
    console.log(err)
  })
})

module.exports = router;
