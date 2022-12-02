# Cyberark
  
Módulo para conectar à Cyberark e gerenciar senhas   

*Read this in other languages: [English](Manual_Cyberark.md), [Portugues](Manual_Cyberark.pr.md), [Español](Manual_Cyberark.es.md).*
  
![banner](imgs/Banner_Cyberark.png)
## Como instalar este módulo
  
__Baixe__ e __instale__ o conteúdo na pasta 'modules' no caminho do Rocketbot  



## Descrição do comando

### Configurar credenciais Cyberark
  
Configure credenciais para conectar com o API do Cyberark.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Usuário|Usuário para conectar com o API do Cyberark|Usuário|
|Senha|Senha para conectar com o API do Cyberark|********|
|URL|URL do API do Cyberark|https://cyberark.example.com|
|Atribuir resultado a variável|Atribuir resultado da conexão a variável|result|

### Obter todas as Cofres
  
Obter todos os Cofres do Vault do CyberArk
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Filtrar por nome|Filtra o resultado pelo nome do Cofre|nome|
|Quantidade de resultados|Quantidade máxima de resultados que serão retornados na variável|25|
|Atribuir resultado a variável|Atribuir resultado a variável|result|

### Obter Cofre
  
Obter informações sobre um Cofre específico no Vault.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do Cofre|URL ID do Cofre|123456|
|Atribuir resultado a variável|Atribuir resultado a variável|result|

### Adicionar Cofre
  
Adiciona um novo Cofre ao Vault. O usuário deve ter permissões para adicionar Cofres no Vault.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome do Cofre|Nome do novo Cofre|COFRE-1|
|Descrição do Cofre|Descrição do novo Cofre|Cofre de teste|
|Localização do Cofre|Localização do novo Cofre. Por padrão é a raiz.|//|
|Atribuir resultado a variável|Atribuir resultado a variável|result|

### Atualizar Cofre
  
Atualiza um único Cofre no Vault do CyberArk
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do Cofre|ID do Cofre para atualizar|123456|
|Novo nome do Cofre|Novo nome que será atribuído ao Cofre|NOVO-NOME|
|Nova descrição do Cofre|Nova descrição que será atribuída ao Cofre|NOVA-DESCRIÇÃO|
|Nova localização do Cofre|Nova localização que será atribuída ao Cofre|//|
|Atribuir resultado a variável|Atribuir resultado a variável|result|

### Excluir Safe
  
Excluir Safe do Vault
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do Cofre|URL ID do Cofre|123456|
|Atribuir resultado a variável|Atribuir resultado a variável|result|

### Obter todas as contas
  
Obter uma lista de todas as contas no Vault
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Filtrar por nome|Filtra o resultado pelo nome da conta|nome|
|Quantidade de resultados|Quantidade máxima de resultados que serão retornados na variável|25|
|Atribuir resultado a variável|Atribuir resultado a variável|result|

### Obter conta
  
Obter informações sobre uma conta identificada por seu ID
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da conta|ID da conta|123456|
|Atribuir resultado a variável|Atribuir resultado a variável|result|

### Adicionar Conta
  
Adiciona uma nova conta privilegiada ou chave SSH ao Vault
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome da conta|Nome que terá a conta criada|Nome|
|PlatformId|Identificador da plataforma atribuída à conta|WinServerLocal|
|Nome do cofre|Nome do cofre onde a conta será localizada|COFRE-1|
|Secret type|Tipo de segredo que será armazenado na conta|key|
|Secret|Segredo que será armazenado na conta|********|
|Atribuir resultado a variável|Atribuir resultado a variável|result|

### Excluir conta
  
Excluir uma conta do Vault
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da conta|ID da conta que será excluída|123456|
|Atribuir resultado a variável|Atribuir resultado a variável|result|

### Gerar senha
  
Gera uma nova senha para uma conta existente. A senha é gerada de acordo com a política de senhas definida no sistema de destino.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da conta|ID da conta que será excluída|123456|
|Atribuir resultado a variável|Atribuir resultado a variável|result|

### Obter o valor da senha
  
Recupere a senha ou a chave SSH de uma conta existente identificada pelo ID da conta.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da conta|ID da conta que será excluída|123456|
|Atribuir resultado a variável|Atribuir resultado a variável|result|

### Obter senha do Central Credential Provider
  
Permite que aplicativos recuperem segredos do Central Credential Provider
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|URL|URL do Central Credential Provider|100.10.2|
|Porta|Porta do servidor|22|
|AppID|Especifica o ID único do aplicativo que emite a solicitação de senha.|BillingApp|
|Nome do Safe|Especifica o nome do Safe onde a senha é armazenada.|SAFE-NAME|
|Pasta|Especifica a pasta onde a senha é armazenada.|BILLING|
|Objeto|Especifica o nome do objeto senha a recuperar.|MonthlyBilling|
|Nome de Usuário|Define critérios de pesquisa de acordo com a propriedade de conta de nome de usuário atribuída.|user|
|Atribuir resultado a variável|Atribuir resultado a variável|result|
