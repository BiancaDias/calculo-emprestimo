'''
1-Formulação do problema:
    A SOLAR ENERGY, empresa sediada em Vitória: ES, 
    comercializa sistema de geração de energia elétrica a partir da energia solar. Normalmente, seus 
    clientes optam por pagar a prazo de até 5 anos (60 meses). Para auxiliar nas vendas os 
    vendedores demandaram da empresa que disponibilize um aplicativo para simular o 
    financiamento segundo a Tabela Price. Assim, o cliente, melhor informado sobre o 
    financiamento, tomará a decisão de forma mais segura. 
2- Algoritmo
    1-Criação da classe "Price" com:
        1-vetores que irão acumular os valores para a criação do gráfico;
        2-Valores iniciais: Valor financiado, juros, tempo de financiamento, fator e carencia.
    2-Funções:
        1-Função para calculo do financiamento sem carencia;
        2-Função para calculo com carencia e com pagamento de juros no periodo e;
        3-Função para calculo com do financiamento com carencia e sem pagamento de juros durante o periodo.
        4-Função para descobrir a quantidade de parcelas que serão geradas
        5-Função para descobrir de quanto em quanto tempo essas parcelas serão pagas;
        6-Funções para impressão de cada um dos 3 tipos de financiamento.
    3-Criação de um objeto "tabela"
        -Será possível cadastrar os dados e, com base neles a geração de tabelas e gráficos.
'''
class price:
    #Inicialização da classe
    vetorK = []
    vetorAmortizacao = []
    vetorJuros = []
    vetorSaldoDevedor = []
    def __init__(self, So, j, n, fator, nca):
        self.So = So
        self.j = j
        self.n = n
        self.fator = fator
        self.nca = nca
        
        
        self.cima = self.j/(100*self.fator)
        self.exp = (-self.n * self.fator)
        self.baixo = (1+self.cima)
        
    #Quitação da dívida sem período de carência    
    def QuitacaoSemCarencia(self, parcelaAtual):
        self.So = parcelaAtual
        a = self.So * (self.cima/(1-(self.baixo)**self.exp))
        return(a)
    
    #Quitação da dívida com período de carência com pagamento de juros no período
    def QuitacaoComCarencia(self, parcelaAtual):
        self.So = parcelaAtual
        b = self.So * (self.cima/(1-(self.baixo)**-self.fator * (self.n - self.nca)))
        return(b)
    
    #Quitação da dívida com período de carência sem pagamento de juros no período
    def QuitacaoComCarenciaSemJuros(self, parcelaAtual):
        self.So = parcelaAtual
        c = (self.So * ((self.baixo)**(self.nca*self.fator))) * (self.cima/(1-(self.baixo)**-self.fator *(self.n - self.nca)))
        return(c)
    #funcao que retorna o numero de parcelas que serão pagas
    def NumerodeParcelas(self):
        if(self.fator == 12):
            #mensal
            return int(self.n*12)#irá seguir a duração do financiamento pagamento mensalmente
        elif(self.fator == 6):
            #bimestral
            return int((self.n*12)/2)
        elif(self.fator==4):
            #trimestral
            return int((self.n*12)/3)
        elif(self.fator==2):
            #semestral
            return int((self.n*12)/6)
        elif(self.fator==1):
            #anual
            return int(self.n)
    #de quanto em quanto tempo
    def AcadaQuantoTempo(self):
        if(self.fator == 12):
            #mensal
            return 1
        elif(self.fator == 6):
            #bimestral
            return 2
        elif(self.fator==4):
            #trimestral
            return 3
        elif(self.fator==2):
            #semestral
            return 6
        elif(self.fator==1):
            #anual
            return 12
            
    
    def ImpressaoQuitacaoSemCarencia(self):
        linha = '_' *100
        print(linha)
        print('{:<2}  {:>10}  {:>10}  {:>10}  {:>10}'.format('Mês da Prestação','Saldo Devedor (R$)','Valor Amortizado (R$)','Juros Pago (R$)','Valor da Prestação (R$)'))
        print(linha)
        parcelaAtual = self.So
        print('{:<2}        {:^.2f}            {:^10}            {:^10}           {:^10}' .format('Contratação', parcelaAtual,'0.00' , '0.00' , '0.00'))
         
        totalAmortizacao = 0.0
        totalJurosPagos = 0.0
        totalPrestacoes = 0.0
        duracao = self.NumerodeParcelas()
        for k in range(1, duracao +1):
            
            Juros = (self.j*(parcelaAtual))/(100*self.fator)
            Amortizacao = self.QuitacaoSemCarencia(self.So) - Juros
            parcelaAtual = parcelaAtual-Amortizacao
            self.vetorK.append(k)
            self.vetorAmortizacao.append(Amortizacao)
            self.vetorJuros.append(juros)
            self.vetorSaldoDevedor.append(parcelaAtual)
              
            print('{:<2}                 {:<.2f}              {:<.2f}              {:<.2f}              {:<.2f}' .format(k, parcelaAtual,Amortizacao , Juros , self.QuitacaoSemCarencia(self.So)))
        
            totalAmortizacao = totalAmortizacao + Amortizacao
            totalJurosPagos = totalJurosPagos +Juros
            totalPrestacoes = totalPrestacoes + self.QuitacaoSemCarencia(self.So)
        print('{:<10}    {:^10}              {:<.2f}              {:<.2f}              {:<.2f}' .format("Totais (R$)", "",totalAmortizacao , totalJurosPagos , totalPrestacoes))
            
    def ImpressaoQuitacaoComCarencia(self):
        linha = '_' *100
        print(linha)
        print('{:<2}  {:>10}  {:>10}  {:>10}  {:>10}'.format('Mês da Prestação','Saldo Devedor (R$)','Valor Amortizado (R$)','Juros Pago (R$)','Valor da Prestação (R$)')) 
        valoraPagar = self.So
        print(linha)
        print('{:<2}        {:^.2f}            {:^10}            {:^10}           {:^10}' .format('Contratação', valoraPagar,'0.00' , '0.00' , '0.00'))
        carencia = int (self.nca)
        totalAmortizacao = 0
        totalJuros = 0
        totalPrestacoes = 0
        aCadaQuantosMeses = int(self.AcadaQuantoTempo())
        for k  in range (1, carencia+1,aCadaQuantosMeses):
            juros = (self.j * valoraPagar) / (100*self.fator)
            totalJuros = totalJuros + juros
            prestacao = juros
            totalPrestacoes = totalPrestacoes + prestacao
            print('{:^2}                 {:^.2f}            {:^10}            {:^.2f}              {:^.2f}' .format(k, valoraPagar,'0.00' , juros , prestacao))

        restante = int(self.NumerodeParcelas())
        for i in range (carencia+1, restante+1):
            
            valorDaPrestacao = self.QuitacaoComCarencia(self.So)
            Juros = (self.j * valoraPagar) / (100*self.fator) #verificar se o 12 se refere a uma variavel
            Amortizacao = valorDaPrestacao - Juros

            valoraPagar = valoraPagar - Amortizacao 
            totalAmortizacao = totalAmortizacao + Amortizacao
            totalJuros = totalJuros + Juros
            totalPrestacoes = totalPrestacoes + valorDaPrestacao
            print('{:<2}                 {:<.2f}              {:<.2f}            {:<.2f}                {:<.2f}' .format(i, valoraPagar,Amortizacao , Juros , valorDaPrestacao))
        print('{:<10}    {:^10}              {:<.2f}              {:<.2f}              {:<.2f}' .format("Totais (R$)", "",totalAmortizacao , totalJuros , totalPrestacoes))

    def ImpressaoQuitacaoComCarenciaSemJuros(self):
        linha = '_' *100
        print(linha)
        print('{:<2}  {:>10}  {:>10}  {:>10}  {:>10}'.format('Mês da Prestação','Saldo Devedor (R$)','Valor Amortizado (R$)','Juros Pago (R$)','Valor da Prestação (R$)')) 
        print(linha)
        valoraPagar = self.So
        print('{:<2}        {:^.2f}            {:^10}            {:^10}           {:^10}' .format('Contratação', valoraPagar,'0.00' , '0.00' , '0.00'))
        totalAmortizacao = 0
        totalJuros = 0
        totalPrestacoes = 0
        carencia = int(self.nca * 12)
        restante = int(self.n * 12)
        aCadaQuantosMeses = int(self.AcadaQuantoTempo())
        for i in range(1,carencia+1, aCadaQuantosMeses):
            juros = (self.j * valoraPagar) / (self.fator)
            valoraPagar = valoraPagar + juros
            #totalJuros = totalJuros + juros
            print('{:^2}                 {:^.2f}            {:^10}            {:^.2f}              {:^10}' .format(i, valoraPagar,'0.00' , juros , '0.00'))
        for j in range (carencia+1,restante+1):
            valorDaPrestacao = self.QuitacaoComCarenciaSemJuros(self.So)
            Juros = (self.j * valoraPagar) / (self.fator) #verificar se o 12 se refere a uma variavel
            Amortizacao = valorDaPrestacao - Juros

            valoraPagar = valoraPagar - Amortizacao #declarar amortizacao
            totalAmortizacao = totalAmortizacao + Amortizacao
            totalJuros = totalJuros + Juros
            totalPrestacoes = totalPrestacoes + valorDaPrestacao
            print('{:<2}                 {:<.2f}              {:<.2f}            {:<.2f}                {:<.2f}' .format(j, valoraPagar,Amortizacao , Juros , valorDaPrestacao))
        print('{:<10}    {:^10}              {:<.2f}              {:<.2f}              {:<.2f}' .format("Totais (R$)", "",totalAmortizacao , totalJuros , totalPrestacoes))





            
        
            
    
