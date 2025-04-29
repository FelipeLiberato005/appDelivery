def gravar_log(mensagem):
    """Grava a mensagem de log no arquivo 'auth_logs.txt'."""
    with open("auth_logs.txt", "a") as f:
        f.write(mensagem + "\n")
