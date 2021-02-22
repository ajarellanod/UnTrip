<template>
  <Layout>
    <template v-slot:body>
      <div class="container has-text-centered">
        <div class="columns is-vcentered">
          <div class="column is-5">
            <figure class="image is-4by3 sombra">
              <img
                src="https://picsum.photos/800/600/?random"
                alt="Description"
              />
            </figure>
          </div>
          <div class="column is-6 is-offset-1">
            <h1 class="title is-2">
              Descubre Tú Destino
            </h1>
            <p class="subtitle is-4">
              Ve rapido a tu destino, con seguridad y confort!
            </p>
            <br />
            <p class="has-text-centered">
              <router-link
                to="/trayectos"
                class="button is-medium is-link is-outlined"
              >
                Empezemos &#x1F68D;
              </router-link>
              <br />
              <span class="content is-small">
                *No Necesitas Registros
              </span>
            </p>
          </div>
        </div>
      </div>
    </template>
  </Layout>
</template>

<script>
import Layout from "@/components/Layout";

export default {
  components: {
    Layout
  }
};
</script>
