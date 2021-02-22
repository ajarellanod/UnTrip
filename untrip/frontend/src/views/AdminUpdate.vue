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
                    @click="setOption(form)"
                    :key="form.name"
                    :class="{ 'is-active': actualForm === form.name }"
                  >
                    <a>{{ form.name }}</a>
                  </li>
                </ul>
              </div>
              <div class="forms">
                <form
                  @submit.prevent
                  v-for="form in forms"
                  v-show="actualForm == form.name"
                  :key="form.name"
                >
                  <!-- Principal Field -->
                  <div class="field">
                    <label class="label">
                      {{ form.principal.label }}
                    </label>
                    <div class="select is-fullwidth">
                      <select
                        v-model="form.principal.data"
                        @change="getPrincipal(form)"
                        :name="form.principal.name"
                      >
                        <option
                          :value="option.id"
                          :key="option.id"
                          v-for="option in getSelectOptions(
                            form.principal.options
                          )"
                        >
                          {{ option[form.principal.attr] }}
                        </option>
                      </select>
                    </div>
                  </div>
                  <!-- Fields -->
                  <div
                    class="field"
                    v-for="field in form.fields"
                    :key="field.name"
                  >
                    <label class="label">
                      {{ field.label }}
                    </label>
                    <div class="control">
                      <input
                        class="input"
                        v-model="field.data"
                        :type="field.type"
                        :placeholder="field.placeholder"
                        v-if="
                          (field.type != 'select') & (field.type != undefined)
                        "
                        :name="field.name"
                      />

                      <div
                        v-else-if="field.options"
                        class="select is-fullwidth"
                      >
                        <select v-model="field.data" :name="field.name">
                          <option
                            :value="option.id"
                            :key="option.id"
                            v-for="option in getSelectOptions(field.options)"
                          >
                            {{ option[field.attr] }}
                          </option>
                        </select>
                      </div>
                    </div>
                  </div>
                  <button @click="sendFormData(form)" class="button is-primary">
                    Actualizar
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
import Swal from "sweetalert2";

export default {
  name: "AdminUpdate",
  data() {
    return {
      APIData: {
        trayectos: { path: "/trayectos/", data: [] },
        buses: { path: "/buses/", data: [] },
        choferes: { path: "/choferes/", data: [] },
        rutas: { path: "/rutas/", data: [] },
        pasajeros: { path: "/pasajeros/", data: [] },
        asientos: { path: "/asientos/", data: [] }
      },
      actualForm: "Trayecto",
      forms: [
        {
          name: "Trayecto",
          path: "/trayectos/",
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
              name: "duracion",
              data: ""
            }
          ]
        },
        {
          name: "Ruta",
          path: "/rutas/",
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
              label: "Hora de Llegada",
              type: "datetime-local",
              placeholder: "",
              name: "llegada",
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
            }
          ]
        },
        {
          name: "Chofer",
          path: "/choferes/",
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
              data: 18,
              fixed: 18
            }
          ]
        },
        {
          name: "Pasajero",
          path: "/pasajeros/",
          principal: {
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
            }
          ]
        },
        {
          name: "Bus",
          path: "/buses/",
          principal: {
            label: "Seleccione Bus",
            type: "select",
            options: "buses",
            attr: "id",
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
              name: "capacidad",
              data: 10,
              fixed: 10
            }
          ]
        },
        {
          name: "Asiento",
          path: "/asientos/",
          principal: {
            label: "Seleccione Asiento",
            type: "select",
            options: "asientos",
            attr: "nombre",
            name: "asiento",
            data: ""
          },
          fields: [
            {
              label: "Pasajero Asignado",
              type: "select",
              options: "pasajeros",
              attr: "nombre",
              name: "pasajero",
              data: ""
            },
            {
              name: "ruta",
              data: ""
            },
            {
              name: "identificador",
              data: ""
            }
          ]
        }
      ]
    };
  },
  components: {
    AdminLayout
  },
  created() {
    let index = 0;
    while (this.forms[index].name != this.actualForm) {
      index++;
    }
    this.getFieldData(this.forms[index].principal);
    this.getFormData(this.forms[index].fields);
  },
  methods: {
    getFieldData(field) {
      if (field.options) {
        let api = this.APIData[field.options];
        getAPI
          .get(api.path)
          .then(response => {
            api.data = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      }
    },
    getFormData(fields) {
      for (let key in fields) {
        this.getFieldData(fields[key]);
      }
    },
    setOption(form) {
      this.actualForm = form.name;
      this.getFieldData(form.principal);
      this.getFormData(form.fields);
    },
    getSelectOptions(name) {
      return this.APIData[name].data;
    },
    getPrincipal(form) {
      let path = `${form.path}${form.principal.data}/`;
      let fields = form.fields;
      getAPI
        .get(path)
        .then(response => {
          for (let key in fields) {
            fields[key].data = response.data[fields[key].name];
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    sendFormData(form) {
      let output = {};
      let path = `${form.path}${form.principal.data}/`;
      let fields = form.fields;
      form.principal.data = "";

      for (let key in fields) {
        output[fields[key].name] = fields[key].data;

        if (fields[key].fixed) {
          fields[key].data = fields[key].fixed;
        } else {
          fields[key].data = "";
        }
      }

      getAPI
        .put(path, output)
        .then(() => {
          Swal.fire(
            "Actualizado Exitosamente!",
            `Formulario ${form.name}`,
            "success"
          );
        })
        .catch(() => {
          Swal.fire("Falló al Guardar", `Formulario ${form.name}`, "error");
        });
    }
  }
};
</script>