print('Digite o valor do financiamento:\n')
financiamento = float(input())
print('Digite a taxa de juros ao ano:\n')
juros =float (input())
print('Qual será a duração do financiamento (em meses)? (limite: 60 meses)\n')
duracao = int(input())/12
print('Qual será o periodo de carencia (em meses)? (de 0 a 12 meses)\n')
carencia = int(input())/12
print('Serão pagos juros no periodo de carencia? (s ou n)\n')
pagamentodeJurosCarencia = str(input())

print('Será parcelado de que forma? Favor digitar o numero correspondente:\n1-Mensal\n2-Bimestral\n3-Trimestral\n4-Semestral\n5-Anual')
fator=int(input())

if(fator == 1):
    fator = 12
elif(fator == 2):
    fator = 6
elif(fator==3):
    fator = 4
elif(fator==4):
    fator = 2
elif(fator==5):
    fator = 1

tabela = price(financiamento,juros,duracao,fator,carencia)

if(carencia == 0):
    tabela.ImpressaoQuitacaoSemCarencia()
elif(carencia > 0 and (pagamentodeJurosCarencia == 's' or pagamentodeJurosCarencia == 'S')):
    tabela.ImpressaoQuitacaoComCarencia()
elif(carencia > 0 and (pagamentodeJurosCarencia == 'n' or pagamentodeJurosCarencia == 'N')):
    tabela.ImpressaoQuitacaoComCarenciaSemJuros()