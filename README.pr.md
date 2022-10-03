# Cyberark
  
Módulo para conectar à Cyberark e gerenciar senhas

*Read this in other languages: [English](README.md), [Portugues](README.pr.md), [Español](README.es.md).*

## Como instalar este módulo
  
__Baixe__ e __instale__ o conteúdo na pasta 'modules' no caminho do Rocketbot  



## Overview


1. Configurar credenciais Cyberark  
Configure credenciais para conectar com o API do Cyberark.

2. Obter todas as Cofres  
Obter todos os Cofres do Vault do CyberArk

3. Obter Cofre  
Obter informações sobre um Cofre específico no Vault.

4. Adicionar Cofre  
Adiciona um novo Cofre ao Vault. O usuário deve ter permissões para adicionar Cofres no Vault.

5. Atualizar Cofre  
Atualiza um único Cofre no Vault do CyberArk

6. Excluir Safe  
Excluir Safe do Vault

7. Obter todas as contas  
Obter uma lista de todas as contas no Vault

8. Obter conta  
Obter informações sobre uma conta identificada por seu ID

9. Adicionar Conta  
Adiciona uma nova conta privilegiada ou chave SSH ao Vault

10. Excluir conta  
Excluir uma conta do Vault

11. Gerar senha  
Gera uma nova senha para uma conta existente. A senha é gerada de acordo com a política de senhas definida no sistema de destino.

12. Obter o valor da senha  
Recupere a senha ou a chave SSH de uma conta existente identificada pelo ID da conta.  




----
### OS

- windows
- mac
- linux
- docker

### Dependencies
- [**python-requests**](https://pypi.org/project/python-requests/)
### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)