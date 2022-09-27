const mongoose = require('mongoose')

require('dotenv').config({path:'.env'})

const DB = async () => {
    try {
        await mongoose.connect(process.env.MONGO_DB , {
            useNewUrlParser: true,
            useUnifiedTopology: true,
        })
        console.log("DB concetada")
    } catch (error) {
        console.error(error)
    }
}
module.exports = DB