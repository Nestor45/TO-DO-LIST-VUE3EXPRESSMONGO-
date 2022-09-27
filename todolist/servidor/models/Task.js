const mongoose = require('mongoose')

const TaskSchema = mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    description: {
        type: String,
        required: true
    },
    status: {
        type: String,
        required: true
    },
    comment: {
        type: String,
        required: true
    },
    dateCreation: {
        type: Date,
        default: Date.now()
    },
})

module.exports = mongoose.model('Task', TaskSchema)