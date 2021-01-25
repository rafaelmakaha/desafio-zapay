#!/usr/bin/python
# -*- coding: latin-1 -*-
from api import API


class SPService:
    """
    Conecta com o webservice do Detran-SP.
    """

    def __init__(self, **kwargs):
        """
        Construtor.
        """
        self.params = kwargs
            
        if kwargs["license_plate"][4].isalpha():
            self.plate_convert()

    def plate_convert(self):
        plate = self.params["license_plate"]
        self.params["license_plate"] = plate[:4] + str(ord(plate[4]) - 65) + plate[5:]

    def get_json_response(self, method):
        """
        Pega a resposta da requisição em json.
        """
        api = API(self.params["license_plate"], self.params["renavam"], method)
        return api.fetch()

    def debt_search(self):
        """
        Pega os débitos de acordo com a opção passada.
        """
        if not self.params['debt_option']:
            debts = {
                'IPVAs': self.get_json_response("ConsultaIPVA").get('IPVAs') or {},
                'DPVATs': self.get_json_response("ConsultaDPVAT").get('DPVATs') or {},
                'Multas': self.get_json_response("ConsultaMultas").get('Multas') or {},
                'Licenciamento': self.get_json_response("ConsultaLicenciamento") or {},
            }
            return debts

        elif self.params['debt_option'] == 'ticket':
            response_json = self.get_json_response("ConsultaMultas")

        elif self.params['debt_option'] == 'licensing':
            response_json = self.get_json_response("ConsultaLicenciamento")

        elif self.params['debt_option'] == 'ipva':
            response_json = self.get_json_response("ConsultaIPVA")

        elif self.params['debt_option'] == 'dpvat':
            response_json = self.get_json_response("ConsultaDPVAT")

        else:
            raise Exception("opção inválida")

        debts = {
            'IPVAs': response_json.get('IPVAs') or {},
            'DPVATs': response_json.get('DPVATs') or {},
            'Multas': response_json.get('Multas') or {},
            'Licenciamento': response_json or {},
        }

        for debt in debts:
            if debts[debt] == {}:
                debts[debt] = None

        return debts
