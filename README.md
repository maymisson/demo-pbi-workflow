# Workflow de Demonstração do Power BI

## O que é isso?  

Este repositório é um exemplo de como trabalhar em colaboração com projetos Power BI usando Git e GitHub Workflow, resolvendo conflitos e construindo um projeto paralelo de exemplo.  
Ele demonstra o uso de um cenário de CI/CD para projetos Microsoft Power BI PRO utilizando [fabric-cicd](https://microsoft.github.io/fabric-cicd/latest/) e GitHub Actions.  

## Instalação  

- Faça um fork deste repositório  
- Configure os segredos do SPN no GitHub Actions secrets


|Nome|Valor|  
|---|---|  
|FABRIC_CLIENT_ID|Seu Client ID do Service Principal da App ID do Entra|  
|FABRIC_CLIENT_SECRET|Seu Secret do Service Principal da App ID do Entra|  
|FABRIC_TENANT_ID|Seu Tenant ID|  


Se executar localmente, na primeira vez instale os requisitos com:  

```bash
$ pip install -r requirements.txt  
``` 












