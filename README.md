# python-api
Criação de API básica com Flask para estudo de Python.  

## Versões
Sobre as versões 2 e 3 do Python: https://python.org.br/qual-python/  

## Bibliotecas utilizadas
- Flask: **pip3 install flask**  
- Resquests: **pip3 install requests**  

## Execução
1- No terminal acessa o diretório do projeto  
2- Utiliza o comando **python3 routes.py**  

## Fazendo requisições
Utilizar qualquer aplicativo para testar as requisições: Insomnia ou Postman, por exemplo  
- Rota GET:  
URL: http://localhost:5000/olamundo  
  
- Rota POST:  
URL: http://localhost:5000/cadastra/usuario  
Json: {  
	    "nome": "Teste",  
	    "email": "teste@teste.com.br",  
	    "senha": "123"  
      }  



