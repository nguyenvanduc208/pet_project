import axios from "axios";
import Cookies from "js-cookie";
import { API_URL } from "@/config.js";

const login = (credentials) => {
  return axios
    .post(`${API_URL}/authen/login/`, credentials)
    .then((response) => {
      const timeTokenExpires = new Date(
        new Date().getTime() + Number(response.data.exp) * 1000
      );
      Cookies.set("token", response.data.access, { expires: timeTokenExpires });
      Cookies.set("name", response.data.username, {
        expires: timeTokenExpires,
      });
      return response;
    })
    .catch((error) => {
      return false;
    });
};

const addImage = (credentials) => {
  return axios
    .post(`${API_URL}/image/`, credentials, {
      headers: {
        Authorization: `Bearer ${Cookies.get("token")}`,
      },
    })
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      return false;
    });
};

const addCategory = (credentials) => {
  return axios
    .post(`${API_URL}/category/`, credentials, {
      headers: {
        Authorization: `Bearer ${Cookies.get("token")}`,
      },
    })
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      return false;
    });
};

const getCategories = (page) => {
  return axios
    .get(`${API_URL}/category/?page=${page}`)
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      return false;
    });
};

const getCategory = (id) => {
  return axios
    .get(`${API_URL}/category/${id}`)
    .then( response => {
      return response.data
    })
    .catch( error => {
      return false
    })
}

const updateCategory = (credentials,id) => {
  return axios
    .put(`${API_URL}/category/${id}`, credentials, {
      headers: {
        Authorization: `Bearer ${Cookies.get("token")}`,
      },
    })
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      return false;
    });
};

const deleteCategory = id => {
  return axios
  .delete(`${API_URL}/category/${id}`,{
    headers: {
      Authorization: `Bearer ${Cookies.get("token")}`,
    },
  })
  .then( response => {
    return response.data
  })
  .catch( error => {
    return false
  })
}

export default {
  login,
  addImage,
  addCategory,
  getCategories,
  getCategory,
  updateCategory,
  deleteCategory
};
