# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import os
import sys
import requests
import traceback

# Add the libs folder to the system path
base_path = tmp_global_obj["basepath"] #type:ignore
cyberark_directory_path = os.path.join(base_path, "modules", "Cyberark")
cyberark_libs_path = os.path.join(cyberark_directory_path, "libs") 

if cyberark_libs_path not in sys.path:
    sys.path.append(cyberark_libs_path)
    

class Cyberark_Auth:

    def __init__(self, url, username, password, verify_ssl=True):
        self.username = username
        self.password = password
        self.cyberark_url = url
        self.cert = None
        self.verify_ssl = verify_ssl
        self.getCert()

    def getCert(self):
        logon_url = "%s/PasswordVault/API/auth/LDAP/Logon/" % (
            self.cyberark_url
        )
        credentials = {"username": self.username, "password": self.password}
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.cert
        }
        r = requests.post(
            logon_url,
            json=credentials,
            headers=headers,
            verify=self.verify_ssl
        )
        j = r.json()
        self.cert = j["CyberArkLogonResult"]
        
    
    def getAllSafes(self, search=None, limit=25):
        get_all_safes_url = "%s/PasswordVault/API/Safes" % (
            self.cyberark_url
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.cert
        }
        
        params = {}
        if search:
            params["search"] = search
        if limit:
            params["limit"] = limit
            
        r = requests.get(
            get_all_safes_url,
            headers=headers,
            params=params,
            verify=self.verify_ssl
        )
        return r.json()
    
    
    def getSafe(self, safe_url_id):
        get_safe_url = "%s/PasswordVault/API/Safes/%s" % (
            self.cyberark_url,
            safe_url_id
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.cert
        }
        r = requests.get(
            get_safe_url,
            headers=headers,
            verify=self.verify_ssl
        )
        return r.json()
    
    
    def addSafe(self, safe_name, safe_description, safe_location):
        add_safe_url = "%s/PasswordVault/API/Safes" % (
            self.cyberark_url
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.cert
        }
        safe = {
            "safeName": safe_name,
            "description": safe_description,
            "location": safe_location
        }
        r = requests.post(
            add_safe_url,
            json=safe,
            headers=headers,
            verify=self.verify_ssl
        )
        return r.status_code

        
    def updateSafe(self, safe_url_id, safe_name=None, safe_description=None, safe_location=None):
        update_safe_url = "%s/PasswordVault/API/Safes/%s" % (
            self.cyberark_url,
            safe_url_id
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.cert
        }
        
        safe = {}
        
        if safe_name:
            safe["safeName"] = safe_name

        if safe_description:
            safe["description"] = safe_description

        if safe_location:
            safe["location"] = safe_location

        r = requests.put(
            update_safe_url,
            json=safe,
            headers=headers,
            verify=self.verify_ssl
        )
        return r.status_code
    
    
    def deleteSafe(self, safe_url_id):
        delete_safe_url = "%s/PasswordVault/API/Safes/%s" % (
            self.cyberark_url,
            safe_url_id
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.cert
        }
        r = requests.delete(
            delete_safe_url,
            headers=headers,
            verify=self.verify_ssl
        )
        return r.status_code
    
    def getAllAccounts(self, search=None, limit=25):
        parameters = ""
        if search:
            parameters += "?search=%s" % search
            parameters += "&limit=%s" % limit
        else:
            parameters += "?limit=%s" % limit

        get_accounts_url = "%s/PasswordVault/API/Accounts/%s" % (
            self.cyberark_url,
            parameters
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.cert
        }

        r = requests.get(
            get_accounts_url,
            headers=headers,
            verify=self.verify_ssl
        )
        return r.json()
    
    def getAccount(self, account_id):
        get_account_url = "%s/PasswordVault/API/Accounts/%s" % (
            self.cyberark_url,
            account_id
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.cert
        }
        r = requests.get(
            get_account_url,
            headers=headers,
            verify=self.verify_ssl
        )
        return r.json()
    
    def addAccount(self, name, platform_id, safe, secret_type, secret):
        add_account_url = "%s/PasswordVault/API/Accounts" % (
            self.cyberark_url
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.cert
        }
        account = {
            "name": name,
            "platformId": platform_id,
            "safeName": safe,
            "secretType": secret_type,
            "secret": secret
        }
        r = requests.post(
            add_account_url,
            json=account,
            headers=headers,
            verify=self.verify_ssl
        )
        return r.status_code
    
    def deleteAccount(self, account_id):
        delete_account_url = "%s/PasswordVault/API/Accounts/%s" % (
            self.cyberark_url,
            account_id
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.cert
        }
        r = requests.delete(
            delete_account_url,
            headers=headers,
            verify=self.verify_ssl
        )
        return r.status_code

    def generatePassword(self, account_id):
        generate_password_url = "%s/PasswordVault/API/Accounts/%s/GeneratePassword" % (
            self.cyberark_url,
            account_id
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.cert
        }
        r = requests.post(
            generate_password_url,
            headers=headers,
            verify=self.verify_ssl
        )
        return r.json()
    
    def getPassword(self, account_id):
        get_password_url = "%s/PasswordVault/API/Accounts/%s/Password" % (
            self.cyberark_url,
            account_id
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.cert
        }
        r = requests.get(
            get_password_url,
            headers=headers,
            verify=self.verify_ssl
        )
        return r.json()
    
    # # def getPassword(self, account_id):
    # #     url = "%s/PasswordVault/API/Accounts/%s/Password/Retrieve/" % (
    # #         self.cyberark_url,
    # #         account_id
    # #     )
    # #     headers = {
    # #         "Content-Type": "application/json",
    # #         "Authorization": self.cert
    # #     }
    # #     r = requests.get(url, headers=headers, verify=self.verify_ssl)
    # #     return r.text
    
    # # def generatePassword(self, account_id):
    # #     url = "%s/PasswordVault/API/Accounts/%s/Password/Generate" % (
    # #         self.cyberark_url,
    # #         account_id
    # #     )
    # #     headers = {
    # #         "Content-Type": "application/json",
    # #         "Authorization": self.cert
    # #     }
    # #     r = requests.post(url, headers=headers, verify=self.verify_ssl)
    # #     return r.text

    
