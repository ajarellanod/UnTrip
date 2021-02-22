<template>
  <div class="hero is-fullheight is-default is-bold">
    <div class="hero-head">
      <nav class="navbar">
        <div class="container">
          <div class="navbar-brand">
            <a class="navbar-item">
              <h4 class="title is-4 logo">
                UnTrip
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
                    <router-link to="/">
                      Inicio
                    </router-link>
                  </li>
                  <li>
                    <router-link to="/trayectos">
                      Trayectos
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

<style>
body {
  background: aliceblue;
}

.logo {
  font-family: "Reggae One", cursive;
}

.sombra {
  -webkit-box-shadow: -4px 5px 10px 3px rgba(102, 102, 102, 0.4);
  -moz-box-shadow: -4px 5px 10px 3px rgba(102, 102, 102, 0.4);
  box-shadow: -4px 5px 10px 3px rgba(102, 102, 102, 0.4);
}

.avatar {
  margin-top: -70px;
  padding-bottom: 20px;
}
.avatar img {
  padding: 5px;
  background: #fff;
  border-radius: 50%;
  -webkit-box-shadow: 0 2px 3px rgba(10, 10, 10, 0.1),
    0 0 0 1px rgba(10, 10, 10, 0.1);
  box-shadow: 0 2px 3px rgba(10, 10, 10, 0.1), 0 0 0 1px rgba(10, 10, 10, 0.1);
}
</style>
