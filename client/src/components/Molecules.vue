<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Molecules</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm">Add Molecule</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">fName</th>
              <th scope="col">Mass</th>
              <th scope="col">Plot</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr>
               <tr v-for="(molecule, index) in molecules" :key="index">
              <td>{{ molecule.fName }}</td>
              <td>{{ molecule.Mass }}</td>
              <td>
                <span v-if="molecule.plot">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Update</button>
                  <button type="button" class="btn btn-danger btn-sm">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
  <b-modal ref="addMoleculeModal"
         id="molecule-modal"
         title="Add a new molecule"
         hide-footer>
    <b-form @submit="onSubmit" @reset="onReset" class="w-100">
    <b-form-group id="form-fName-group"
                label="fName:"
                label-for="form-fName-input">
      <b-form-input id="form-fName-input"
                    type="text"
                    v-model="addMoleculeForm.fName"
                    required
                    placeholder="Enter name">
      </b-form-input>
    </b-form-group>
    <b-form-group id="form-Mass-group"
                  label="Mass:"
                  label-for="form-Mass-input">
        <b-form-input id="form-Mass-input"
                      type="text"
                      v-model="addMoleculeForm.Mass"
                      required
                      placeholder="Enter mass">
        </b-form-input>
      </b-form-group>
    <b-form-group id="form-plot-group">
      <b-form-checkbox-group v-model="addMoleculeForm.plot" id="form-checks">
        <b-form-checkbox value="true">plot?</b-form-checkbox>
      </b-form-checkbox-group>
    </b-form-group>
    <b-button type="submit" variant="primary">Submit</b-button>
    <b-button type="reset" variant="danger">Reset</b-button>
  </b-form>
</b-modal>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      molecules: [],
      addMoleculeForm: {
        fName: '',
        Mass: '',
        plot: [],
      },
    };
  },
  methods: {
    getmolecules() {
      const path = 'http://localhost:5000/Molecules';
      axios.get(path)
        .then((res) => {
          this.molecules = res.data.molecules;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addMolecule(payload) {
      const path = 'http://localhost:5000/Molecules';
      axios.post(path, payload)
        .then(() => {
          this.getmolecules();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getmolecules();
        });
    },
  },
  created() {
    this.getmolecules();
  },
};
</script>
