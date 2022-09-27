const express = require('express')
var cors = require('cors')
const db = require('./config/db')
//Creamos el servidor

const app = express()


//Conexion a la base de datos
db();

//Definimos rutas
app.use(cors())

app.get('/',(req, res) => {
    res.send("Hola mundo")
})

app.use(express.json())

app.use('/api/tasks', require('./routes/routes'))

app.listen(4000, () => {
    console.log('El servidor esta corriendo correctamente')
})
