<template>
  <div>
    <b-container>
        <div v-if="cond">
            <h2>Información de {{dato.Sujeto}}</h2>
            <b-table striped hover :items="arr"></b-table>
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
    dato: {
      Sujeto: "",
      datoECG: "",
      datoEMG: "",
      datoEDA: "",
      datoTEMP: "",
      datoRESP: "",
      Estado: ""
    }
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
            this.dato.Sujeto = String(result.dato.Subject);
            this.dato.datoECG = String(result.dato.ECGData);
            this.dato.datoEMG = String(result.dato.EMGData);
            this.dato.datoEDA = String(result.dato.EDAData);
            this.dato.datoTEMP = String(result.dato.TEMPData);
            this.dato.datoRESP = String(result.dato.RESPData);
            this.dato.Estado = String(result.dato.Status);
          }
        });
  },
  computed:{
    cond: function () {
      return this.dato.datoECG !==undefined && this.dato.datoEMG!==undefined
       && this.dato.datoEDA!==undefined && this.dato.datoTEMP!==undefined && this.dato.datoRESP!==undefined && this.dato.Estado!==undefined;
    },
    arr: function () {
      return [this.dato];
    }
  }
};
</script>
 
<style>

</style>