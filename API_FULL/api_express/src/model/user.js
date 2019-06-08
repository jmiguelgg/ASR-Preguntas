const mongoose = require('mongoose')

const userSchema = mongoose.Schema({
    _id: mongoose.Schema.Types.ObjectId,
    nombres: String,
    apellidos: String,
    correo: String,
    numero: String,
    pass: String
})

module.exports = mongoose.model('User',userSchema)