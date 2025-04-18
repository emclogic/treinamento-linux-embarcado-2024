# Docker para Sistemas Embarcados

Execução de script python em container.

Na aula 2 foi criada uma aplicação web para controlar GPIO, o arquivo app.py está em web-gpio e deverá ser encapsulado num container.

## Construcao

O container deverá ser construido com a linha de comando abaixo:

```bash
docker build --no-cache --build-arg "HOST_UID=$(id -u)" --build-arg "HOST_GID=$(id -g)" --rm -f "Dockerfile" -t web-container .
```

## Execucao

O comando abaixo vai criar o container com os parametros para executar o container com os privilegios necessarios para acessar os GPIOs da placa.

```bash
docker run -d --name web-container --privileged --device /dev/gpiomem -p 5000:5000 web-container
```

Para verificar se o container esta em execucao digite o comando:

```bash
docker ps
```

Para verificar os logs, digite:

```bash
docker logs -f web-container
```

Se precisar acessar o container interativamente, use:

```bash
docker exec -it web-container bash
```

## Finalizacao

Apos execucao dos testes o container devera ser interrompido com:

```bash
docker stop web-container
```

Para excuir o container criado:

```bash
docker container rm web-container
```

E, por fim, para excluir a imagem:

```bash
docker image rm web-container:latest
```
