# eEDB-016-2024-2

# criar tabelas DynamoDB

para criar as tabelas DynamoDB basta importar o arquivo `cloudformation.yaml` na aba de CloudFormation no Console da AWS

# inserir dados nas tabelas DynamoDB

para inserir os dados nas tabelas é necessário executar o script Python `insert_dynamodb.py` passando o argumento -t ou --table para definir  o nome da tabela e o argumento -f ou --file para especificar o caminho do arquivo JSON que contém uma lista de objetos a serem inseridos nas tabelas DynamoDB

Exemplo: 
> $ python insert_dynamodb.py --table Cliente --file dados/Cliente.json