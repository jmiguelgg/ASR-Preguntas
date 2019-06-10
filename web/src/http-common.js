import axios from "axios";

export const HTTP_PYTHON = axios.create({
  baseURL: `http://localhost:5000/api`
})

export const HTTP_EXPRESS = axios.create({
  baseURL: `http://localhost:3000/user`
})

export const HTTP_EXPRESS_TABLA_4 = axios.create({
  baseURL: `http://localhost:3000/tabla4`
})