<template>
    <AdminLayout>
        <template v-slot:body>
            <div class="container">
                <div class="columns">
                    <div class="column is-6 is-offset-3">
                        <div class="box">
                            <div class="tabs is-centered is-boxed">
                              <ul>
                                <li v-for="option in formsOptions" :key="option"
                                :class="{ 'is-active': actualOption === option }"
                                @click="setOption(option)"
                                >
                                    <a>{{option}}</a>
                                </li>
                              </ul>
                            </div>
                            <div class="forms">
                                <form @submit.prevent v-show="actualOption == form.name" v-for="form in forms" :key="form.name">
                                    <!-- Principal Field -->
                                   <div class="field">
                                        <label class="label">
                                            {{form.principal.label}}
                                        </label>                                 
                                          <div class="select is-fullwidth">
                                            <select v-model="form.principal.data" @change="getObject(form)" :name="form.principal.name">
                                                <option 
                                                  v-for="option in getSelectOptions(form.principal.options)" 
                                                  :value="option.id" 
                                                  :key="option.id">
                                                    {{ option[form.principal.attr] }}
                                                </option>
                                            </select>
                                          </div>
                                    </div>
                                  <button @click="sendForm(form)" class="button is-danger">Eliminar</button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </template>
    </AdminLayout>
</template>

<script>
import AdminLayout from "@/components/AdminLayout";
import { getAPI } from "@/axios-api";
import Swal from 'sweetalert2';

export default {
    name: 'AdminDelete',
    data () {
        return {
            APIData: {
                "trayectos": { path: "/trayectos/", data: [] },
                "buses": { path: "/buses/", data: [] },
                "choferes": { path: "/choferes/", data: [] },
                "rutas": { path: "/rutas/", data: [] },
                "pasajeros": { path: "/pasajeros/", data: [] },
                "asientos": { path: "/asientos/", data: [] },
            },
            formsOptions: ["Trayecto", "Chofer", "Bus", "Ruta", "Pasajero", "Asiento"],
            actualOption: 'Trayecto',
            forms: [
                {   
                    name: 'Trayecto',
                    path: '/trayectos/',
                    principal: {
                        label: "Seleccione Trayecto",
                        type: "select",
                        options: "trayectos",
                        attr: "nombre",
                        name: "trayecto",
                        data: ""
                    }
                },
                {   
                    name: 'Ruta',
                    path: '/rutas/',
                    principal: {
                        label: "Seleccione Ruta",
                        type: "select",
                        options: "rutas",
                        attr: "id",
                        name: "ruta",
                        data: ""
                    }
                },
                {   
                    name: 'Chofer',
                    path: '/choferes/',
                    principal: {
                        label: "Seleccione Chofer",
                        type: "select",
                        options: "choferes",
                        attr: "nombre",
                        name: "chofer",
                        data: ""
                    }
                },
                {   
                    name: 'Pasajero',
                    path: '/pasajeros/',
                    principal:{
                        label: "Seleccione Pasajero",
                        type: "select",
                        options: "pasajeros",
                        attr: "nombre",
                        name: "pasajero",
                        data: ""
                    }
                },
                {   
                    name: 'Bus',
                    path: '/buses/',
                    principal: {
                        label: "Seleccione Bus",
                        type: "select",
                        options: "buses",
                        attr: "chofer_nombre",
                        name: "bus",
                        data: ""
                    }
                }
            ]
        }
    },
    components: {
        AdminLayout
    },
    created () {
        this.getData();
    },
    methods: {
        getData(){
            let vm = this;
            for (let key in vm.APIData) {
                getAPI.get(vm.APIData[key].path)
                  .then((response) => {
                    vm.APIData[key].data = response.data;
                  })
                  .catch((err) => {
                    console.log(err)
                  })

                setTimeout(()=>{console.log("Making Request...")}, 1000);
            }
        },
        setOption(option){
            this.actualOption = option;
            this.getData();
        },
        getSelectOptions(name){
            return this.APIData[name].data
        },
        getObject(form){
            let path = `${form.path}${form.principal.data}/`

            getAPI.get(path)
              .then((response) => {
                for (let field in form.fields){
                    form.fields[field].data = response.data[form.fields[field].name];
                }
              })
              .catch((err) => {
                console.log(err)
              }) 
        },
        sendForm (form){
            let path = `${form.path}${form.principal.data}/`

            getAPI.delete(path)
             .then(() => {
                Swal.fire(
                  'Se Elimino Correctamente!',
                  `Formulario ${form.name}`,
                  'success'
                )
             })
             .catch(() => {
                Swal.fire(
                  'Falló al Eliminar',
                  `Formulario ${form.name}`,
                  'error'
                )
             });
        }
    }
};
</script>
