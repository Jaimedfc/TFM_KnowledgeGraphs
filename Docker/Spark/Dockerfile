FROM openjdk:8


RUN apt-get update && apt-get install curl tar wget git -y &&\
    rm -rf /var/lib/apt/lists/*

RUN echo "deb https://dl.bintray.com/sbt/debian /" | tee -a /etc/apt/sources.list.d/sbt.list &&\
    curl -sL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x2EE0EA64E40A89B84B2DF73499E82A75642AC823" | apt-key add &&\
    apt-get update && apt-get install sbt -y
ARG SPARK_VERSION=2.4.5
ENV SPARK_HOME=/usr/local/spark-$SPARK_VERSION-bin-hadoop2.7
WORKDIR /usr/local
RUN wget "https://apache.brunneis.com/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz"
RUN tar -zxvf spark-2.4.5-bin-hadoop2.7.tgz
ENV SPARK_CLASSPATH ${SPARK_HOME}/jars/*
ENV PATH $SBT_HOME/bin:$SPARK_HOME/bin:${SPARK_HOME}/jars/*:$PATH
WORKDIR /
RUN git clone https://github.com/Jaimedfc/TFM_KnowledgeGraphs && mkdir /TFM_KnowledgeGraphs/Data && mkdir /TFM_KnowledgeGraphs/pySparkRFModel
COPY ./Data/pySparkRFModel /TFM_KnowledgeGraphs/Data/pySparkRFModel
WORKDIR /TFM_KnowledgeGraphs/Scala/realtimeclassification
RUN sbt package
CMD echo "I'm done"
