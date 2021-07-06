<template>
    <Form :validation-schema="schema" v-slot="{ errors }" data-vv-scope="contact-form" class="marble-contact-form" id="twoRockContactForm">
      <div class="form-group mb-4">
          <label class="form-label visually-hidden">Name</label>
          <Field v-model="name" name="name" type="text" class="form-control" aria-describedby="name of person contacting Two Rock Software" placeholder="Name"/>
          <div class="invalid-feedback errorlist">{{ errors.name }}</div>
      </div>

      <div class="form-group mb-4">
          <label class="form-label visually-hidden">Organization</label>
          <Field v-model="org" name="org" type="text" class="form-control" aria-describedby="Organization of person contacting Two Rock Software" placeholder="Organization"/>
          <div class="invalid-feedback errorlist">{{ errors.org }}</div>
      </div>

      <div class="form-group mb-4">
          <label class="form-label visually-hidden">Email</label>
          <Field v-model="email" name="email" type="text" class="form-control" aria-describedby="Email address of person contacting Two Rock Software" placeholder="Email"/>
          <div class="invalid-feedback errorlist">{{ errors.email }}</div>
      </div>

      <div class="form-group mb-4">
          <label class="form-label visually-hidden">Email</label>
          <Field v-model="phone_number" name="phone_number" type="tel" class="form-control" aria-describedby="Phone Number of person contacting Two Rock Software"
                 placeholder="Phone Number" v-mask="['(###) ###-####', '(###) ###-#### Ext. ####']"/>
          <div class="invalid-feedback errorlist">{{ errors.phone_number }}</div>
      </div>
    </Form>
</template>

<script>
import * as Yup from 'yup'
import { Form, Field } from 'vee-validate'

export default {
  name: 'ContactForm',
  setup () {
    const schema = Yup.object().shape({
      name: Yup.string().required(),
      org: Yup.string().required(),
      email: Yup.string().email().required(),
      phone_number: Yup.string().required(),
      // city: Yup.string(),
      // // .matches(/^[0-9]{5}(?:-[0-9]{4})?$/, 'Must be 5 or 9 digits')
      // zipcode: Yup.string().required().matches(/^[0-9]+$/, 'Must be only digits').min(5, 'Must be exactly 5 digits').max(5, 'Must be exactly 5 digits'),
      // cardNumber: Yup.string().required(),
      // expireDate: Yup.string().required(),
      // cvv: Yup.string(3).required()
    })

    return {
      schema
    }
  },
  data () {
    return {
      name: '',
      email: '',
      org: '',
      phone_number: ''
    }
  },
  props: {
    msg: String
  },
  components: {
    Form,
    Field
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
