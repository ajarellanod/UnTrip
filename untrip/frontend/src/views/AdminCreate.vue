<template>
    <AdminLayout>
        <template v-slot:body>
            <div class="container">
                <div class="columns">
                    <div class="column is-6 is-offset-3">
                        <div class="box">
                            <div class="tabs is-centered is-boxed">
                              <ul>
                                <li 
                                v-for="form in forms" 
                                :key="form.name"
                                :class="{ 'is-active': actualForm === form.name }"
                                @click="setOption(form)"
                                >
                                    <a>{{form.name}}</a>
                                </li>
                              </ul>
                            </div>
                            <div class="forms">
                                <form 
                                @submit.prevent 
                                v-show="actualForm == form.name" 
                                v-for="form in forms" 
                                :key="form.name"
                                >
                                  <div class="field" v-for="field in form.fields" :key="field.name">
                                    <label class="label">
                                        {{field.label}}
                                    </label>
                                    <div class="control">
                                      <input 
                                      class="input" 
                                      v-model="field.data" 
                                      :type="field.type" 
                                      :name="field.name" 
                                      :placeholder="field.placeholder"
                                      v-if="!field.options" 
                                      />
                                      <div v-else class="select is-fullwidth">
                                        <select v-model="field.data" :name="field.name">
                                          <option 
                                          v-for="option in getSelectOptions(field.options)" 
                                          :value="option.id" 
                                          :key="option.id"
                                          >
                                              {{ option[field.attr] }}
                                          </option>
                                        </select>
                                      </div>
                                    </div>
                                  </div>
                                  <button @click="sendFormData(form)" class="button is-link">
                                    Guardar
                                  </button>
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
    name: 'AdminCreate',
    data () {
        return {
            APIData: {
                "trayectos": { path: "/trayectos/", data: [] },
                "buses": { path: "/buses/", data: [] },
                "choferes": { path: "/choferes/disponibles/", data: [] },
            },
            actualForm: 'Trayecto',
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
                            attr: "id",
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
        let index = 0;
        while(this.forms[index].name != this.actualForm){
            index++;
        }
        this.getFormData(this.forms[index].fields);
    },
    methods: {
        getFieldData(field){
            if (field.options) {
                let api = this.APIData[field.options];
                getAPI.get(api.path)
                  .then((response) => {
                    api.data = response.data;
                  })
                  .catch((error) => {
                    console.log(error.data);
                  });
            }
        },
        getFormData(fields){
            for(let key in fields){
                this.getFieldData(fields[key]);
            }
        },
        setOption(form){
            this.actualForm = form.name;
            this.getFormData(form.fields);
        },
        getSelectOptions(options){
            return this.APIData[options].data
        },
        sendFormData(form){
            let output = {};
            let fields = form.fields;

            for (let key in fields) {
                output[fields[key].name] = fields[key].data;
                fields[key].data = "";
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