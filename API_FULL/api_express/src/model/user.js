const mongoose = require('mongoose')

const template = mongoose.Schema({
    _id: mongoose.Schema.Types.ObjectId,
        id: Number,
        fecha: Date,
        data: {
            _id: mongoose.Schema.Types.ObjectId,
            hostname: String,
            idOSPF: String,
            user_name: String,
            pass: String,
            server_syslogs: String,
            networks: [{
                _id: mongoose.Schema.Types.ObjectId,
                id: Number,
                network: String,
                wildcard: String,
                area: Number
            }],
            interfaces: [{
                _id: mongoose.Schema.Types.ObjectId,
                id: Number,
                tipo: String,
                identificador: String,
                address: String,
                mascara: String
            }]
        }
})

const userSchema = mongoose.Schema({
    _id: mongoose.Schema.Types.ObjectId,
    nombres: String,
    apellidos: String,
    correo: String,
    numero: String,
    pass: String,
    templates:[template]
})

module.exports = mongoose.model('User',userSchema)