import axios from "axios";

export const HTTP_PYTHON = axios.create({
  baseURL: `http://localhost:5000/api`
})

export const HTTP_EXPRESS = axios.create({
  baseURL: `http://localhost:3000/user`
})