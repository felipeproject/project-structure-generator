# Project Structure Generator

Este projeto foi criado para gerar rapidamente estruturas de projetos utilizando um arquivo JSON. A ideia surgiu a partir da necessidade de criar grandes estruturas de projetos de forma mais ágil e eficiente, utilizando a inteligência artificial (como o ChatGPT) para gerar o formato JSON com a organização necessária. Assim, ao invés de criar manualmente as pastas e arquivos, o formato JSON é gerado e o script executa todo o processo automaticamente.

## Funcionalidade

O script `create_project_structure.py` lê um arquivo JSON com a estrutura do projeto e cria pastas e arquivos no diretório de destino, conforme descrito no JSON. Isso permite a criação de projetos de forma rápida e simples.

### Exemplo de Estrutura do JSON

O arquivo `project_structure.json` deve seguir o formato abaixo:

```json
{
  "name": "nome_do_projeto",
  "project": {
    "pasta_1": {
      "arquivo_1.txt": "Conteúdo do arquivo 1",
      "arquivo_2.txt": "Conteúdo do arquivo 2"
    },
    "pasta_2": {
      "arquivo_3.txt": "Conteúdo do arquivo 3"
    }
  }
}
