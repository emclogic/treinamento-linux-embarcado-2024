# Treinamento Linux Embarcado 2024

Repositório com exercícios referentes ao curso [Aprendendo Linux Embarcado na Prática com Raspberry Pi](https://cursos.embarcados.com.br/cursos/aprendendo-linux-embarcado-na-pratica-co/)

## Preparacao do ambiente do target

Existem um playbook ansible para instalar as dependencias dos projetos no raspberry pi zero 2w (também foi testado num raspberry pi zero).

Para executar o playbook é preciso instalar o ansible no raspberry pi.

```bash
apt install -y ansible
```

Execute este playbook no target para instalacao dos pacotes (binarios, bibliotecas) necessarios.

```bash
ansible-playbook playbook-target.yml
```

Desde a versão Bookworm, os usuarios nao devem instalar diretamente as bibliotecas do python diretamente no sistema.

Ao inves disso, utilize um ambiente virtual (venv), para instalar uma biblioteca a nivel de sistema, para todos os usuarios, instale utilizand apt.

A vantagem de se utilizar ambientes virtuais e que (caso necessario) voce pode utilizar versoes diferentes das bibliotecas para cada projeto.

O playbook cria o ambiente virtual em $HOME/.venv, para ativa-lo utilize o comando:

```bash
source ~/.venv/bin/activate
```

O prompt do shell ficara parecido com isso:

```bash
(.venv) $
```

Quando finalizar o trabalho no projeto, execute o seguinte comando a partir de qualquer diretorio para finalizar a execucao em ambiente virtual.

```bash
deactivate
```
