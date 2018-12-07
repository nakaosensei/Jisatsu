import json
import Plant as plantManager

class FloraDecoder:

    def decodeRequestAndWriteToDb(self,requestJson):
        estado = requestJson["statusQualificador"]
        if "Sinônimo" in estado or "sinônimo" in estado or "Sinonimo" in estado or "sinonimo" in estado:
            if('ehSinonimo' in requestJson.keys()):
                result = self.parseSinonimoSource(requestJson["ehSinonimo"])
                return result
            else:
                return 0
        if len(estado)==0:
            return 0
        if "Nome correto" in estado:
            estado = "nome correto"
        elif "Nome aceito" in estado:
            estado = "nome aceito"
        elif "Variante ortográfica" in estado:
            estado = "variante ortografica"
        elif "Nome mal aplicado" in estado:
            estado = "nome mal aplicado"
        if "endemismo" in requestJson.keys():
            endemismo = requestJson["endemismo"]
        else:
            endemismo = ""
        if 'formaVida' in requestJson.keys():
            formaVida = requestJson["formaVida"]
            formaVida = self.arrayToStr(formaVida)
        else:
            formaVida = ""
        if "substrato" in requestJson.keys():
            substrato = requestJson["substrato"]
            substrato = self.arrayToStr(substrato)
        else:
            substrato = ""
        if "tipoVegetacao" in requestJson.keys():
            tipoVegetacao = requestJson["tipoVegetacao"]
            tipoVegetacao = self.arrayToStr(tipoVegetacao)
        else:
            tipoVegetacao = ""
        if "origem" in requestJson.keys():
            origem = requestJson["origem"]
        else:
            origem = ""
        if "nome" in requestJson.keys():
            nome=self.parseNome(requestJson["nome"])
            autor=self.parseAutor(requestJson["nome"])
            nome = nome.strip()+" "+autor.strip()
        else:
            nome=""
            autor=""
        if "dominioFitogeografico" in requestJson.keys():
            dominioFitogeografico=requestJson["dominioFitogeografico"]
            dominioFitogeografico = self.arrayToStr(dominioFitogeografico)
        else:
            dominioFitogeografico=""
        if "hierarquia" in requestJson.keys():
            familia = self.getFamily(requestJson["hierarquia"])
            grupoTaxonomico = self.getGrupoTaxonomico(requestJson["hierarquia"])
        else:
            familia=""
            grupoTaxonomico=""
        fonte="floradobrasil"
        ocorrenciasConfirmadas = self.parseOcorrenciasConfirmadas(requestJson)
        ocorrenciasDuvidosas = self.parseOcorrenciasDuvidosas(requestJson)
        sinonimosList = []
        if "temComoSinonimo" in requestJson.keys():
            sinonimosList=self.parseSinonimos(requestJson["temComoSinonimo"])

        ocorrenciasConfirmadas = self.arrayToStr(ocorrenciasConfirmadas)
        ocorrenciasDuvidosas = self.arrayToStr(ocorrenciasDuvidosas)
        manager = plantManager.PlantsManager()
        manager.addPlant(nome,autor,fonte,estado,grupoTaxonomico,familia,formaVida,substrato,origem,endemismo,ocorrenciasConfirmadas,ocorrenciasDuvidosas,dominioFitogeografico,tipoVegetacao,"")
        for sino in sinonimosList:
            manager.addPlant(sino[0],sino[1],fonte,"sinonimo","","","","","","","","","","",nome)
        if autor=="" or autor is None:
            autor="desconhecido"

        print("nome:"+nome)
        print("autor:"+autor)
        print("fonte: "+fonte)
        print(estado)
        manager.writeAllToDb()
        '''
        print("endemismo:"+endemismo)
        print("grupo grupoTaxonomico: "+grupoTaxonomico)
        print("familia: "+familia)
        print(tipoVegetacao)
        print(dominioFitogeografico)
        print(formaVida)
        print(substrato)
        print(ocorrenciasConfirmadas)
        print(ocorrenciasDuvidosas)
        for sinonimo in sinonimosList:
            print(sinonimo)
        manager.writeAllToDb()
        '''
        return 1


    def parseNome(self,nomeStr):
        out = ""
        if "<div class=\"taxon\">" in nomeStr:
            out = self.getStringsBetweenS(nomeStr,"<div class=\"taxon\">","</div>").strip()
            out = self.removeString(out,"<i>")
            out = self.removeString(out,"</i>")
        elif "<span><div class=\"taxon vazio\">" in nomeStr:
            out = self.getStringsBetweenS(nomeStr,'<span><div class=\"taxon vazio\">',"</div>").strip()
            out = self.removeString(out,"<i>")
            out = self.removeString(out,"</i>")
        return out.strip()

    def parseAutor(self,nomeStr):
        out = self.getStringsBetweenS(nomeStr,"<div class=\"nomeAutorInfraGenerico\">","</div></span>").strip()
        out = self.removeString(out,"<div>")
        out = self.removeString(out,"</div>")
        return out.strip()

    def parseSinonimoSource(self,ehSinonimoStr):
        result = self.getStringsBetweenS(ehSinonimoStr,"<div class=\"taxon\"> <i>","</i>")
        return result.strip()

    def arrayToStr(self,array):
        out=""
        for i in range(0,len(array)):
            if i==len(array)-1:
                out+=array[i]
            else:
                out+=array[i]+","
        return out

    def parseOcorrenciasConfirmadas(self,requestJson):
        norte = requestJson["distribuicaoGeograficaCertezaNorte"]
        nordeste = requestJson["distribuicaoGeograficaCertezaNordeste"]
        centroOeste = requestJson["distribuicaoGeograficaCertezaCentroOeste"]
        sul = requestJson["distribuicaoGeograficaCertezaSul"]
        sudeste = requestJson["distribuicaoGeograficaCertezaSudeste"]
        ocorrenciasConfirmadas = []
        norteR = self.getStringsBetweenS(norte,"(",")")
        nordesteR = self.getStringsBetweenS(nordeste,"(",")")
        centroOesteR = self.getStringsBetweenS(centroOeste,"(",")")
        sulR =self.getStringsBetweenS(sul,"(",")")
        sudesteR = self.getStringsBetweenS(sudeste,"(",")")
        regioes = norteR.split(",")
        for regiao in regioes:
            regiao = regiao.strip()
            if regiao!="":
                ocorrenciasConfirmadas.append(regiao)
        regioes = nordesteR.split(",")
        for regiao in regioes:
            regiao = regiao.strip()
            if regiao!="":
                ocorrenciasConfirmadas.append(regiao)
        regioes = centroOesteR.split(",")
        for regiao in regioes:
            regiao = regiao.strip()
            if regiao!="":
                ocorrenciasConfirmadas.append(regiao)
        regioes = sulR.split(",")
        for regiao in regioes:
            regiao = regiao.strip()
            if regiao!="":
                ocorrenciasConfirmadas.append(regiao)
        regioes = sudesteR.split(",")
        for regiao in regioes:
            regiao = regiao.strip()
            if regiao!="":
                ocorrenciasConfirmadas.append(regiao)
        return ocorrenciasConfirmadas

    def parseOcorrenciasDuvidosas(self,requestJson):
        norte = requestJson["distribuicaoGeograficaDuvidaNorte"]
        nordeste = requestJson["distribuicaoGeograficaDuvidaNordeste"]
        centroOeste = requestJson["distribuicaoGeograficaDuvidaCentroOeste"]
        sul = requestJson["distribuicaoGeograficaDuvidaSul"]
        sudeste = requestJson["distribuicaoGeograficaDuvidaSudeste"]
        ocorrenciasDuvidosas = []
        norteR = self.getStringsBetweenS(norte,"(",")")
        nordesteR = self.getStringsBetweenS(nordeste,"(",")")
        centroOesteR = self.getStringsBetweenS(centroOeste,"(",")")
        sulR =self.getStringsBetweenS(sul,"(",")")
        sudesteR = self.getStringsBetweenS(sudeste,"(",")")
        regioes = norteR.split(",")
        for regiao in regioes:
            regiao = regiao.strip()
            if regiao!="":
                ocorrenciasDuvidosas.append(regiao)
        regioes = nordesteR.split(",")
        for regiao in regioes:
            regiao = regiao.strip()
            if regiao!="":
                ocorrenciasDuvidosas.append(regiao)
        regioes = centroOesteR.split(",")
        for regiao in regioes:
            regiao = regiao.strip()
            if regiao!="":
                ocorrenciasDuvidosas.append(regiao)
        regioes = sulR.split(",")
        for regiao in regioes:
            regiao = regiao.strip()
            if regiao!="":
                ocorrenciasDuvidosas.append(regiao)
        regioes = sudesteR.split(",")
        for regiao in regioes:
            regiao = regiao.strip()
            if regiao!="":
                ocorrenciasDuvidosas.append(regiao)
        return ocorrenciasDuvidosas

    def getGrupoTaxonomico(self,hierarquiaStr):
        grupos = self.getStringsBetween(hierarquiaStr,"<div class=\"grupo\">","</div>")
        return grupos[len(grupos)-1].strip()

    def getFamily(self,hierarquiaStr):
        taxons = self.getStringsBetween(hierarquiaStr,"<div class=\"taxon\">","</div>")
        family = taxons[0]
        familiy = family +" "+ self.getStringsBetweenS(hierarquiaStr,"<div class=\"taxon\">"+family+"</div><div class=\"nomeAutorSupraGenerico\">","</div>")
        family = self.removeString(family,"<i>")
        family = self.removeString(family,"</i>")
        return family.strip()

    def removeString(self,str,toRemove):
        return str.replace(toRemove,"")

    def parseSinonimos(self,sinonimosStr):
        sinonimosList = []
        sinonimos = self.getStringsBetween(sinonimosStr,"<div class=\"sinonimo\">","</div>")
        for sinonimo in sinonimos:
            startStr = "<div class=\"sinonimo\">"+sinonimo+"</div><div class=\"nomeAutorSinonimo\">"
            endStr = "</div>"
            autor = self.getStringsBetweenS(sinonimosStr,startStr,endStr)
            autor = self.removeString(autor,"<i>")
            autor = self.removeString(autor,"</i>")
            sinonimo = self.removeString(sinonimo,"<i>")
            sinonimo = self.removeString(sinonimo,"</i>")
            sinonimosList.append([sinonimo,autor])
        return sinonimosList

    def getStringsBetweenS(self,stringInput,startStr,endStr):
        vet = stringInput.split(startStr)
        out=""
        for i in range(1, len(vet)):
            vet2 = vet[i].split(endStr)
            out+=vet2[0]
        return out.strip()

    def getStringsBetween(self,stringInput,startStr,endStr):
        vet = stringInput.split(startStr)
        out=[]
        for i in range(1, len(vet)):
            vet2 = vet[i].split(endStr)
            out.append(vet2[0])
        return out
