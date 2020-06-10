<template>
    <div id="mainFooter" className="main-footer">
            <b-container fluid>
                <b-row>
                    <b-col class="brief text-center" md="4">
                        <div class="header"><img id="imgFooter" src="../assets/logo.png" alt="Vue logo" width="200"/></div>
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
</template>

<script>

export default {
  name: 'Footer'
}
</script>