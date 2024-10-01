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
