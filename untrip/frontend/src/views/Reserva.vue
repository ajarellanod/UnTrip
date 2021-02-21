<template>
  <Layout>
    <template v-slot:body>
      <div class="container">
        <div class="columns">
          <div class="column is-6 is-offset-3">
            <h3 class="title is-3 has-text-centered logo">
              {{ mensaje }}
            </h3>
            <div class="box">
              <form @submit.prevent v-if="!register">
                <div class="field">
                  <label class="label">
                    Nombre del Pasajero
                  </label>
                  <div class="control">
                    <input placeholder="Ingrese su Nombre" type="text" class="input" v-model="form.nombre"/>
                  </div>
                </div>
                <div class="field">
                  <label class="label">
                    Numero de Identificación
                  </label>
                  <div class="control">
                    <input placeholder="Ingrese su Identificación" type="text" class="input" v-model.number="form.identificacion"/>
                  </div>
                </div>
                <button @click="getOptions()" class="button is-link">
                  Siguiente
                </button>
              </form>
              <form @submit.prevent v-if="register & !objAsiento.codigo">
                <div class="field">
                  <label class="label">
                    Seleccione Numero de Asiento
                  </label>
                  <div class="control">
                    <div class="select is-fullwidth">
                      <select v-model="asiento">
                        <option v-for="option in selectOptions" :key="option.id" :value="option.identificador">
                          {{option.identificador}}
                        </option>
                      </select>
                    </div>
                  </div>
                </div>
                <button @click="reservar()" class="button is-link">
                  Reservar
                </button>
              </form>
              <div id="last-info" v-if="objAsiento.codigo">
                <table class="table is-fullwidth is-bordered">
                  <thead>
                    <tr>
                      <th colspan="2">
                        <p class="title is-4">Detalles de la Reservación</p>
                      </th>
                    </tr>
                    <tr>
                      <th>
                        <p class="title is-5">Codigo</p>
                      </th>
                      <th>
                        <p class="title is-5">{{objAsiento.codigo}}</p>
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <p class="subtitle is-5">Trayecto</p>
                      </td>
                      <td>
                        <p class="subtitle is-5">{{trayecto.nombre}}</p>
                      </td>
                    </tr>
                    <tr>
                      <td>
                        <p class="subtitle is-5">Pasajero</p>
                      </td>
                      <td>
                        <p class="subtitle is-5">{{form.nombre}}</p>
                      </td>
                    </tr>
                    <tr>
                      <td>
                        <p class="subtitle is-5">Fecha</p>
                      </td>
                      <td>
                        <p class="subtitle is-5">{{ruta.salida}}</p>
                      </td>
                    </tr>
                    <tr>
                      <td>
                        <p class="subtitle is-5">Chofer</p>
                      </td>
                      <td>
                        <p class="subtitle is-5">{{ruta.info_bus.chofer_nombre}}</p>
                      </td>
                    </tr>
                    <tr>
                      <td>
                        <p class="subtitle is-5">Numero de Asiento</p>
                      </td>
                      <td>
                        <p class="subtitle is-5">{{objAsiento.identificador}}</p>
                      </td>
                    </tr>
                  </tbody>
                </table>
                <router-link class="button is-link" to="/trayectos">
                  Confirmar
                </router-link>
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
  name: 'Reserva',
  props: ['rutaId'],
  data () {
    return {
      form: {
        nombre: '',
        identificacion: ''
      },
      register: false,
      objAsiento: '',
      asiento: '',
      ruta: '',
      trayecto: '',
      selectOptions: [],
      mensaje: 'Llena el Formulario con tu Información!'
    }
  },
  components: {
    Layout
  },
  created(){
    let vm = this;
    getAPI.get(`/rutas/${vm.rutaId}/`)
      .then((response) => {
        vm.ruta = response.data;
        vm.trayecto = vm.ruta.info_trayecto;
      })
      .catch((error) => {
        console.log(error);
      });
  },
  methods:{
    reservar(){
      let vm = this;
      getAPI.post(`/rutas/${this.rutaId}/reservar/${this.asiento}/`, this.form)
        .then((response) => {
          vm.objAsiento = response.data;
          vm.mensaje = "Felicidades ya has reservado tu asiento!"
        })
        .catch(() => {
          vm.mensaje = "Ha fallado tu registro, intentalo nuevamente."
        });
    },
    getOptions(){
      let vm = this;
      if(vm.form.nombre == ''){
        vm.form.nombre = 'Ingresa tu nombre!'
      }else if(vm.form.identificacion == ''){
        vm.form.identificacion = 'Ingresa tu numero de identificación!'
      }else{
        vm.register = true
        getAPI.get(`/rutas/${vm.rutaId}/asientos/`)
          .then((response) => {
            vm.selectOptions = response.data;
            vm.mensaje = "Ahora solo selecciona tu Asiento y habras terminado!"
          })
          .catch((error) => {
            console.log(error);
          });
      }

    },
  }
};
</script>
