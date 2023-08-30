# Use a base image oficial do Python
FROM python:3.8

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie os arquivos do projeto para o diretório de trabalho
COPY . /app

# Comando para executar quando o contêiner iniciar
CMD ["python", "-m", "main"]
