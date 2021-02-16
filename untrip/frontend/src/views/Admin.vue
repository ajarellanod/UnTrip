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
                                  <div class="field" v-for="field in form.fields" :key="field.name">
                                    <label class="label">{{field.label}}</label>
                                    <div class="control">
                                      
                                      <input v-if="field.type != 'select'" class="input" v-model="field.data" :type="field.type" :name="field.name" :placeholder="field.placeholder">
                                      
                                      <div v-else class="select is-fullwidth">
                                        <select v-model="field.data" :name="field.name">
                                          <option v-for="option in getSelectOptions(field.options)" :value="option.id" :key="option.id">
                                              {{ option[field.attr] }}
                                          </option>
                                        </select>
                                      </div>
                                      
                                    </div>
                                  </div>
                                  <button @click="sendForm(form)" class="button is-link">Guardar</button>
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
    name: 'Admin',
    data () {
        return {
            APIData: {
                "trayectos": { path: "/trayectos/", data: [] },
                "buses": { path: "/buses/", data: [] },
                "choferes": { path: "/choferes/disponibles/", data: [] },
            },
            formsOptions: ["Trayecto", "Chofer", "Bus", "Ruta", "Pasajero"],
            actualOption: 'Trayecto',
            forms: [
                {   
                    name: 'Trayecto',
                    path: '/trayectos/',
                    fields: [
                        {
                            label: "Nombre del Trayecto",
                            type: "text",
                            placeholder: "Ingrese Nombre",
                            name: "nombre",
                            data: ""
                        },
                        {
                            label: "Duración del Trayecto",
                            type: "text",
                            placeholder: "2 00:01:30",
                            name: "duracion",
                            data: ""
                        },
                    ]
                },
                {   
                    name: 'Ruta',
                    path: '/rutas/',
                    fields: [
                        {
                            label: "Hora de Salida",
                            type: "datetime-local",
                            placeholder: "",
                            name: "salida",
                            data: ""
                        },
                        {
                            label: "Seleccione Trayecto",
                            type: "select",
                            options: "trayectos",
                            attr: "nombre",
                            name: "trayecto",
                            data: ""
                        },
                        {
                            label: "Seleccione Bus",
                            type: "select",
                            options: "buses",
                            attr: "chofer_nombre",
                            name: "bus",
                            data: ""
                        },
                    ]
                },
                {   
                    name: 'Chofer',
                    path: '/choferes/',
                    fields: [
                        {
                            label: "Nombre del Chofer",
                            type: "text",
                            placeholder: "Agrege Chofer",
                            name: "nombre",
                            data: ""
                        },
                        {
                            label: "Edad del Chofer",
                            type: "number",
                            placeholder: "Agrege Edad",
                            name: "edad",
                            data: 18
                        },
                    ]
                },
                {   
                    name: 'Pasajero',
                    path: '/pasajeros/',
                    fields: [
                        {
                            label: "Nombre del Pasajero",
                            type: "text",
                            placeholder: "Agrege Nombre",
                            name: "nombre",
                            data: ""
                        },
                        {
                            label: "Identificación",
                            type: "number",
                            placeholder: "Agrege Identificación",
                            name: "identificacion",
                            data: ""
                        },
                    ]
                },
                {   
                    name: 'Bus',
                    path: '/buses/',
                    fields: [
                        {
                            label: "Seleccione Chofer",
                            type: "select",
                            options: "choferes",
                            attr: "nombre",
                            name: "chofer",
                            data: ""
                        },
                        {
                            label: "Capacidad del Bus",
                            type: "number",
                            placeholder: "Agrege Capacidad",
                            name: "capacidad",
                            data: 10
                        },
                    ]
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
                if (vm.APIData[key].path != ''){
                    getAPI.get(vm.APIData[key].path)
                      .then(response => {
                        vm.APIData[key].data = response.data;
                      })
                      .catch(err => {
                        console.log(err)
                      }) 
                }
            }
        },
        setOption(option){
            this.actualOption = option;
            this.getData();
        },
        getSelectOptions(name){
            return this.APIData[name].data
        },
        sendForm (form){
            let output = {};
            
            for (let field in form.fields) {
                output[form.fields[field].name] = form.fields[field].data;
                form.fields[field].data = "";
            }

            getAPI.post(form.path, output)
             .then(() => {
                Swal.fire(
                  'Guardado Exitosamente!',
                  `Formulario ${form.name}`,
                  'success'
                )
             })
             .catch(() => {
                Swal.fire(
                  'Falló al Guardar',
                  `Formulario ${form.name}`,
                  'error'
                )
             });
        }
    }
};
</script>