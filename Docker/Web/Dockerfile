FROM node
RUN apt-get update && apt-get install git -y && npm install -g nodemon
WORKDIR /
RUN git clone https://github.com/Jaimedfc/TFM_KnowledgeGraphs
WORKDIR /TFM_KnowledgeGraphs/Web/
RUN npm install && npm install --prefix ./frontend
EXPOSE 3000
CMD npm run build --prefix ./frontend && npm run devbabel