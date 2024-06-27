# eEDB-016/2024-2 - Projeto de Conclusão de Disciplina

## Criar tabelas DynamoDB

Para criar as tabelas DynamoDB basta importar o arquivo `cloudformation.yaml` na aba "Stacks" no recurso de CloudFormation no Console da AWS.

Tabelas DynamoDB:
- Carrinho
- ListaDesejo
- Recomendacao
- Pedido
- Cliente
- Produto

## Inserir dados nas tabelas DynamoDB

Para inserir os dados nas tabelas é necessário executar o script Python `insert_dynamodb.py` passando o argumento -t ou --table para definir  o nome da tabela e o argumento -f ou --file para especificar o caminho do arquivo JSON que contém uma lista de objetos a serem inseridos nas tabelas DynamoDB. Os arquivos de inserção encontram-se na pasta `dados/`.

Exemplo: 
> $ python insert_dynamodb.py --table Cliente --file dados/Cliente.json