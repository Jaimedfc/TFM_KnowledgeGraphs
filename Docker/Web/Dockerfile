FROM node
RUN apt-get update && apt-get install git -y && npm install -g nodemon
WORKDIR /
RUN git clone https://github.com/Jaimedfc/TFM_KnowledgeGraphs
WORKDIR /TFM_KnowledgeGraphs/Web/frontend
RUN npm install && npm run build
WORKDIR /TFM_KnowledgeGraphs/Web/
RUN npm install
EXPOSE 3000
CMD ["npm", "run", "devbabel"]