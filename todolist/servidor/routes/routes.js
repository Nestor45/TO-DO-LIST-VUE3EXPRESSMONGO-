//Para acceder al ruteo vamos a usar EXPRESS
const express = require('express')
const router = express.Router()

const taskController = require('../controller/taskController')

// api/datos
router.post('/', taskController.crearTask)
router.get('/', taskController.obtenerTasks)
router.put('/:id', taskController.actualizarTask)
router.get('/:id', taskController.obtenerTask)
router.delete('/:id', taskController.eliminarTask)
module.exports = router