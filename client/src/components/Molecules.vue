<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Molecules</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm"
                v-b-modal.molecule-modal>Add Molecule</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">fName</th>
              <th scope="col">Mass</th>
              <th scope="col">Plot?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
              <tr v-for="(molecule, index) in molecules" :key="index">
              <td>{{ molecule.fName }}</td>
              <td>{{ molecule.Mass }}</td>
              <td>
                <span v-if="molecule.Plot">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-danger btn-sm" @click="deleteMol(Mol)">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <!--First Modal-->
      <b-modal ref="addStatusModal"
             id="status-modal"
             title="Add a new staus"
             hide-backdrop hide-footer>
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-name-group"
                    label="name:"
                    label-for="form-name-input">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="addStatusForm.name"
                        required
                        placeholder="Enter name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-type-group"
                      label="type:"
                      label-for="form-type-input">
            <b-form-input id="form-type-input"
                          type="text"
                          v-model="addStatusForm.type"
                          required
                          placeholder="Enter type">
            </b-form-input>
        </b-form-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
    <!--End of First Modal-->

    
  </div>
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
    initForm() {
      this.addMoleculeForm.fName = '';
      this.addMoleculeForm.Mass = '';
      this.addMoleculeForm.plot = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addMoleculeModal.hide();
      let plot = false;
      if (this.addMoleculeForm.plot[0]) plot = true;
      const payload = {
        fName: this.addMoleculeForm.fName,
        Mass: this.addMoleculeForm.Mass,
        plot, // property shorthand
      };
      this.addMolecule(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addMoleculeModal.hide();
      this.initForm();
    },
  },
  removeMol(molId) {
  const path = `http://localhost:5000/Molecules/${molId}`;
  axios.delete(path)
    .then(() => {
      this.getmolecules();
    })
    .catch((error) => {
      // eslint-disable-next-line
      console.error(error);
      this.getmolecules();
    });
},

// Handle Delete Button
deleteMol(mol) {
  this.removeMol(mol.id);
},
  created() {
    this.getmolecules();
  },
};
</script>
