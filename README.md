# Workflow de Demonstração do Power BI

## O que é isso?  

Este repositório é um exemplo de como trabalhar em colaboração com projetos Power BI usando Git e GitHub Workflow, resolvendo conflitos e construindo um projeto paralelo de exemplo.  
Ele demonstra o uso de um cenário de CI/CD para projetos Microsoft Power BI PRO utilizando [fabric-cli](https://aka.ms/fabric-cli) e GitHub Actions.  

## Instalação  

- Faça um fork deste repositório  
- Crie uma cópia de `.env.example` e renomeie para `.env` preenchendo com os segredos do SPN  
- Configure os mesmos segredos do SPN no GitHub Actions se desejar usar CD  


|Nome|Valor|  
|---|---|  
|FABRIC_CLIENT_ID|Seu Client ID do Service Principal da App ID do Entra|  
|FABRIC_CLIENT_SECRET|Seu Secret do Service Principal da App ID do Entra|  
|FABRIC_TENANT_ID|Seu Tenant ID|  


Se executar localmente, na primeira vez instale os requisitos com:  

```bash
$ pip install -r requirements.txt  
```

- Configure o arquivo `config.json` com os IDs por branch.  
  - Os adminUPNs são o Object ID do Entra User Principal Name.  


## Pipeline de CI/CD  

- Os projetos Power BI são salvos na pasta `src` com as extensões `*.Report` e `*.SemanticModel`.  
- Novas versões são implantadas na branch `dev`.  
- A cada Pull Request para `develop`, o pipeline do GitHub Actions chamado `.github\workflows\bpa.yml` é acionado, executando a análise de melhores práticas. Este processo utiliza ferramentas da comunidade como [Tabular Editor](https://github.com/TabularEditor/) e [PBI-Inspector](https://github.com/NatVanG/PBI-InspectorV2). Se aprovado e mesclado, o pipeline `.github\workflows\deploy.yml` implantará no workspace `*-DEV` com o nome e fonte de dados especificados no `config.json`.  
- Uma vez aprovado o projeto, é criado um pull request para a branch `main`, onde o pipeline implantará a versão no workspace `*-PRD` seguindo o mesmo `config.json`.  












