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
                                :key="form.name">

                                  <!-- Principal Field -->
                                   <div class="field">
                                      <label class="label">
                                        {{form.principal.label}}
                                      </label>                                 
                                      <div class="select is-fullwidth">
                                        <select 
                                        v-model="form.principal.data" 
                                        @change="getPrincipal(form)" 
                                        :name="form.principal.name">
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
                                  <button @click="sendFormData(form)" class="button is-danger">
                                    Eliminar
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
            actualForm: 'Trayecto',
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
                        attr: "id",
                        name: "bus",
                        data: ""
                    }
                },
                {   
                    name: 'Asiento',
                    path: '/asientos/',
                    principal: {
                        label: "Seleccione Asiento",
                        type: "select",
                        options: "asientos",
                        attr: "id",
                        name: "asiento",
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
        let index = 0;
        while(this.forms[index].name != this.actualForm){
            index++;
        }
        this.getFieldData(this.forms[index].principal);
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
                    console.log(error);
                  });
            }
        },
        setOption(form){
            this.actualForm = form.name;
            this.getFieldData(form.principal);
        },
        getSelectOptions(name){
            return this.APIData[name].data
        },
        getPrincipal(form){
            let path = `${form.path}${form.principal.data}/`
            let fields = form.fields;
            getAPI.get(path)
              .then((response) => {
                for (let key in fields){
                    fields[key].data = response.data[fields[key].name];
                }
              })
              .catch((error) => {
                console.log(error)
              }) 
        },
        sendFormData(form){
            let path = `${form.path}${form.principal.data}/`

            getAPI.delete(path)
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