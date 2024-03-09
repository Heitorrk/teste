# Consumo de uma API
Bem-vindo à API do universo Demon Slayer, uma plataforma que fornece informações sobre personagens, técnicas e citações da série de anime e mangá Demon Slayer (Kimetsu no Yaiba).

# Como instalar :card_file_box:
Para começar, você precisará clonar este repositório:
git clone https://github.com/seu-usuario/demon-slayer-api.git
Em seguida, instale as dependências necessárias:
pip install -r requirements.txt

# Como usar :pencil:
Inicie o servidor da API:
python manage.py runserver
Acesse a API em http://localhost:8000/ para obter uma lista de endpoints disponíveis.
Utilize os endpoints para obter informações sobre personagens, técnicas e citações.
Exemplo de endpoint para obter informações sobre um personagem:
ex.:
http://localhost:8000/api/Demon/{id}
o 'id' na url é indicado na lista de um personagem específico, sendo gerado na ordem em que foram adicionados.