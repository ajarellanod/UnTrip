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

                                  <!-- Fields -->
                                  <div class="field" v-for="field in form.fields" :key="field.name">
                                    <label class="label">{{field.label}}</label>
                                    
                                    <div class="control">
                                      <!-- Input -->
                                      <input v-if="field.type != 'select'" class="input" v-model="field.data" :type="field.type" :name="field.name" :placeholder="field.placeholder">

                                      <!-- Or Select -->
                                      <div v-else class="select is-fullwidth">
                                        <select v-model="field.data" :name="field.name">
                                          <option v-for="option in getSelectOptions(field.options)" :value="option.id" :key="option.id">
                                              {{ option[field.attr] }}
                                          </option>
                                        </select>
                                      </div>
                                    </div>
                                  </div>
                                  <button @click="sendForm(form)" class="button is-link">Actualizar</button>
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
    name: 'AdminUpdate',
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
                    },
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
                    principal: {
                        label: "Seleccione Ruta",
                        type: "select",
                        options: "rutas",
                        attr: "id",
                        name: "ruta",
                        data: ""
                    },
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
                    principal: {
                        label: "Seleccione Chofer",
                        type: "select",
                        options: "choferes",
                        attr: "nombre",
                        name: "chofer",
                        data: ""
                    },
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
                    principal:{
                        label: "Seleccione Pasajero",
                        type: "select",
                        options: "pasajeros",
                        attr: "nombre",
                        name: "pasajero",
                        data: ""
                    },
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
                    principal: {
                        label: "Seleccione Bus",
                        type: "select",
                        options: "buses",
                        attr: "chofer_nombre",
                        name: "bus",
                        data: ""
                    },
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
                getAPI.get(vm.APIData[key].path)
                  .then(response => {
                    vm.APIData[key].data = response.data;
                  })
                  .catch(err => {
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
            let output = {};
            let path = `${form.path}${form.principal.data}/`
            
            for (let field in form.fields) {
                output[form.fields[field].name] = form.fields[field].data;
                form.fields[field].data = "";
            }

            getAPI.put(path, output)
             .then(() => {
                Swal.fire(
                  'Actualizado Exitosamente!',
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
