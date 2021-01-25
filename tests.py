from service import SPService
import pytest

# Para rodar os testes: python3 -m pytest tests.py

# =============== SERVICE =============
def test_service_search_ticket_succsess(mocker):
    service = SPService(
        license_plate="ABC1234",
        renavam="11111111111",
        debt_option="ticket"
    )
    mocker.patch.object(
        service,
        'debt_search'
    )
    service.debt_search.return_value={'Multas': {'Multa': [{'AIIP': '5E5E5E5E  ', 'DescricaoEnquadramento': 'Estacionar em Desacordo com a Sinalizacao.', 'Guia': 472535212, 'Valor': 20118}, {'AIIP': '6F6F6F6F  ', 'DescricaoEnquadramento': 'Trans. Veloc. Super. a Maxima Permitidaem Ate 20%.', 'Valor': 13166}]}, 'Licenciamento': {'Multas': {'Multa': [{'AIIP': '5E5E5E5E  ', 'DescricaoEnquadramento': 'Estacionar em Desacordo com a Sinalizacao.', 'Guia': 472535212, 'Valor': 20118}, {'AIIP': '6F6F6F6F  ', 'DescricaoEnquadramento': 'Trans. Veloc. Super. a Maxima Permitidaem Ate 20%.', 'Valor': 13166}]}, 'Veiculo': {'Placa': 'ABC1234', 'Renavam': '11111111111', 'UF': 'SP', 'Proprietario': 'JOHN', 'CPFCNPJ': '000.000.000-00'}, 'Servico': 'Multas'}, 'IPVAs': None, 'DPVATs': None}
    result = service.debt_search()
    expected = {'Multas': {'Multa': [{'AIIP': '5E5E5E5E  ', 'DescricaoEnquadramento': 'Estacionar em Desacordo com a Sinalizacao.', 'Guia': 472535212, 'Valor': 20118}, {'AIIP': '6F6F6F6F  ', 'DescricaoEnquadramento': 'Trans. Veloc. Super. a Maxima Permitidaem Ate 20%.', 'Valor': 13166}]}, 'Licenciamento': {'Multas': {'Multa': [{'AIIP': '5E5E5E5E  ', 'DescricaoEnquadramento': 'Estacionar em Desacordo com a Sinalizacao.', 'Guia': 472535212, 'Valor': 20118}, {'AIIP': '6F6F6F6F  ', 'DescricaoEnquadramento': 'Trans. Veloc. Super. a Maxima Permitidaem Ate 20%.', 'Valor': 13166}]}, 'Veiculo': {'Placa': 'ABC1234', 'Renavam': '11111111111', 'UF': 'SP', 'Proprietario': 'JOHN', 'CPFCNPJ': '000.000.000-00'}, 'Servico': 'Multas'}, 'IPVAs': None, 'DPVATs': None}

    assert result == expected

def test_service_search_ticket_fail(mocker):
    service = SPService(
        license_plate="ABC1234",
        renavam="11111111112",
        debt_option="ticket"
    )
    mocker.patch.object(
        service,
        'debt_search'
    )
    service.debt_search.return_value='Veículo não encontrado'
    result = service.debt_search()
    expected = 'Veículo não encontrado'

    assert result == expected

def test_service_search_ipva_success(mocker):
    service = SPService(
        license_plate="ABC1234",
        renavam="11111111111",
        debt_option="ipva"
    )
    mocker.patch.object(
        service,
        'debt_search'
    )
    service.debt_search.return_value = {'Multas': None, 'Licenciamento': {'Veiculo': {'Placa': 'ABC1234', 'Renavam': '11111111111', 'UF': 'SP', 'Proprietario': 'JOHN', 'CPFCNPJ': '000.000.000-00'}, 'IPVAs': {'IPVA': [{'Exercicio': 2021, 'Valor': 136569, 'Cota': 8}, {'Exercicio': 2020, 'Valor': 101250, 'Cota': 2}]}, 'Servico': 'IPVA'}, 'IPVAs': {'IPVA': [{'Exercicio': 2021, 'Valor': 136569, 'Cota': 8}, {'Exercicio': 2020, 'Valor': 101250, 'Cota': 2}]}, 'DPVATs': None}
    result = service.debt_search()
    expected =  {'Multas': None, 'Licenciamento': {'Veiculo': {'Placa': 'ABC1234', 'Renavam': '11111111111', 'UF': 'SP', 'Proprietario': 'JOHN', 'CPFCNPJ': '000.000.000-00'}, 'IPVAs': {'IPVA': [{'Exercicio': 2021, 'Valor': 136569, 'Cota': 8}, {'Exercicio': 2020, 'Valor': 101250, 'Cota': 2}]}, 'Servico': 'IPVA'}, 'IPVAs': {'IPVA': [{'Exercicio': 2021, 'Valor': 136569, 'Cota': 8}, {'Exercicio': 2020, 'Valor': 101250, 'Cota': 2}]}, 'DPVATs': None}
    
    assert result == expected

