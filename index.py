
import http.server
import socketserver
import os
from urllib.parse import parse_qs, urlparse

# Função para gerar HTML dinamicamente com base na URL
def gerar_html_dinamico(caminho, parametros):
    # Página inicial
    if caminho == "/":
        return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Servidor de Teste Python</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f0f0f0;
        }
        .container {
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            max-width: 800px;
            margin: 0 auto;
        }
        nav {
            margin-bottom: 20px;
        }
        nav a {
            margin-right: 10px;
            text-decoration: none;
            color: #0066cc;
            padding: 5px 10px;
            border-radius: 3px;
            background-color: #e9f2ff;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Servidor de Teste Python</h1>
        <nav>
            <a href="/">Início</a>
            <a href="/contatos">Contatos</a>
            <a href="/usuario?nome=Visitante">Área do Usuário</a>
        </nav>
        <p>Este é um servidor simples de testes criado com Python.</p>
        <p>Você pode navegar pelas páginas usando os links acima.</p>
    </div>
</body>
</html>"""
    
    # Página de contatos
    elif caminho == "/contatos":
        return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contatos - Servidor de Teste</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f0f0f0;
        }
        .container {
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            max-width: 800px;
            margin: 0 auto;
        }
        nav {
            margin-bottom: 20px;
        }
        nav a {
            margin-right: 10px;
            text-decoration: none;
            color: #0066cc;
            padding: 5px 10px;
            border-radius: 3px;
            background-color: #e9f2ff;
        }
        .contato {
            border-bottom: 1px solid #ddd;
            padding: 10px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Lista de Contatos</h1>
        <nav>
            <a href="/">Início</a>
            <a href="/contatos">Contatos</a>
            <a href="/usuario?nome=Visitante">Área do Usuário</a>
        </nav>
        
        <div class="lista-contatos">
            <div class="contato">
                <h3>João Silva</h3>
                <p>Email: joao@exemplo.com</p>
            </div>
            <div class="contato">
                <h3>Maria Oliveira</h3>
                <p>Email: maria@exemplo.com</p>
            </div>
            <div class="contato">
                <h3>Carlos Santos</h3>
                <p>Email: carlos@exemplo.com</p>
            </div>
        </div>
    </div>
</body>
</html>"""
    
    # Página de usuário com parâmetro dinâmico
    elif caminho == "/usuario":
        nome = parametros.get('nome', ['Visitante'])[0]
        return f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Área do Usuário - Servidor de Teste</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f0f0f0;
        }}
        .container {{
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            max-width: 800px;
            margin: 0 auto;
        }}
        nav {{
            margin-bottom: 20px;
        }}
        nav a {{
            margin-right: 10px;
            text-decoration: none;
            color: #0066cc;
            padding: 5px 10px;
            border-radius: 3px;
            background-color: #e9f2ff;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Bem-vindo, {nome}!</h1>
        <nav>
            <a href="/">Início</a>
            <a href="/contatos">Contatos</a>
            <a href="/usuario?nome=Visitante">Área do Usuário</a>
        </nav>
        <p>Esta é sua área pessoal na aplicação de teste.</p>
        <p>Você pode mudar o nome na URL para ver uma saudação diferente.</p>
    </div>
</body>
</html>"""
    
    # Página não encontrada
    else:
        return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página não encontrada</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f0f0f0;
        }
        .container {
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            max-width: 800px;
            margin: 0 auto;
            text-align: center;
        }
        .erro {
            color: #cc0000;
            font-size: 72px;
            margin: 0;
        }
        a {
            display: inline-block;
            margin-top: 20px;
            color: #0066cc;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="erro">404</h1>
        <h2>Página não encontrada</h2>
        <p>A página que você está procurando não existe.</p>
        <a href="/">Voltar para a página inicial</a>
    </div>
</body>
</html>"""

# Cria um handler personalizado para o servidor HTTP
class MeuHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Analisa a URL para extrair o caminho e os parâmetros
        url_parts = urlparse(self.path)
        caminho = url_parts.path
        parametros = parse_qs(url_parts.query)
        
        # Verifica se o caminho corresponde a um arquivo existente
        if os.path.exists('.' + caminho) and not os.path.isdir('.' + caminho):
            # Se o arquivo existe, serve-o normalmente
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
        
        # Gera conteúdo HTML dinâmico com base no caminho
        conteudo = gerar_html_dinamico(caminho, parametros)
        
        # Envia resposta HTTP
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(conteudo.encode('utf-8'))

# Configuração do servidor
PORT = 8000
Handler = MeuHandler

# Inicia o servidor
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor rodando na porta {PORT}")
    print(f"Acesse http://localhost:{PORT}/ no seu navegador")
    print("Pressione Ctrl+C para encerrar o servidor")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor encerrado.")
