<template>
  <div class="hero is-fullheight is-default is-bold">
    <div class="hero-head">
      <nav class="navbar">
        <div class="container">
          <div class="navbar-brand">
            <a class="navbar-item">
              <h4 class="title is-4 logo">
                Admin UnTrip
              </h4>
            </a>
            <span class="navbar-burger burger" data-target="navbarMenu">
              <span></span>
              <span></span>
              <span></span>
            </span>
          </div>
          <div id="navbarMenu" class="navbar-menu">
            <div class="navbar-end">
              <div class="tabs is-right">
                <ul>
                  <li>
                    <router-link to="/admin/create">
                      Creación
                    </router-link>
                  </li>
                  <li>
                    <router-link to="/admin/update">
                      Actualización
                    </router-link>
                  </li>
                  <li>
                    <router-link to="/admin/delete">
                      Eliminación
                    </router-link>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </nav>
    </div>
    <div class="hero-body">
      <slot name="body"></slot>
    </div>
    <div class="hero-foot">
      <div class="container">
        <div class="tabs is-centered">
          <ul>
            <li><a></a></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.logo {
  font-family: "Reggae One", cursive;
}

.hero-body,
.hero-foot {
  background: #dbdbdb;
}
</style>
