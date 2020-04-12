import express from 'express';
var kafka = require('kafka-node');
const router = express.Router();

//payload scheme:
/*{
   topic: 'topicName',
   messages: ['message body'], // multi messages should be a array, single message can be just a string or a KeyedMessage instance
   key: 'theKey', // string or buffer, only needed when using keyed partitioner
   partition: 0, // default 0
   attributes: 2, // default: 0
   timestamp: Date.now() // <-- defaults to Date.now() (only available with kafka v0.10+)
}*/

// Agregar una nota
router.post('/dato', async(req, res) => {
  const body = req.body;  
  try {
    const dato = {
        'datoID': body.datoID,
        'ECG': parseFloat(body.ECG),
        'EMG': parseFloat(body.EMG),
        'EDA': parseFloat(body.EDA),
        'TEMP': parseFloat(body.TEMP),
        'RESP': parseFloat(body.RESP),
        'sujeto': body.sujeto
    }
    console.log(dato);
    // conf kafka
    let urlKafka = process.env.KAFKA_URI || 'localhost';
    urlKafka = urlKafka+':9092';
    console.log(urlKafka);
    //console.log(process.env);
    var client = new kafka.KafkaClient({kafkaHost: urlKafka});
    var producer = new kafka.Producer(client);
    
    
    var payloads = [{ topic: 'myTopic', messages: JSON.stringify(dato), partition: 0 }];
    producer.on('ready', function () {
      producer.send(payloads, function (err, data) {
          console.log('TODO SALIO A PEDIR DE MILHOUSE');
          console.log(data);
          res.status(200).json({'msg': 'TODO SALIO A PEDIR DE MILHOUSE'}); 
      });
    });
  
    producer.on('error', function (err) {
      res.status(500).json({'error': 'KAFKA LA LIO'});
    })
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
      res.status(200).json({'msg': 'TODO OK', 'dato': _id});
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