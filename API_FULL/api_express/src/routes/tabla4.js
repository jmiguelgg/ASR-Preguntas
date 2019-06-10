const express = require('express');
const mongoose = require('mongoose');
const router = express.Router();
const User =  require('../model/user');

router.post('/newTemplate', (req, res, next) => {
    User
    .findById(req.body.userId)
    .exec()
    .then(result=>{
        result.templates[result.templates.length] = req.body.template
        result
        .save()
        .then(result1 =>{
            res.status(200).json(result1)
        })
        .catch(err =>{
            console.log(err)
          })
    })
    .catch(err =>{
        console.log(err)
      })
  })

  router.post('/templates', (req, res, next) =>{
      User
      .findById(req.body.userId)
      .exec()
      .then(result =>{
          res.status(200).json(result.templates)
      })
      .catch(err =>{
          console.log(err)
      })
  })

  module.exports = router;