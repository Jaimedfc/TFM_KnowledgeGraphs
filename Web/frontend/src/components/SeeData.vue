<template>
  <div>
    <b-container>
        <div v-if="dato !== null">
            <h2>Información de {{dato.datoID}}</h2>
            <ul id="v-for-object">
                <li v-for="(value, name) in dato" v-bind:key="name">
                    {{ name }}: {{ value }}
                </li>
            </ul>
        </div>
        <div v-else>
            <h2>No se ha especificado ningún dato válido</h2>
        </div>
    </b-container>
  </div>
</template>
 
<script>
const url = process.env.URL_EXPRESS || "http://localhost:3000";
const API_URL = url + '/api/dato';
export default {
  name: "SeeData",
  data: () => ({
    dato: null
  }),
  created: function () {
    console.log('DATO: ' + this.$route.params.data)
    fetch(API_URL+"/"+this.$route.params.data, {
        method: "GET"
      })
        .then(response => response.json())
        .then(result => {
          if (result.details) {
            // there was an error...
            const error = result.details
              .map(detail => detail.message)
              .join(". ");
            this.error = error;
          } else {
            console.log(result);
            this.dato = result.dato;
          }
        });
  }
};
</script>
 
<style>

</style>