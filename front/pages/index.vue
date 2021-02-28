<template>
  <div>
    <div class="d-flex flex-row">
      <div class="d-flex pa-2">
        <div>
          <h3>SolverTypes</h3>
          <v-data-table
            :headers="solverTypesHeaders"
            :items="solverTypes.objects"
            :items-per-page="10"
            class="elevation-1"
          />
        </div>
      </div>
      <div class="d-flex pa-2">
        <div>
          <h3>Solvers</h3>
          <v-data-table
            :headers="solversHeaders"
            :items="solvers.objects"
            :items-per-page="10"
            class="elevation-1"
          />
        </div>
      </div>
    </div>
    <div class="pa-2">
      <h3>Tests</h3>
      <v-data-table
        :headers="testsHeaders"
        :items="tests.objects"
        :items-per-page="10"
        class="elevation-1"
      />
    </div>
  </div>
</template>

<script>

export default {
  components: {},
  data () {
    return {
      solverTypes: [],
      solverTypesHeaders: [
        { text: 'Id', value: 'id' },
        { text: 'Name', value: 'name' }
      ],
      solvers: [],
      solversHeaders: [
        { text: 'Id', value: 'id' },
        { text: 'SolverType', value: 'solver_type' },
        { text: 'Name', value: 'name' }
      ],
      tests: [],
      testsHeaders: [
        { text: 'Id', value: 'id' },
        { text: 'SolverType', value: 'solver_type' },
        { text: 'Name', value: 'name' }
      ],
      testRuns: []
    }
  },
  mounted () {
    this.updateSolverTypes()
    this.updateSolvers()
    this.updateTests()
  },
  methods: {
    updateSolverTypes () {
      this.$axios.get(
        'http://localhost:7777/solver_type'
      )
        .then(
          (response) => {
            this.solverTypes = response.data
          }
        )
    },
    updateSolvers () {
      this.$axios.get(
        'http://localhost:7777/solver'
      )
        .then(
          (response) => {
            this.solvers = response.data
          }
        )
    },
    updateTests () {
      this.$axios.get(
        'http://localhost:7777/test'
      )
        .then(
          (response) => {
            this.tests = response.data
          }
        )
    }
  }
}
</script>
