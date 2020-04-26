FROM openjdk:8

ENV TAG_VERSION 0.1

RUN apt-get update && apt-get install curl tar wget -y &&\
    rm -rf /var/lib/apt/lists/*

ARG SBT_VERSION=1.1.5
ARG SBT_HOME=/usr/local/sbt
RUN curl -sL "https://github.com/sbt/sbt/releases/download/v$SBT_VERSION/sbt-$SBT_VERSION.tgz" | tar -xz -C /usr/local

ARG SPARK_VERSION=2.4.4
ENV SPARK_HOME=/usr/local/spark-$SPARK_VERSION-bin-hadoop2.7
WORKDIR /usr/local
RUN wget "http://apache.rediris.es/spark/spark-2.4.4/spark-2.4.4-bin-hadoop2.7.tgz"
RUN tar -zxvf spark-2.4.4-bin-hadoop2.7.tgz
ENV SPARK_CLASSPATH ${SPARK_HOME}/jars/*
ENV PATH $SBT_HOME/bin:$SPARK_HOME/bin:${SPARK_HOME}/jars/*:$PATH
RUN mkdir /practica
COPY practica_big_data_2019/ /practica/


EXPOSE 7077

CMD spark-submit --packages org.mongodb.spark:mongo-spark-connector_2.11:2.3.2,org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.0 --class es.upm.dit.ging.predictor.MakePrediction /practica/flight_prediction/target/scala-2.11/flight_prediction_2.11-0.1.jar
