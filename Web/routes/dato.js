import express from 'express';
var kafka = require('kafka-node');
const neo4j = require('neo4j-driver')
const router = express.Router();

// Agregar un dato
router.post('/dato', async(req, res) => {
  const body = req.body;  
  try {
    const dato = {
        'ECG': parseFloat(body.ECG),
        'EMG': parseFloat(body.EMG),
        'EDA': parseFloat(body.EDA),
        'TEMP': parseFloat(body.TEMP),
        'RESP': parseFloat(body.RESP),
        'sujeto': body.sujeto
    }
    // conf kafka
    let urlKafka = process.env.KAFKA_URI || 'localhost:9092';
    var client = new kafka.KafkaClient({kafkaHost: urlKafka});
    var producer = new kafka.Producer(client);
    
    
    var payloads = [{ topic: 'myTopic', messages: JSON.stringify(dato), partition: 0 }];
    producer.on('ready', function () {
      producer.send(payloads, function (err, data) {
          res.status(200).json({'msg': 'TODO SALIO A PEDIR DE MILHOUSE'}); 
      });
    });
  
    producer.on('error', function (err) {
      res.status(500).json({'error': err, 'msg': 'KAFKA LA LIO'});
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
    let urineo = process.env.NEO_URI || 'localhost';
    urineo = "neo4j://"+urineo
    const driver = neo4j.driver(urineo, neo4j.auth.basic('neo4j', 'test'),{
      connectionTimeout: 20 * 1000,
      maxConnectionLifetime: 3 * 60 * 60 * 1000, // 3 hours
      maxConnectionPoolSize: 50,
      connectionAcquisitionTimeout: 2 * 60 * 1000 // 120 seconds
    });
    const session = driver.session({ defaultAccessMode: neo4j.session.READ });
    session.run('MATCH (n :Subject {val: $value})--(x) RETURN x AS data',{ value: _id })
    .then(result =>{
      session.close();
      console.log(result);
      let myData = {}
      result.records.forEach(record => {
        myData[record.get('data').labels[0]] = record.get('data').properties.val
      })
      myData["Subject"] = _id;
      return res.status(200).json({'msg': 'TODO OK', 'dato': myData});
    })
    .catch (err =>{
      console.log("ERRRRROR",err);
      session.close();
      return res.status(400).json({
        mensaje: 'Ocurrio un error',
        err
      })
    })
    .then(() => driver.close());
  });
// Exportamos la configuración de express app
module.exports = router;