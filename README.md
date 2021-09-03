# Github actions - Hello World

Esse repositório é apenas um teste de utilização da ferramenta de automação do
github.

Basicamente, a imagem da aplicação `Dockerfile` vai ser atualizada no docker hub
quando as alterações propostas nas outras branches forem adicionadas na branch
`main` de forma similar todas as outras branches terão uma imagem publicada no
docker hub, entretanto terão como flag de versão o *short hash* do commit que
gerou a execução da pipeline.

## 📦 Aplicação

A aplicação é feita a partir do framework Flask, proporcionando apenas uma rota.

| rota | descrição                                       |
| --   | --                                              |
| `/`  | Retorna o hostname de onde está sendo executada |

## 🏗 Infraestrutura

Está sendo provisionada em containers. Sua image pode ser encontrada no docker
hub, e baixada a partir do seguinte commando.

```
docker pull josecarlosnf/flask-hostname
```

Com isso a última versão estável será utilizada.

Além disso, há também um `docker-compose.yml` que a proporciona a possibilidade
de ser altamente escalável. Podendo ter diversas intâncias que serão acessiveis
por meio de um balanceador de carga, configurado a partir de um nginx.

## 🏃 Como rodar - configuração para alta disponibilidade

Para "orquestrar" os containers o docker-compose pode ser utilizado da seguinte
maneira.

```
docker-compose up -d
```

Dessa forma, uma instância do serviço da aplicação (app) e uma instância do
nginx, atuando como balanceador de carga (load_balancer), serão criadas.

Para visualizar os serviços rodando.
```
docker-compose ps
```

Para acessar os serviços basta acessar <http://localhost>. Note que se a página
for atualizada várias vezes nada mudará.

### 🔝 Escalando o serviço da aplicação

Para aumentar a quantidade de instâncias da aplicação podemos utilizar a
seguinte comando:

```
docker-compose scale app=5
```

Assim teremos 5 instâncias da aplicação rodando.

Agora, ao atualizar a página, note que o nome do hostname mudará. Visto que o
tráfego está sendo balanceado entre as instâncias de aplicação.

## 🛑 Como parar tudo

```
docker-compose down
```
