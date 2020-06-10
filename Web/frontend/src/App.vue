<template>
  <div id="app">
    <Navbar/>
    <b-row id='spacer'></b-row>
    <b-row id='spacer'></b-row>
    <router-view/>
    <b-row id='spacer'></b-row>
    <Footer/>
  </div>
</template>

<script>
import Navbar from "./components/Navbar"
import Footer from "./components/Footer"


export default {
  name: 'App',
  components: {
    Navbar,
    Footer
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
#logo {
  max-width: 50px;
}
#logo-cont {
  max-width: 50px;
  vertical-align: middle;
}
#spacer{
  height: 50px;
}
</style>
