def verificar_usuario(usuario, senha, usuarios):
    """Verifica se o usuário e senha são válidos."""
    return usuarios.get(usuario) == senha

def gerar_log_autenticacao(usuario, ip_usuario, sucesso):
    """Simula a geração de log de autenticação."""
    from datetime import datetime
    from logs import gravar_log
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    resultado = "sucesso" if sucesso else "falha"
    
    log = f"{timestamp} - {usuario} - IP: {ip_usuario} - {resultado}"
    gravar_log(log)