module = GetParams("module")

try:
    if module == "config":
        url = GetParams("url")
        username = GetParams("username")
        password = GetParams("password")
        result = GetParams("result")
        
        try:
            cyberark = Cyberark_Auth(
                url=url,
                username=username,
                password=password,
            )

            SetVar(result, True)
            print("Configuracion exitosa")
        except Exception as e:
            PrintException()
            SetVar(result, False)
            raise e
        
    if module == "get_all_safes":
        search = GetParams("search")
        limit = GetParams("limit")
        result = GetParams("result")
        
        try:
            cyberark = Cyberark_Auth(
                url=url,
                username=username,
                password=password,
            )
            safes = cyberark.getAllSafes(search, int(limit))
            SetVar(result, safes)
            print("Safes obtenidos")
        except Exception as e:
            PrintException()
            SetVar(result, False)
            raise e

    if module == "get_safe":
        safe_url_id = GetParams("safe_url_id")
        result = GetParams("result")
        
        try:            
            safe = cyberark.getSafe(
                safe_url_id=safe_url_id
            )
            SetVar(result, safe)
            print("Safe obtenido")
        except Exception as e:
            PrintException()
            SetVar(result, False)
            raise e

    if module == "add_safe":
        safe_name = GetParams("safe_name")
        safe_description = GetParams("safe_description")
        safe_location = GetParams("safe_location")
        result = GetParams("result")
        
        try:
            status_code = cyberark.addSafe(
                safe_name=safe_name,
                safe_description=safe_description,
                safe_location=safe_location
            )

            SetVar(result, status_code)
            print("Safe creado exitosamente")
        except Exception as e:
            PrintException()
            SetVar(result, False)
            raise e
    
    if module == "update_safe":
        safe_url_id = GetParams("safe_url_id")
        safe_name = GetParams("safe_name")
        safe_description = GetParams("safe_description")
        safe_location = GetParams("safe_location")
        result = GetParams("result")
        
        try:
            status_code = cyberark.updateSafe(
                safe_url_id=safe_url_id,
                safe_name=safe_name,
                safe_description=safe_description,
                safe_location=safe_location
            )

            SetVar(result, status_code)
            print("Safe actualizado exitosamente")
        except Exception as e:
            PrintException()
            SetVar(result, False)
            raise e
        
    if module == "delete_safe":
        safe_url_id = GetParams("safe_url_id")
        result = GetParams("result")
        
        try:
            status_code = cyberark.deleteSafe(
                safe_url_id=safe_url_id
            )
            SetVar(result, status_code)
            print("Safe eliminado exitosamente")
        except Exception as e:
            PrintException()
            SetVar(result, False)
            raise e
        
    if module == "get_all_accounts":
        search = GetParams("search")
        limit = GetParams("limit")
        result = GetParams("result")
        
        try:
            accounts = cyberark.getAllAccounts(
                search=search, 
                limit=int(limit)
            )
            SetVar(result, accounts)
            print("Cuentas obtenidas")
        except Exception as e:
            PrintException()
            SetVar(result, False)
            raise e
    
    if module == "get_account":
        account_id = GetParams("account_id")
        result = GetParams("result")
        
        try:
            account = cyberark.getAccount(
                account_id=account_id
            )
            SetVar(result, account)
            print("Cuenta obtenida")
        except Exception as e:
            PrintException()
            SetVar(result, False)
            raise e

    if module == "add_account":
        name = GetParams("name")
        platform_id = GetParams("platform_id")
        safe = GetParams("safe")
        secret_type = GetParams("secret_type")
        secret = GetParams("secret")
        result = GetParams("result")
        
        try:
            status_code = cyberark.addAccount(
                name=name,
                platform_id=platform_id,
                safe=safe,
                secret_type=secret_type,
                secret=secret
            )
            SetVar(result, status_code)
            print("Cuenta creada exitosamente")
        except Exception as e:
            PrintException()
            SetVar(result, False)
            raise e
    
    if module == "delete_account":
        account_id = GetParams("account_id")
        result = GetParams("result")
        
        try:
            status_code = cyberark.deleteAccount(
                account_id=account_id
            )
            SetVar(result, status_code)
            print("Cuenta eliminada exitosamente")
        except Exception as e:
            PrintException()
            SetVar(result, False)
            raise e
        
    if module == "generate_password":
        account_id = GetParams("account_id")
        result = GetParams("result")
        
        try:
            password = cyberark.generatePassword(
                account_id=account_id
            )
            SetVar(result, password)
            print("Password generada")
        except Exception as e:
            PrintException()
            raise e
        
    if module == "get_password":
        account_id = GetParams("account_id")
        result = GetParams("result")
        
        try:
            password = cyberark.getPassword(
                account_id=account_id
            )
            SetVar(result, password)
            print("Password obtenida")
        except Exception as e:
            PrintException()
            raise e
    
    # # if module == "get_password":
    # #     account_id = GetParams("account_id")
    # #     result = GetParams("result")
        
    # #     try:
    # #         password = cyberark.getPassword(account_id)
    # #         SetVar(result, password)
    # #         print("Password obtenida")
    # #     except Exception as e:
    # #         PrintException()
    # #         raise e

    
    # if module == "get_password":
    #     safe = GetParams("safe")
    #     keyword = GetParams("keyword")
    #     result = GetParams("result")
        
    #     try:
    #         account_id = cyberark.getAccountIDs(safe, keyword)[0]
    #         password = cyberark.getPassword(account_id)
    #         SetVar(result, password)
    #         print("Password: %s" % password)
    #     except Exception as e:
    #         PrintException()
    #         SetVar(result, False)
    #         raise e
    
    # if module == "add_password":
    #     safe = GetParams("safe_name")
    #     account = GetParams("account")
    #     platform = GetParams("platform")
    #     address = GetParams("address")
    #     result = GetParams("result")
        
    #     try:
    #         cyberark.addPassword(safe, account, platform, address)
    #         SetVar(result, True)
    #         print("Password agregado")
    #     except Exception as e:
    #         PrintException()
    #         SetVar(result, False)
    #         raise e

except Exception as e:
    traceback.print_exc()
    PrintException()
    raise e