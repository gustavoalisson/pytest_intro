from pytest import mark
from codigo.jogo import brincadeira

#LINHA DE COMANDO
# pytest -v (mostra os testes que passou)
# pytest -x (para no teste que falhou, sem precisar mostrar todos os teste)
# pýtest --pdb (Debug / Consigo ver o escopo (acesso a tudo que tem no escopo))
# pytest -k "exemplo_queijo"
# pytest -s mostra os prints da funcao 

# gerar xml > pytest --junitxml example.xml

'''
O teste é formado por 3 etapas (GWT - AAA):

* Given - Dado
* When - Quando
* Then - Então

* Arange
* Act
* Assert

xUnit Patterns

- Setup - Dado
- Exercise - Quando
- Verify - Então
- TearDown - "Desmonta tudo antes que seja tarde" rsrs

'''

''' 
RESPOSTA DE RESUMO

. Passou
F Falhou
x Falha esperada
X Falha esperada, mas nao falhou 
s pulou
'''

# ! Toda vez que tiver um teste a mensagem não for AssertionError, significa que o que esta errado é a estrutura do codigo
# OU seja, ASSERTION ERROR - TUDO deu certo, menos o resultado...

# ! MARCAÇÕES

# Criar grupo de marcações exe: @mark.tag 
# Exemplo: pytest -m tag
# Exemplo2: pytest -m "not tag"

@mark.smoke
def test_quando_brincadeira_receber_1_entao_deve_retornar_1():
    '''
    - Brincadeira - SUT - System Under Test
    '''
    entrada = 1 #given
    esperado = 1 #given
    
    resultado = brincadeira(entrada) #when
    
    # TDD - Kent Beck - One-steo Test
    assert resultado == esperado #then
    
def test_quando_brincadeira_receber_2_entao_deve_retornar_2():
    
    assert brincadeira(2) == 2
    
@mark.smoke
def test_quando_brincadeira_receber_3_entao_deve_retornar_queijo():
    
    assert brincadeira(3) == 'queijo'

@mark.goiabada
def test_quando_brincadeira_receber_5_entao_deve_retornar_goiabada():
    
    assert brincadeira(5) == 'goiabada'
    
@mark.goiabada
def test_quando_brincadeira_receber_10_entao_deve_retornar_goiabada():
    
    assert brincadeira(10) == 'goiabada'

@mark.goiabada
@mark.smoke
def test_quando_brincadeira_receber_20_entao_deve_retornar_goiabada():
    
    assert brincadeira(20) == 'goiabada'    
    
@mark.skip(reason='Não vai rodar, pq ainda não implementei')    
def test_quando_brincadeira_receber_menor_do_que_1_entao_deve_retornar_None():
    
    assert brincadeira(-2) == 'goiabada'
    
@mark.xfail
def test_xfail_1():
    assert brincadeira(20) != 'goiabada'
    
import sys
    
@mark.xfail(sys.platform == 'win32')
def test_xfail_windows():
    assert brincadeira(20) == 'goiabada'
    

@mark.skipif(sys.platform == 'win32')
def test_xfail_windows_skip():
    assert brincadeira(20) == 'goiabada'                    

@mark.parametrizado
@mark.parametrize(
    'entrada',
    [3,6,9,12,18]
)
def test_brincadeira_deve_retornar_queijo_com_multiplos_de_3(entrada):
    
    assert brincadeira(entrada) == 'queijo'
    
    
# @mark.parametrizado
# @mark.parametrize(
#     'entrada, esperado',
#     [(1,1), (2,2), (3, 'queijo'), (4,4), (5,'goiabada')]
# )
# def test_brincadeira_deve_retornar_valor_esperado(entrada, esperado):
    
#     assert brincadeira(entrada) == esperado    
