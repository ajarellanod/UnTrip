<template>
<Layout>
<template v-slot:body>
    <div class="container has-text-centered">
        <div class="columns is-vcentered">
            <div class="column is-6">
                <article class="panel is-link">
                  <p class="panel-heading logo">
                    Trayectos
                  </p>
                  <p class="panel-tabs">
                    <a class="is-active">Todos</a>
                    <a>Cortos</a>
                    <a>Largos</a>
                    <a>Internacionales</a>
                  </p>
                  <div class="panel-block">
                    <p class="control has-icons-left">
                      <input class="input is-link" type="text" placeholder="Search">
                      <span class="icon is-left">
                        <i class="fas fa-search" aria-hidden="true"></i>
                      </span>
                    </p>
                  </div>
                  <a v-for="trayecto in APIData" :key="trayecto.id" class="panel-block is-active">
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
            APIData: []
        }
    },
    created () {
        getAPI.get("/trayectos/")
          .then(response => {
            this.APIData = response.data
          })
          .catch(err =>{
            console.log(err)
          })
    },
    components: {
        Layout
    }
};
</script>
