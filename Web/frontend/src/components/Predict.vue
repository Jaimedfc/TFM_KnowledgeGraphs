<template>
  <div>
    <form @submit.prevent="addDato" class="mb-3">
      <div v-if="error" class="alert alert-dismissible alert-warning">
        <button type="button" class="close" data-dismiss="alert">&times;</button>
        <h4 class="alert-heading">Error!</h4>
        <p class="mb-0">{{error}}</p>
      </div>
      <div class="form-group">
        <label for="datoID">DatoID</label>
        <input
          v-model="dato.datoID"
          type="text"
          class="form-control"
          id="datoID" required>
      </div>
      <div class="form-group">
        <label for="sujeto">Sujeto</label>
        <input
          v-model="dato.sujeto"
          type="text"
          class="form-control"
          id="sujeto"
          required>
      </div>
      <div class="form-group">
        <label for="ECG">Valor de ECG</label>
        <input
          v-model="dato.ECG"
          class="form-control"
          type="text"
          id="ECG" required>
      </div>
      <div class="form-group">
        <label for="EMG">Valor de EMG</label>
        <input
          v-model="dato.EMG"
          class="form-control"
          type="text"
          id="EMG" required>
      </div>
      <div class="form-group">
        <label for="EDA">Valor de EDA</label>
        <input
          v-model="dato.EDA"
          class="form-control"
          type="text"
          id="EDA" required>
      </div>
      <div class="form-group">
        <label for="TEMP">Valor de TEMP</label>
        <input
          v-model="dato.TEMP"
          class="form-control"
          type="text"
          id="TEMP" required>
      </div>
      <div class="form-group">
        <label for="RESP">Valor de RESP</label>
        <input
          v-model="dato.RESP"
          class="form-control"
          type="text"
          id="RESP" required>
      </div>
      <button type="submit" class="btn btn-primary">Predecir Estrés</button>
    </form>
  </div>
</template>
 
<script>
const url = process.env.URL_EXPRESS || "http://localhost:3000";
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
    }
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
            this.showMessageForm = false;
            console.log(result);
          }
        });
    }
  }
};
</script>
 
<style>

</style>