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
          // this.response = JSON.stringify(response, null, 2)
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
    <div class=label-test>
      <label for="query">Busca:</label><br>
      <input id="query" type="text" v-model="query" required/>
    </div>
    
    <button :class="[query ? activeClass : '']" type="submit" id="my-button">Pesquisar</button>
        <div v-if="success">
          {{ success }}
          <div v-for="item in response.products" :key="item" class="my-card" style="width:28rem;">
            <p>Produto: {{item.descricao}}</p>
            <p>Marca: {{item.marca}}</p>
            
            <div v-if="item.valores[0].individual">
              <p>Valor individual: {{item.valores[0].individual}}</p>
            </div>
            <div v-if="item.desconto != null">
              <p> Promoção: {{item.desconto}}</p>
            </div>
            <div v-if="item.valores[0].promocao">
              <p>Desconto em compra em combo: {{item.desconto}}</p>
              <p>Valor individual da compra em combo: {{item.valores[0].promocao}}</p>
            </div>  
          </div>
      </div>
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

#my-button{
  margin-top:20px;
}

.my-card {
  /* Add shadows to create the "card" effect */
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
  border-radius: 5px; /* 5px rounded corners */
  margin:20px;
  text-align: left;
}

/* On mouse-over, add a deeper shadow */
.my-card:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}

/* Add some padding inside the card container */
.container {
  padding: 2px 16px;
}


.searchbar {
  font-size: 1rem;
  font-family: monospace;
  text-align: center;
  width: 18rem;
  padding-bottom: 10123090px;
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
