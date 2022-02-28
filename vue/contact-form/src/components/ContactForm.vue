<template>
    <Form @submit="onSubmit"  :validation-schema="schema" v-slot="{ errors }" data-vv-scope="contact-form"
          class="marble-contact-form" id="twoRockContactForm" v-if="!submitted">
      <div class="form-group mb-4">
          <label class="form-label visually-hidden">Name</label>
          <Field v-model="name" name="name" type="text" class="form-control" aria-describedby="name of person contacting Two Rock Software" placeholder="Name"/>
          <div class="invalid-feedback text-danger">{{ errors.name }}</div>
      </div>

      <div class="form-group mb-4">
          <label class="form-label visually-hidden">Organization</label>
          <Field v-model="organization" name="organization" type="text" class="form-control" aria-describedby="Organization of person contacting Two Rock Software" placeholder="Organization"/>
          <div class="invalid-feedback text-danger">{{ errors.organization }}</div>
      </div>

      <div class="form-group mb-4">
          <label class="form-label visually-hidden">Email</label>
          <Field v-model="email" name="email" type="text" class="form-control" aria-describedby="Email address of person contacting Two Rock Software" placeholder="Email"/>
          <div class="invalid-feedback text-danger">{{ errors.email }}</div>
      </div>

      <div class="form-group row mb-4">
        <div class="col-7">
          <label class="form-label visually-hidden">Email</label>
          <Field v-model="phone_number" name="phone_number" type="tel" class="form-control" aria-describedby="Phone Number of person contacting Two Rock Software"
                 placeholder="Phone Number" v-mask="['(###) ###-####', '(###) ###-#### Ext. ####']"/>
          <div class="invalid-feedback text-danger">{{ errors.phone_number }}</div>
        </div>
        <div class="col-5">
          <label class="form-label visually-hidden">Budget</label>
          <Field v-model="budget" name="budget" type="text" class="form-control" aria-describedby="Budget allocated for project"
                 placeholder="Budget" />
          <div class="invalid-feedback text-danger">{{ errors.budget }}</div>
        </div>
      </div>

      <div class="form-group mb-4">
          <label class="form-label visually-hidden" for="message">Email</label>
          <Field v-slot="{ field }" v-model="message" name="message">
            <textarea v-bind="field" class="form-control" aria-describedby="Message"
                   placeholder="What can we build together?" rows="4" id="message"></textarea>
          </Field>
          <div class="invalid-feedback text-danger">{{ errors.message }}</div>
      </div>

      <button type="submit" class="btn btn-outline-white">Let's Rock</button>
    </Form>
    <div class="server-messages" v-if="submitted">
      <div class="row marble-rock-row">
        <div class="col-lg-8 marble-rock" style="background-image: url('/static/backgrounds/rock-home-2.svg');">
            {{ server_message }}
        </div>

        <div v-if="server_error" id="server-error">
          <a href="#" style="background-image: url('/static/backgrounds/rock-nav-0.7514b350bc1e.svg');" class="marble-rock" @click="showForm()">Show Form</a>
        </div>
      </div>
    </div>
</template>

<script>
import axios from 'axios'
import * as Yup from 'yup'
import { Form, Field } from 'vee-validate'

export default {
  name: 'ContactForm',
  setup () {
    const schema = Yup.object().shape({
      name: Yup.string().required().label("Name"),
      organization: Yup.string().required().label("Organization"),
      email: Yup.string().email().required().label("Email"),
      phone_number: Yup.string().required().label("Phone number"),
      message: Yup.string().required().label("Message"),
      budget: Yup.string().matches(/^\$?-?0*(?:\d+(?!,)(?:\.\d{1,2})?|(?:\d{1,3}(?:,\d{3})*(?:\.\d{1,2})?))$/, "Please enter a valid amount")
    })

    return {
      schema
    }
  },
  data () {
    return {
      name: '',
      email: '',
      organization: '',
      phone_number: '',
      message: '',
      budget: '',
      submitted: false,
      submitting: false,
      server_message: '',
      server_error: false
    }
  },
  methods: {
    async recaptcha() {
      // (optional) Wait until recaptcha has been loaded.
      await this.$recaptchaLoaded()

      // Execute reCAPTCHA with action "login".
      const token = await this.$recaptcha('contact')
      return token
    },
    showForm() {
      this.submitted = false
    },
    onSubmit(values) {
      // do not allow multiple submission while one is processing
      if (this.submitting) {
        return false
      }
      // get recapcha token
      const token = this.recaptcha()
      token.then(value => {
        // set submitting to true so that double clicking hits the if statement above
        this.submitting = true
        const url = '/contact-submit/'
        values.g_recaptcha_response = value
        axios.post(url, values).then((response) => {
          this.submitting = false
          this.submitted = true
          this.server_message = response.data.message
          if (response.data.errors) {
            this.server_error = true
          }
        }).catch((error) => {
          console.log(error)
          this.submitted = true
          this.submitting = false
          this.server_message = 'A server error has occurred, please try again later.'
        })
      })
    },
  },
  components: {
    Form,
    Field
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.error {
  color: red;
  text-align: left;
}
div.server-messages {
  min-height: 500px;
}
#server-error a {
  color: white;
  font-weight: bolder;
}
</style>
