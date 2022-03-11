from services.pier import Pier
import json

def handle_request(row, pier):
    def operacao(flag):
        if flag == 1:
            return "habilitar-operacao"
        if flag == 0:
            return "desabilitar-operacao"

    id, idEstabelecimento, idOperacao, idProduto, mcc, flagoperacao = row

    data = {"idProduto": idProduto, "idOperacao":idOperacao, "codigoMCC": mcc}
    url = f"/estabelecimentos/{idEstabelecimento}/{operacao(flagoperacao)}" 
    status, content = pier.post(url=url, body=json.dumps(data))
    return status, url

        
