import json
import Plant as plantManager

class FloraDecoder:

    def decodeRequestAndWriteToDb(self,requestJson):
        estado = requestJson["statusQualificador"]
        if "Sinônimo" in estado or "sinônimo" in estado or "Sinonimo" in estado or "sinonimo" in estado:
            result = self.parseSinonimoSource(requestJson["ehSinonimo"])
            return result
        if "Nome correto" in estado:
            estado = "Nome correto"
        elif "Nome aceito" in estado:
            estado = "Nome aceito"
        endemismo = requestJson["endemismo"]
        formaVida = requestJson["formaVida"]
        substrato = requestJson["substrato"]
        tipoVegetacao = requestJson["tipoVegetacao"]
        origem = requestJson["origem"]
        nome=self.parseNome(requestJson["nome"])
        autor=self.parseAutor(requestJson["nome"])
        dominioFitogeografico=requestJson["dominioFitogeografico"]
        familia = self.getFamily(requestJson["hierarquia"])
        grupoTaxonomico = self.getGrupoTaxonomico(requestJson["hierarquia"])
        fonte="floradobrasil"
        ocorrenciasConfirmadas = self.parseOcorrenciasConfirmadas(requestJson)
        ocorrenciasDuvidosas = self.parseOcorrenciasDuvidosas(requestJson)
        sinonimosList=self.parseSinonimos(requestJson["temComoSinonimo"])
        sinonimosDbFormat = []
        for sinonimo in sinonimosList:
            nomeSinonimo = sinonimo[0]
            autorSinonimo = sinonimo[1]
            sinonimosDbFormat.append((nomeSinonimo,autorSinonimo,fonte,nome))
        dominioFitogeografico = self.arrayToStr(dominioFitogeografico)
        tipoVegetacao = self.arrayToStr(tipoVegetacao)
        formaVida = self.arrayToStr(formaVida)
        substrato = self.arrayToStr(substrato)
        ocorrenciasConfirmadas = self.arrayToStr(ocorrenciasConfirmadas)
        ocorrenciasDuvidosas = self.arrayToStr(ocorrenciasDuvidosas)
        manager = plantManager.PlantsManager()
        manager.addPlant(nome,autor,fonte,estado,grupoTaxonomico,familia,formaVida,substrato,origem,endemismo,ocorrenciasConfirmadas,ocorrenciasDuvidosas,dominioFitogeografico,tipoVegetacao,sinonimosDbFormat)
        print("nome:"+nome)
        print("autor:"+autor)
        print("endemismo:"+endemismo)
        print("grupo grupoTaxonomico: "+grupoTaxonomico)
        print("familia: "+familia)
        print("fonte: "+fonte)
        print(estado)
        print(tipoVegetacao)
        print(dominioFitogeografico)
        print(formaVida)
        print(substrato)
        print(ocorrenciasConfirmadas)
        print(ocorrenciasDuvidosas)
        for sinonimo in sinonimosDbFormat:
            print(sinonimo)
        manager.writeAllToDb()
        return 1

    def parseNome(self,nomeStr):
        return self.getStringsBetweenS(nomeStr,"<div class=\"taxon\"> <i>","</i></div>").strip()

    def parseAutor(self,nomeStr):
        return self.getStringsBetweenS(nomeStr,"<div class=\"nomeAutorInfraGenerico\">","</div></span>").strip()

    def parseSinonimoSource(self,ehSinonimoStr):
        result = self.getStringsBetweenS(ehSinonimoStr,"<div class=\"taxon\"> <i>","</i>")
        print(result)
        return result

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
        taxons = self.getStringsBetween(hierarquiaStr,"<div class=\"taxon\"> <i>","</i></div>")
        family = taxons[len(taxons)-2]
        familiy = family +" "+ self.getStringsBetweenS(hierarquiaStr,"<div class=\"taxon\">"+family+"</div><div class=\"nomeAutorSupraGenerico\">","</div>")
        return family.strip()

    def parseSinonimos(self,sinonimosStr):
        sinonimosList = []
        sinonimos = self.getStringsBetween(sinonimosStr,"<div class=\"sinonimo\"> <i>","</i>")
        for sinonimo in sinonimos:
            startStr = "<div class=\"sinonimo\"> <i>"+sinonimo+"</i></div><div class=\"nomeAutorSinonimo\">"
            endStr = "</div>"
            autor = self.getStringsBetweenS(sinonimosStr,startStr,endStr)
            sinonimosList.append([sinonimo,autor])
        return sinonimosList

    def getStringsBetweenS(self,stringInput,startStr,endStr):
        vet = stringInput.split(startStr)
        out=""
        for i in range(1, len(vet)):
            vet2 = vet[i].split(endStr)
            out+=vet2[0]
        return out

    def getStringsBetween(self,stringInput,startStr,endStr):
        vet = stringInput.split(startStr)
        out=[]
        for i in range(1, len(vet)):
            vet2 = vet[i].split(endStr)
            out.append(vet2[0])
        return out
