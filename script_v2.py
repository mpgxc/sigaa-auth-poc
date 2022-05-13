from requests import  Session

session = Session()

ENTITY_DOMAIN = 'ufpi'
BASE_URL = f"https://sigaa.{ENTITY_DOMAIN}.br/sigaa"
USERNAME = '<username>'
PASSWORD = '<password>'

# Cria Sessão
session.get(f"{BASE_URL}/verTelaLogin.do", allow_redirects=True, verify=True)

# Realiza Login
response_auth = session.post(
  f"{BASE_URL}/logar.do",
  params = {
    "dispatch": "logOn"
  },
  data = {
    "user.login": USERNAME,
    "user.senha": PASSWORD,
  }
)

if response_auth.status_code == 200:
  print(response_auth.url)

# Realiza requisição com sessão logada
response_discente = session.get(f"{BASE_URL}/ufpi/portais/discente/discente.jsf")

if response_discente.status_code == 200:
    print(response_discente.url)
    print(response_discente.text)