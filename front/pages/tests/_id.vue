<template>
  <div>
    {{ id }}
    {{ testData }}
    {{ testSolverType }}
  </div>
</template>

<script>

export default {
  asyncData ({ params }) {
    const id = params.id // When calling /abc the slug will be "abc"
    return { id }
  },
  data () {
    return {
      testData: {},
      testSolverType: {},
      testRuns: []
    }
  },
  mounted () {
    this.setTestData(this.id)
  },
  methods: {
    setTestData (testId) {
      this.$axios.get(
        'http://localhost:7777/test/' + testId
      )
        .then((response) => {
          this.testData = response.data
          this.setTestSolverType(this.testData.solver_type)
        })
    },
    setTestSolver (solverId) {
      this.$axios.get(
        'http://localhost:7777/solver/' + solverId
      )
        .then((response) => {
          this.testSolver = response.data
        })
    },
    setTestSolverType (solverTypeId) {
      this.$axios.get(
        'http://localhost:7777/solver_type/' + solverTypeId
      )
        .then((response) => {
          this.testSolverType = response.data
        })
    }
  }
}
</script>

<style scoped>

</style>
