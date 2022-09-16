<script>
  import axios from "axios"
  
  export default {
    data() {
      return {
        products: '',
        response: '',
        success: '',
        activeClass: 'active'
      }
    },
    methods: {
      submitForm() {
        axios.post('http://127.0.0.1:8000/v1/', {
          "query": this.query,
        }).then(response => {
          console.log(query)
          console.log(response);
          console.log(response.data)
          this.response = response.data
          this.success = 'Dados recuperados com sucesso';
          this.response = JSON.stringify(response, null, 2)
        }).catch(error => {
          this.response = 'Erro: ' + error.response.status
        })
        this.products = '';
      }
    }
  }  
</script>

<template>

  <div class="searchbar" id="app">
  <form @submit.prevent="submitForm">
    <div>
      <label for="query">Busca:</label><br>
      <input id="query" type="text" v-model="query" required/>
    </div>
    
    <button :class="[query ? activeClass : '']" type="submit">Faça sua pesquisa</button>
    <div>
      <p v-if="success"> {{ success }}</p>
      <v-card>
        asdadkl
      </v-card>
      <pre>{{ response }}</pre>
    </div>
  </form>
</div>

</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 1.8rem;
  top: -10px;
}



.searchbar {
  font-size: 1rem;
  font-family: monospace;
  text-align: center;
  width: 18rem;
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
