
<template>
  <div class="searchbar">
    <input class="green" type="text" placeholder="Faça aqui sua busca" />
    <h1 class="green">{{ msg }}</h1>
    <h3>
      This is a table
      <a href="https://vitejs.dev/" target="_blank" rel="noopener">Vite</a> +
      <a href="https://vuejs.org/" target="_blank" rel="noopener">Vue 3</a>.
    </h3>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  top: -10px;
}

.searchbar {
  font-size: 1.2rem;
  font-family: monospace;
  text-align: center;
}

h3 {
  font-size: 1.2rem;
}
.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
