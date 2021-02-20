<template>
    <Layout>
        <template v-slot:body>
            <div class="container">
                <div class="columns">
                    <div class="column is-5">
                      <div class="box panel is-link">
                        <p class="panel-heading logo">
                          Trayectos
                        </p>
                        <table class="table is-fullwidth is-hoverable">
                          <thead>
                            <tr>
                              <th>Nombre</th>
                              <th>
                                Promedio de Pasajeros <br>
                                <span class="content is-small">
                                  Por Cada Ruta
                                </span>
                              </th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr v-for="trayecto in APIData" :key="trayecto.id" 
                            @click="setTrayecto(trayecto)" 
                            >
                              <th><a>{{ trayecto.nombre }}</a></th>
                              <td>{{ trayecto.promedio_pasajeros }}</td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </div>
                    <div class="column is-7">
                          <!-- Titulos -->
                          <h3 v-if="nombreActual == ''" class="title is-3 has-text-centered logo">
                              Seleccione Un Trayecto<br>
                              <span class="content is-small">Para Ver Rutas Disponibles</span>
                          </h3>
                          <h3 v-if="rutasActuales.length != 0" class="title is-3 has-text-centered logo">
                              Rutas Disponibles<br>
                              <span class="content is-small">{{ nombreActual }}</span>
                          </h3>
                          <h3 v-else-if="rutasActuales.length == 0 & nombreActual != ''" class="title is-3 has-text-centered logo">
                              Ninguna Ruta Disponible<br>
                              <span class="content is-small">{{ nombreActual }}</span>
                          </h3>
                          <!-- Titulos -->

                        <div class="field has-addons">
                          <div class="control is-expanded">
                            <input class="input is-link" v-model="porcentaje" type="text" 
                            placeholder="Filtra Rutas">
                          </div>
                          <div class="control">
                            <a @click="filtrarRutas()" class="button is-link">
                              Filtrar
                            </a>
                          </div>
                        </div><br>
                        
                        <!-- Rutas -->
                        <div class="columns is-flex is-flex-wrap-wrap">
                            <div v-for="ruta in rutasActuales" :key="ruta.id" class="column is-6">
                                <div class="box">
                                  <article class="media">
                                    <div class="media-left">
                                      <figure class="image is-64x64">
                                        <img src="https://bulma.io/images/placeholders/128x128.png" alt="Image">
                                      </figure>
                                    </div>
                                    <div class="media-content">
                                      <div class="content">
                                        <p>
                                          <strong>Identificador:</strong> <small>{{ ruta.id }}</small>
                                          <br>
                                          <strong>Chofer:</strong> <small>{{ ruta.info_bus.chofer_nombre }}</small>
                                          <br>
                                          <strong>Fecha:</strong> <small>{{ ruta.salida }}</small>
                                          <br>
                                          <strong>Capacidad:</strong> <small>{{ ruta.info_bus.capacidad }}</small>
                                          <br>
                                          <strong>Asientos Disponibles:</strong> <small>{{ asientosDisponibles(ruta) }}</small>
                                          <br>
                                        </p>
                                      </div>
                                      <nav class="level is-mobile">
                                        <div class="level-left">
                                          <a class="level-item" aria-label="reply">
                                            <span class="icon is-small" title="Reservar">
                                              <i class="fas fa-suitcase" aria-hidden="true"></i>
                                            </span>
                                            &nbsp;Reserva
                                          </a>
                                        </div>
                                      </nav>
                                    </div>
                                  </article>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </template>
    </Layout>
</template>

<script>
import Layout from "@/components/Layout";
import { getAPI } from "@/axios-api";

export default {
    name: 'Trayectos',
    data () {
        return {
            APIData: [],
            rutasActuales: [],
            nombreActual: '',
            trayectoActual: '',
            porcentaje: 0,
        }
    },
    created () {
        getAPI.get("/trayectos/")
          .then((response) => {
            this.APIData = response.data
          })
          .catch((error) => {
            console.log(error)
          })
    },
    methods: {
      setTrayecto(trayecto){
        this.trayectoActual = trayecto;
        this.nombreActual = trayecto.nombre;
        this.porcentaje = 0;
        this.getRutas();
      },
      filtrarRutas(){
        if (this.porcentaje == ''){
          this.porcentaje = 0;
        }else if(this.porcentaje >= 100){
           this.porcentaje = 100;
        }
        this.getRutas();
      },
      asientosDisponibles(ruta){
        return ruta.asientos.filter(
          asiento => asiento.estado == 1
        ).length;
      },
      getRutas(){
        let vm = this;
        let path = `/trayectos/${vm.trayectoActual.id}/rutas/${vm.porcentaje}/`
        getAPI.get(path)
          .then((response) => {
            vm.rutasActuales = response.data;
          })
          .catch((error) => {
            console.log(error)
          });
      }
    },
    components: {
        Layout
    }
};
</script>


<style scoped>
    .box {
        margin-top: 0rem;
    }
</style>