<template>
  <div id="app">
    <b-navbar variant="dark" type="dark" fixed='top'>
      <b-navbar-brand href="/" id='logo-cont'>
        <img src="./assets/logo.png" class="d-inline-block align-top" alt="Vue logo" id='logo'/>
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
    <b-row id='spacer'></b-row>
    <b-row id='spacer'></b-row>
    <router-view/>
    <b-row id='spacer'></b-row>
    <div id="mainFooter" className="main-footer">
            <b-container fluid>
                <b-row>
                    <b-col class="brief text-center" md="4">
                        <div class="header"><img id="imgFooter" src="./assets/logo.png" alt="Vue logo" width="200"/></div>
                            <p>Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.</p>
                    </b-col>
                    <b-col class="contact" md="4">
                        <div class="header">
                            <h4>Contacto</h4>
                        </div>
                        <ul class="contact list-unstyled">
                            <li><span class="icon-map text-primary">Dirección: </span>Calle Esta, Las Rozas de Madrid 28232, Madrid(España)  </li>
                            <li><b-link href="mailto:jaime.frutos.cerezo@alumnos.upm.es"><span class="icon-phone text-primary">e-mail: </span>jaime.frutos.cerezo@alumnos.upm.es</b-link></li>
                            <li><span class="icon-mail text-primary">Tlfn: </span>123 45 67 89</li>
                            <li><span class="icon-printer text-primary">Fax: </span>333-999-666</li>
                        </ul>
                    </b-col>
                    <b-col class="newsletter" md="4">
                        <div class="header">
                            <h4>Noticias</h4>
                        </div>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit sed do eiusmo.</p>
                    </b-col>
                </b-row>
                <ul class="social list-inline">
                    <li class="list-inline-item"><b-link to="#"><i class="fa fa-facebook"></i></b-link></li>
                    <li class="list-inline-item"><b-link to="#"><i class="fa fa-twitter"></i></b-link></li>
                    <li class="list-inline-item"><b-link to="#"><i class="fa fa-instagram"></i></b-link></li>
                    <li class="list-inline-item"><b-link to="#"><i class="fa fa-google-plus"></i></b-link></li>
                    <li class="list-inline-item"><b-link to="#"><i class="fa fa-pinterest"></i></b-link></li>
                    <li class="list-inline-item"><b-link to="#"><i class="fa fa-skype"></i></b-link></li>
                </ul>
            </b-container>
            <div class="copyrights">
                <b-container>
                    <b-row>
                        <b-col md="5">
                            <ul class="list-inline mb-0">
                                <li class="list-inline-item"><b-link to="#">Policy Privacy</b-link></li>
                                <li class="list-inline-item"><b-link to="#">Terms of Use</b-link></li>
                                <li class="list-inline-item"><b-link to="#">Contact</b-link></li>
                            </ul>
                        </b-col>
                        <b-col md="7">
                            <p class="mb-0">© 2020 Company: Las Rozas.</p>
                        </b-col>
                    </b-row>
                </b-container>
            </div>
        </div>
  </div>
</template>

<script>



export default {
  name: 'App'
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
