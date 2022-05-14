require("dotenv").config();
const axios = require("axios");

async function auth() {
  const client = axios.create({
    baseURL: "https://sigaa.ufpi.br/sigaa",
  });

  const response = await client.get("verTelaLogin.do");

  const [cookie] = response.headers["set-cookie"];

  client.defaults.headers.Cookie = cookie;

  const payload = new URLSearchParams({
    "user.login": process.env.USERNAME,
    "user.senha": process.env.PASSWORD,
  });

  await client.post("logar.do", payload, {
    params: {
      dispatch: "logOn",
    },
  });

  return client;
}

auth().then();
