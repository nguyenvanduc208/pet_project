import axios from "axios";

const API_URL = "http://localhost:8000/";

const login = (credentials) => {
  return axios
    .post(`${API_URL}authen/login/`, credentials)
    .then((response) => {
      sessionStorage.setItem("token", JSON.stringify(response.data));

      return response;
    })
    .catch((error) => {
      return false;
    });
};

export default {
  login,
};
