import firebase from 'firebase/compat/app'
import 'firebase/compat/firestore'
import 'firebase/compat/storage'
import {firebaseInfor} from '@/config.js'


export const fb = firebase.initializeApp(firebaseInfor)

export const convertToSlug = (Text) => {
    return Text.toLowerCase()
               .replace(/[^\w ]+/g, '')
               .replace(/ +/g, '-');
  }