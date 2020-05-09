<template>
  <div>
    <b-container fluid class='text-left'>
      <b-form @submit.prevent="searchDato" class='left-align'>
        <b-form-group label='Sujeto a buscar:' label-for="dataToSearch" description="Se recomienda esperar unos segundos tras rellenar el formulario inferior para buscar datos.">
        <b-form-input
          v-model="dataToSearch"
          type="text"
          id="dataToSearch"
          required></b-form-input>
      </b-form-group>
      <b-row fluid align-h="around">
        <b-button type="submit" variant="primary">Buscar datos</b-button>
      </b-row>
      </b-form>
    </b-container>
    <b-container fluid class='text-left'>
    <h2>Por favor, rellene el siguiente formulario:</h2>
    <b-form @submit.prevent="addDato" @reset.prevent="onReset" class='left-align'>
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
    <b-row id='spacer'></b-row>
    <div v-if="sent" class="alert alert-dismissible alert-warning">
      <h3>¡Dato Enviado!</h3>
    </div>
    </b-container>
  </div>
</template>
 
<script>
const url = process.env.VUE_APP_API || "localhost:3000";
const API_URL = "http://" + url + '/api/dato';
 
export default {
  name: "Predict",
  data: () => ({
    error: "",
    dato: {
      sujeto: "",
      ECG: "",
      EMG: "",
      EDA: "",
      TEMP: "",
      RESP: ""
    },
    sent: false,
    dataToSearch: ""
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
            this.sent = true;
          }
        });
    },
    onReset() {
        // Reset our form values
        this.dato.sujeto = '';
        this.dato.ECG = '';
        this.dato.EMG = '';
        this.dato.EDA = '';
        this.dato.TEMP = '';
        this.dato.RESP = '';
        this.sent = false;
      },
    searchDato(){
      this.$router.push('/data/'+this.dataToSearch);
    }
  }
};
</script>
 
<style>
#spacer{
  height: 50px;
}
</style>