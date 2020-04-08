<template>
  <div>
    <b-container fluid class='text-left'>
    <h2>Por favor, rellene el siguiente formulario:</h2>
    <b-form @submit.prevent="addDato" @reset.prevent="onReset" class='left-align'>
      <b-form-group label='ID de los datos:' label-for="datoID">
        <b-form-input
          v-model="dato.datoID"
          type="text"
          id="datoID"
          required></b-form-input>
      </b-form-group>
      <b-form-group label='Sujeto:' label-for="sujeto" description="Introducir un valor anonimizado. Ej. 'S15'">
        <b-form-input
          v-model="dato.sujeto"
          type="text"
          id="sujeto"
          required></b-form-input>
      </b-form-group>
      <b-form-group label='Valor de ECG:' label-for="ECG">
        <b-form-input
          v-model="dato.ECG"
          type="text"
          id="ECG" required></b-form-input>
      </b-form-group>
      <b-form-group label='Valor de EMG:' label-for="EMG">
        <b-form-input
          v-model="dato.EMG"
          type="text"
          id="EMG" required></b-form-input>
      </b-form-group>
      <b-form-group label='Valor de EDA:' label-for="EDA">
        <b-form-input
          v-model="dato.EDA"
          type="text"
          id="EDA" required></b-form-input>
      </b-form-group>
      <b-form-group label='Valor de TEMP:' label-for="TEMP">
        <b-form-input
          v-model="dato.TEMP"
          type="text"
          id="TEMP" required></b-form-input>
      </b-form-group>
      <b-form-group label='Valor de RESP:' label-for="RESP">
        <b-form-input
          v-model="dato.RESP"
          type="text"
          id="RESP" required></b-form-input>
      </b-form-group>
      <b-row fluid align-h="around">
        <b-button type="submit" variant="primary">Enviar datos</b-button>
        <b-button type="reset" variant="danger">Limpiar formulario</b-button>
      </b-row>
    </b-form>
    <div v-if="error" class="alert alert-dismissible alert-warning">
        <button type="button" class="close" data-dismiss="alert">&times;</button>
        <h4 class="alert-heading">Error!</h4>
        <p class="mb-0">{{error}}</p>
    </div>
    <b-row v-if="showLink">
        <h4><b-link v-bind:to="resultURL">Ver resultado del dato {{dato.datoID}}</b-link></h4>
      </b-row>
    </b-container>
  </div>
</template>
 
<script>
const url = process.env.VUE_APP_API || "http://localhost:3000";
const API_URL = url + '/api/dato';
 
export default {
  name: "Predict",
  data: () => ({
    error: "",
    dato: {
      datoID: "",
      sujeto: "",
      ECG: "",
      EMG: "",
      EDA: "",
      TEMP: "",
      RESP: ""
    },
    showLink: false
  }),
  
  methods: {
    addDato() {
      console.log(this.dato);
      fetch(API_URL, {
        method: "POST",
        body: JSON.stringify(this.dato),
        headers: {
          "content-type": "application/json"
        }
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
            this.error = "";
            console.log(result);
            this.showLink = true;
          }
        });
    },
    onReset() {
        // Reset our form values
        this.dato.sujeto = '';
        this.dato.datoID = '';
        this.dato.ECG = '';
        this.dato.EMG = '';
        this.dato.EDA = '';
        this.dato.TEMP = '';
        this.dato.RESP = '';
        this.showLink = false;
      }
  },
  computed:{
    resultURL: function () {
      return "/data/"+this.dato.datoID;
    }
  }
};
</script>
 
<style>

</style>