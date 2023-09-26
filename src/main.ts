import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { Amplify, Auth } from 'aws-amplify'

const app = createApp(App)

app.use(router)

app.mount('#app')

const redirectURL = window.location.origin + window.location.path

Amplify.configure({
  Auth: {
    // REQUIRED only for Federated Authentication - Amazon Cognito Identity Pool ID
    //identityPoolId: 'XX-XXXX-X:XXXXXXXX-XXXX-1234-abcd-1234567890ab',

    // REQUIRED - Amazon Cognito Region
    region: 'us-east-1',

    // OPTIONAL - Amazon Cognito Federated Identity Pool Region
    // Required only if it's different from Amazon Cognito Region
    //identityPoolRegion: 'XX-XXXX-X',

    // OPTIONAL - Amazon Cognito User Pool ID
    userPoolId: 'us-east-1_mjewQwwHp',

    // OPTIONAL - Amazon Cognito Web Client ID (26-char alphanumeric string)
    userPoolWebClientId: '4evgbmouciqv3vodnoafsp4rag',

    // OPTIONAL - Enforce user authentication prior to accessing AWS resources or not
    //mandatorySignIn: false,

    // OPTIONAL - This is used when autoSignIn is enabled for Auth.signUp
    // 'code' is used for Auth.confirmSignUp, 'link' is used for email link verification
    //signUpVerificationMethod: 'code', // 'code' | 'link'

    // OPTIONAL - Configuration for cookie storage
    // Note: if the secure flag is set to true, then the cookie transmission requires a secure protocol
    /*cookieStorage: {
      // REQUIRED - Cookie domain (only required if cookieStorage is provided)
      domain: 'localhost',
      // OPTIONAL - Cookie path
      path: '/',
      // OPTIONAL - Cookie expiration in days
      expires: 365,
      // OPTIONAL - See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie/SameSite
      sameSite: 'lax',//'strict' | 'lax',
      // OPTIONAL - Cookie secure flag
      // Either true or false, indicating if the cookie transmission requires a secure protocol (https).
      secure: true,
    },*/

    // OPTIONAL - customized storage object
    //storage: MyStorage,

    // OPTIONAL - Manually set the authentication flow type. Default is 'USER_SRP_AUTH'
    //authenticationFlowType: 'USER_PASSWORD_AUTH',

    // OPTIONAL - Manually set key value pairs that can be passed to Cognito Lambda Triggers
    //clientMetadata: {myCustomKey: 'myCustomValue'},

    // OPTIONAL - Hosted UI configuration
    oauth: {
      domain: 'herdmentality.auth.us-east-1.amazoncognito.com',
      scope: ['phone', 'email', 'profile', 'openid', 'aws.cognito.signin.user.admin'],
      redirectSignIn: redirectURL,
      //redirectSignOut: 'http://localhost:3000/',
      responseType: 'code' // or 'token', note that REFRESH token will only be generated when the responseType is code
    }
  }
})

// You can get the current config object
const currentConfig = Auth.configure()