def test_service_search_ipva_fail(mocker):
    service = SPService(
        license_plate="ABC1234",
        renavam="11111111112",
        debt_option="ipva"
    )
    mocker.patch.object(
        service,
        'debt_search'
    )
    service.debt_search.return_value='Veículo não encontrado'
    result = service.debt_search()
    expected='Veículo não encontrado'

    assert result == expected

def test_service_search_licensing_success(mocker):
    service = SPService(
        license_plate="ABC1234",
        renavam="11111111111",
        debt_option="licensing"
    )
    mocker.patch.object(
        service,
        'debt_search'
    )
    service.debt_search.return_value = {'Multas': None, 'Licenciamento': {'Exercicio': 2021, 'Veiculo': {'Placa': 'ABC1234', 'Renavam': '11111111111', 'UF': 'SP', 'Proprietario': 'JOHN', 'CPFCNPJ': '000.000.000-00'}, 'Servico': 'Licenciamento', 'TaxaLicenciamento': 9891}, 'IPVAs': None, 'DPVATs': None}

    result = service.debt_search()
    expected = {'Multas': None, 'Licenciamento': {'Exercicio': 2021, 'Veiculo': {'Placa': 'ABC1234', 'Renavam': '11111111111', 'UF': 'SP', 'Proprietario': 'JOHN', 'CPFCNPJ': '000.000.000-00'}, 'Servico': 'Licenciamento', 'TaxaLicenciamento': 9891}, 'IPVAs': None, 'DPVATs': None}
    
    assert result == expected

def test_service_search_licensing_fail(mocker):
    service = SPService(
        license_plate="ABC1234",
        renavam="11111111112",
        debt_option="licensing"
    )
    mocker.patch.object(
        service,
        'debt_search'
    )
    service.debt_search.return_value='Veículo não encontrado'
    result = service.debt_search()
    expected='Veículo não encontrado'
    assert result == expected

def test_service_search_dpvat_success(mocker):
    service = SPService(
        license_plate="ABC1234",
        renavam="11111111111",
        debt_option="dpvat"
    )
    mocker.patch.object(
        service,
        'debt_search'
    )
    service.debt_search.return_value = {'Multas': None, 'Licenciamento': {'Veiculo': {'Placa': 'ABC1234', 'Renavam': '11111111111', 'UF': 'SP', 'Proprietario': 'JOHN', 'CPFCNPJ': '000.000.000-00'}, 'Servico': 'DPVAT', 'DPVATs': {'DPVAT': [{'Exercicio': 2020, 'Valor': 523}]}}, 'IPVAs': None, 'DPVATs': {'DPVAT': [{'Exercicio': 2020, 'Valor': 523}]}}

    result = service.debt_search()
    expected = {'Multas': None, 'Licenciamento': {'Veiculo': {'Placa': 'ABC1234', 'Renavam': '11111111111', 'UF': 'SP', 'Proprietario': 'JOHN', 'CPFCNPJ': '000.000.000-00'}, 'Servico': 'DPVAT', 'DPVATs': {'DPVAT': [{'Exercicio': 2020, 'Valor': 523}]}}, 'IPVAs': None, 'DPVATs': {'DPVAT': [{'Exercicio': 2020, 'Valor': 523}]}}

    assert result == expected

def test_service_search_dpvat_fail(mocker):
    service = SPService(
        license_plate="ABC1234",
        renavam="11111111112",
        debt_option="dpvat"
    )
    mocker.patch.object(
        service,
        'debt_search'
    )
    service.debt_search.return_value='Veículo não encontrado'
    result = service.debt_search()
    expected='Veículo não encontrado'
    assert result == expected

def test_service_plate_convert_success():
    service = SPService(
        license_plate="ABC1C34",
        renavam="11111111111",
        debt_option="dpvat"
    )
    result = service.params["license_plate"]
    expected='ABC1234'
    assert result == expected

def test_service_plate_convert_fail():
    with pytest.raises(TypeError):
        service = SPService(
            license_plate=None,
            renavam="11111111111",
            debt_option="dpvat"
        )
