const Task = require("../models/Task")

exports.crearTask = async (req, res) => {
    console.log(req.body)
    try {
        let task
        //Creamos nuestra tarea
        task = new Task(req.body)
        await task.save()
        res.send(task)
        
    } catch (error) {
        console.log(error)
        res.status(500).send('Ocurrio un error')
    }
}

exports.obtenerTasks = async (req , res) => {
    try {
        const tasks = await Task.find()
        res.json(tasks)
    } catch (error) {
        console.log(error)
        res.status(500).send('Ocurrio un error')
    }
}

exports.actualizarTask = async (req, res) => {
    try {
        const { name, description, status, comment } = req.body
        let task = await Task.findById(req.params.id)
        if (!task) {
            res.status(404).json({msg: 'No existe la tarea'})
        }
        task.name = name
        task.description = description
        task.status = status
        task.comment = comment

        task = await Task.findOneAndUpdate({_id: req.params.id}, task, {new: true})
        res.json(task)

    } catch (error) {
        console.log(error)
        res.status(500).send('Ocurrio un error al actulizar')
    }
}

exports.obtenerTask = async (req, res) => {
    try {
        let task = await Task.findById(req.params.id)
        if (!task) {
            res.status(404).json({msg: 'No existe la tarea'})
        }
        res.json(task)
    } catch (error) {
        console.log(error)
        res.status(500).send('Ocurrio un error al obtener el dato')
    }
}

exports.eliminarTask = async (req, res) => {
    try {
        let task = await Task.findById(req.params.id)
        if (!task) {
            res.status(404).json({msg: 'No existe la tarea'})
        }
        await Task.findOneAndRemove({_id: req.params.id})
        res.json({msg: 'Tarea eliminada con exito'})
    } catch (error) {
        console.log(error)
        res.status(500).send('Ocurrio un error al eliminar el dato')
    }
}