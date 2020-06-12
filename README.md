# TFM_KnowledgeGraphs
Sercicio para clasificar nivel de estrés en streaming generando un grafo al cual se puede aplicar algoritmos para estudiar "Knowledge Graphs".
## Instalación y Ejecución
Son necesarias las siguientes herramientas para correr el proyecto en local:
* Git.
* NodeJS y npm.
* Kafka y Zookeeper ([Versión 2.11-2.4.0](https://www.apache.org/dyn/closer.cgi?path=/kafka/2.4.1/kafka_2.11-2.4.1.tgz)).
* sbt.
* Spark ([Versión 2.4.5-hadoop2.7](https://archive.apache.org/dist/spark/spark-2.4.5/)).
* Docker
* Python versión 3 o superior.
* Dataset [WESAD](http://archive.ics.uci.edu/ml/datasets/WESAD+%28Wearable+Stress+and+Affect+Detection%29#)
* PySpark

En primer lugar, se clona el repositorio con:

``` git clone https://github.com/Jaimedfc/TFM_KnowledgeGraphs && cd /TFM_KnowledgeGraphs ```

Es necesario crear una carpeta Data en la raiz del proyecto, aquí se almacenarán los datos del proyecto.

``` mkdir Data ```

Se instalan las dependencias necesarias con pip y se ejecutan los siguientes scripts (adaptando las rutas del código) para preprocesar el dataset WESAD y reducirlo:

``` 
    cd Python
    pip3 install -r requirements.txt
    python3 dataClean.py
    python3 DFreduction.py
```

En /Data, se encontrarán varios ficheros, el más interesante es reducedDataset001.csv. Es el fichero que usará PySpark para generar el modelo al ejecutar:

``` python3 PySparkModel.py ```

Una vez calculado el modelo, se puede comenzar a correr el servicio.
Primero, se lanza Zookeeper con:

``` /kafka_2.11-2.4.0/bin/zookeeper-server-start.sh /kafka_2.11-2.4.0/config/zookeeper.properties ```

Se lanza Kafka y se crea el tópico (cada comando en una consola distinta):

``` 
    /kafka_2.11-2.4.0/bin/kafka-server-start.sh /kafka_2.11-2.4.0/config/server.properties
    /kafka_2.11-2.4.0/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic myTopic
```
Se usa Docker para lanzar un contenedor con Neo4j, mapeando los puertos necesarios:

``` docker run -p7474:7474 -p7687:7687 -v $HOME/neo4j/data:/pruebas --env=NEO4J_AUTH=neo4j/test --rm  neo4j:latest ```

Se compila el proyecto de Spark usando sbt, modificando el fichero Classification.scala:
En la línea 22 hay que poner la ruta absoluta al proyecto.
Comentar la línea 27 y descomentar la 28.

``` cd /TFM_KnowledgeGraphs/Scala/realtimeclassification && sbt package ```

Se lanza el archivo compilado usando spark-submit, indicando la dirección de neo4j y las credenciales de acceso:

``` ./spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.5,neo4j-contrib:neo4j-spark-connector:2.4.1-M1 --class Classification --conf spark.neo4j.bolt.url=bolt://localhost:7687 --conf spark.neo4j.bolt.user=neo4j --conf spark.neo4j.bolt.password=test /TFM_KnowledgeGraphs/Scala/realtimeclassification/target/scala-2.11/realtimeclassification_2.11-1.0.jar ```

Por último, se lanza el frontend, para ello, se instala las dependencias necesarias, se compila la parte de VueJS y se lanza Express:

```
    cd /TFM_KnowledgeGraphs/Web/frontend && npm install
    npm run build
    cd .. && npm install
    npm run devbabel
```

Ya se puede uno conectar a [http://localhost:3000](http://localhost:3000) y probar el servicio.

## Lanzar servicio usando docker-compose
Se necesita instalar la herramienta docker-compose y ejecutar lo siguiente estado en /TFM_KnowledgeGraphs:

``` docker-compose up ```

Para parar el servicio y limpiar entorno:

``` 
    Ctrl + C
    docker-compose down
```

## Lanzar el servicio usando Kubernetes
Se necesitan las siguientes herramientas:
* minikube
* kubectl

Una vez instaladas, se comienza lanzando el nodo donde se desplegará todo el servicio con:

``` minikube start --vm-driver=virtualbox --force --disk-size=15g --memory='4g' --cpus=4 ```

_Nota: Se pueden modificar los recursos usados por el nodo para adaptarlo a las capacidades de cada máquina._

Lanzado el nodo, se puede usar un dashboard que proporciona minikube para controlar el entorno:

``` minikube dashboard ```

Ahora, solo resta indicar los ficheros yaml que contienen todo el proyecto:

``` 
    cd k8s
    kubectl create -f kafka-service.yaml,neo-service.yaml,spark-service.yaml,web-service.yaml,zookeeper-service.yaml,kafka-deployment.yaml,neo-deployment.yaml,spark-deployment.yaml,web-deployment.yaml,zookeeper-deployment.yaml,web-ingress.yaml,highPriorityClass.yaml,mediumPriorityClass.yaml,lowPriorityClass.yaml
```

Tras unos minutos, en el dashboard, en el apartado que controla los Ingress, aparecerá el link de acceso al proyecto.

### Posibles problemas con Kubernetes
Es posible que si el dashboard no funciona o tarda demasiado el obtener un link a través del Ingress, se necesite habilitar los addons pernitentes en minikube:

```
    minikube addons enable dashboard
    minikube addons enable ingress
```

## Tras poblar el grafo...
Una vez se ha usado el servicio, se pueden hacer cálculos con el grafo que se ha generado en Neo4J. Todos el código necesario se puede encontrar en  /TFM_KnowledgeGraphs/Python.

_Nota: No se recomienda lanzar los scripts sin antes revisarlos. Hay que adaptarlos a cada situación._
