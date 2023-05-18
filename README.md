# Documentação do Conversor de Imagens JPEG para PNG

Este código é um conversor de imagens que utiliza a biblioteca `PIL` (Python Imaging Library) para converter todas as imagens JPEG presentes no diretório atual em imagens PNG.

## Requisitos

Você precisará da seguinte biblioteca para executar este código:

- PIL (Python Imaging Library)

Para instalar a biblioteca necessária, execute o seguinte comando:

```sh
pip install Pillow
```

## Como usar

O código é um script que, quando executado, verifica o diretório atual em busca de arquivos com a extensão `.jpeg`. Para cada arquivo JPEG encontrado, ele converte o arquivo para o formato PNG e salva na pasta `Convertidas`, que é criada no diretório atual, caso não exista.

Os arquivos JPEG originais são removidos após a conversão.

## Estrutura do código

O código é um script simples que não possui funções ou classes. Ele realiza as seguintes ações:

1. Lista todos os arquivos no diretório atual usando `os.listdir()`.
2. Tenta criar a pasta `Convertidas`. Se a pasta já existir, o código continua sem interrupção.
3. Itera sobre a lista de arquivos.
   - Se o arquivo for uma imagem JPEG, abre a imagem com a classe `Image` da biblioteca PIL, salva a imagem convertida em PNG na pasta `Convertidas` e remove o arquivo JPEG original.
   - Se o arquivo não for uma imagem JPEG, informa que não foi possível converter o arquivo.

## Exemplo de uso

Para usar o conversor, siga estas etapas:

1. Salve o código em um arquivo chamado, por exemplo, `conversor.py`.
2. Coloque todos os arquivos JPEG que deseja converter no mesmo diretório que o arquivo `conversor.py`.
3. Execute o script `conversor.py`:

```sh
python conversor.py
```

A pasta `Convertidas` será criada no diretório atual (caso ainda não exista) e todas as imagens JPEG serão convertidas para PNG e salvas nessa pasta. Os arquivos JPEG originais serão removidos.
