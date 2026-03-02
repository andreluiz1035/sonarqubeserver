#DB_PASSWORD = "SuperSecret123!"  # hardcoded credential (vulnerabilidade)

def conectar():
    print("Conectando com senha:", DB_PASSWORD)


username = os.getenv("username") # Compliant
password = os.getenv("password") # Compliant
usernamePassword = 'user=%s&password=%s' % (username, password) # Compliant{code}