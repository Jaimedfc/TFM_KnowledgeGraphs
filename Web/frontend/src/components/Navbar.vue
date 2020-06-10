<template>
    <b-navbar variant="dark" type="dark" fixed='top'>
      <b-navbar-brand href="/" id='logo-cont'>
        <img src="../assets/logo.png" class="d-inline-block align-top" alt="Vue logo" id='logo'/>
      </b-navbar-brand>
      <h1 class='text-light'>TFM de Jaime de Frutos Cerezo</h1>
      <b-navbar-nav class="ml-auto">
        <b-nav-form>
          <b-form-input size="sm" class="mr-sm-2" placeholder="Buscar"></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0" type="submit">Buscar</b-button>
        </b-nav-form>
        <b-nav-item to="/predict" align='left'><h3>Predecir nivel de Estrés</h3></b-nav-item>
      </b-navbar-nav>
    </b-navbar>
</template>

<script>

export default {
  name: 'Navbar'
}
</script>
