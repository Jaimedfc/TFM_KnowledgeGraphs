<template>
    <b-container class="text-center home">
        <b-row class="text-center">
            <b-col><h1>¡Bienvenidos a la Tercera Era del Machine Learning!</h1></b-col>
        </b-row>
        <b-row class="text-center">
            <b-col><img alt="Vue logo" src="../assets/KG.png"/></b-col>
        </b-row>
        <b-row class="text-center">
            <b-col><p>Fuente:  <span><b-link href="https://medium.com/@dmccreary/knowledge-graphs-the-third-era-of-computing-a8106f343450">Artículo en Medium</b-link></span></p></b-col>
        </b-row>
        <div class="spacer"></div>
        <b-row class="text-center">
            <b-col><h3>GitHub del proyecto:  <span><b-link href="https://github.com/Jaimedfc/TFM_KnowledgeGraphs">github.com/Jaimedfc/TFM</b-link></span></h3></b-col>
        </b-row>
        <div class="spacer"></div>
    </b-container>
</template>

<script>



export default {
  name: 'Home'
}
</script>

<style>
.home {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.spacer{
    height: 150px;
}
</style>