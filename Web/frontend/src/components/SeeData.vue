<template>
  <div>
    <b-container>
        <div v-if="cond">
            <h2>Información de {{dato.Subject}}</h2>
            <b-table striped hover :items="dato"></b-table>
        </div>
        <div v-else>
            <h2>No se ha especificado ningún dato válido</h2>
            <p>Si está seguro de que el dato es válido, vuelva a intentarlo tras unos segundos.</p>
        </div>
    </b-container>
  </div>
</template>
 
<script>
const url = process.env.VUE_APP_API || "localhost:3000";
const API_URL = "http://" + url + '/api/dato';
export default {
  name: "SeeData",
  data: () => ({
    dato: null
  }),
  created: function () {
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
            this.dato = result.dato;
          }
        });
  },
  computed:{
    cond: function () {
      return this.dato !== null && Object.keys(this.dato).length >= 7;
    }
  }
};
</script>
 
<style>

</style>