import express from 'express';
const router = express.Router();

// importar el modelo dato

// Agregar una nota
router.post('/dato', async(req, res) => {
  const body = req.body;  
  try {
    const dato = {
        'id': body.datoID,
        'ECG': body.ECG,
        'EMG': body.EMG,
        'EDA': body.EDA,
        'TEMP': body.TEMP,
        'RESP': body.RESP,
        'sujeto': body.sujeto
    }
    //TODO ENVIAR A KAFKA
    console.log(body);
    res.status(200).json(dato); 
  } catch (error) {
    return res.status(500).json({
      mensaje: 'Ocurrio un error',
      error
    })
  }
});

// Get con parámetros
router.get('/dato/:id', async(req, res) => {
    const _id = req.params.id;
    try {
      //const dato = COGERDENEO4J
      res.json({'msg': 'TODO OK'});
    } catch (error) {
      return res.status(400).json({
        mensaje: 'Ocurrio un error',
        error
      })
    }
  });

  // Get con todos los documentos
router.get('/dato', async(req, res) => {
    try {
      //const datos = PILLARTODOSLOSDATOS
      res.json({'msg': 'TODO OK'});
    } catch (error) {
      return res.status(400).json({
        mensaje: 'Ocurrio un error',
        error
      })
    }
  });

// Exportamos la configuración de express app
module.exports = router;