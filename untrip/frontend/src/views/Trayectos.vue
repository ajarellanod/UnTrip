<template>
    <Layout>
        <template v-slot:body>
            <div class="container">
                <div class="columns">
                    <div class="column is-5">
                        <article class="panel is-link">
                          <p class="panel-heading logo">
                            Trayectos
                          </p>
                          <p class="panel-tabs">
                            <a v-for="option in filterOptions" :key="option"
                            :class="{ 'is-active': actualOption === option }"
                            @click="getFilterOptions(option)"
                            >
                                {{option}}
                            </a>
                          </p>
                          <div class="panel-block">
                            <p class="control has-icons-left">
                              <input class="input is-link" type="text" placeholder="Search">
                              <span class="icon is-left">
                                <i class="fas fa-search" aria-hidden="true"></i>
                              </span>
                            </p>
                          </div>
                          <a v-for="trayecto in APIData" :key="trayecto.id" @click="getRutas(trayecto)" class="panel-block is-active">
                            <span class="panel-icon">
                              <i class="fas fa-book" aria-hidden="true"></i>
                            </span>
                            {{ trayecto.nombre }}
                          </a>
                          <div class="panel-block">
                            <nav class="pagination" role="navigation" aria-label="pagination">
                                <a class="pagination-previous button is-link is-outlined">
                                    <i class="fas fa-caret-left" aria-hidden="true"></i>
                                </a>
                                <a class="pagination-next button is-link is-outlined">
                                    <i class="fas fa-caret-right" aria-hidden="true"></i>
                                </a>
                                <ul class="pagination-list">
                                </ul>
                            </nav>
                          </div>
                        </article>
                    </div>
                    <div class="column is-7">
                        <h3 v-if="trayectoActual == ''" class="title is-3 has-text-centered logo">
                            Seleccione Un Trayecto
                            <br>
                            <span class="content is-small">Para Ver Rutas Disponibles</span>
                        </h3>
                        <h3 v-if="rutasActuales.length != 0" class="title is-3 has-text-centered logo">
                            Rutas Disponibles
                            <br>
                            <span class="content is-small">{{ trayectoActual }}</span>
                        </h3>
                        <h3 v-else-if="rutasActuales.length == 0 & trayectoActual != ''" class="title is-3 has-text-centered logo">
                            Trayecto Sin Rutas Disponibles
                            <br>
                            <span class="content is-small">{{ trayectoActual }}</span>
                        </h3>
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
                                          </a>
                                          <a class="level-item" aria-label="retweet">
                                            <span class="icon is-small" title="Obten Información">
                                              <i class="fas fa-info" aria-hidden="true"></i>
                                            </span>
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
            trayectoActual: '',
            filterOptions: ['Todos', 'Largos', 'Cortos'],
            actualOption: 'Todos'
        }
    },
    created () {
        getAPI.get("/trayectos/")
          .then(response => {
            this.APIData = response.data
          })
          .catch(err => {
            console.log(err)
          })
    },
    methods: {
        getRutas(trayecto){
            let vm = this;
            vm.trayectoActual = trayecto.nombre;
            vm.rutasActuales = [];
            trayecto.rutas.forEach(function (path){
                getAPI.get(path)
                  .then(response => {
                    vm.rutasActuales.push(response.data);
                    console.log(response.data);
                  })
                  .catch(err => {
                    console.log(err)
                  })
            });
        },
        asientosDisponibles(ruta){
            let asientos = ruta.asientos.filter(asiento => asiento.estado == 1);
            return asientos.length
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