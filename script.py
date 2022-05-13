import requests

BASE_URL = "https://sigaa.ufpi.br/sigaa"

USERNAME = ""
PASSWORD = ""

#Primeiro acesso para criar sessão

response = requests.get(f"{BASE_URL}/verTelaLogin.do")

session_id = response.cookies.get_dict().get("JSESSIONID")
print("JSESSIONID: ", session_id)


# Registra a sessão com login no sistema!

response = requests.post(
  f"{BASE_URL}/logar.do",
  params = {
    "dispatch": "logOn"
  },
  cookies = {
    "JSESSIONID": session_id,
  },
  data = {
    "user.login": USERNAME,
    "user.senha": PASSWORD,
  }
)

# Utiliza a sessão criada!

response = requests.get(
  f"{BASE_URL}/ufpi/portais/discente/discente.jsf", cookies = {
    "JSESSIONID": session_id
  }
)

if response.status_code == 200:
    print(response.url)
    print(response.text)