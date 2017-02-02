# -*- coding: cp1252 -*-
import pygame, random
Meses = ['Janeiro', 'Fevereiro', 'Mar篧, 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembo', 'Outubro', 'Novembro', 'Dezembro']
NumerodoMes = 1
MesAtual = Meses[NumerodoMes-1]
i = 1
Clientes = []
class Pessoa():
    def __init__(self,Nome):
        self.Nome = None
        self.CPF = None
        self.RG = None
        self.Salario = None
        self.PresencaTotal = None
        self.FaltaTotal = None
        self.PresencaMensal = None
        self.FaltaMensal = None
        print "Cadastrando membro."
        print "Cadastrando membro.."
        print "Cadastrando membro..."
#------------------Gets e Sets--------------------------------------------
    def GetNome(self):
        return self.Nome
    def SetNome(self,NomedaPessoa):
        #NomedaPessoa = raw_input("Digite seu nome : ")
        self.Nome = NomedaPessoa 
    def GetCPF(self):
        return self.CPF
    def SetCPF(self):
        CPFdaPessoa = raw_input("Digite seu CPF :")
        self.CPF = CPFdaPessoa 
    def GetRG(self):
        return self.RG
    def SetRG(self):
        RGdaPessoa = raw_input("Digite seu RG :")
        self.RG = RGdaPessoa 
    def GetSalario(self):
        return self.Salario
    def SetSalario(self):
        SalariodaPessoa = input("Digite seu salᲩo :")
        self.Salario = SalariodaPessoa
#--------------------------------------------------------------------------
    def ContadePresencaseFaltas(self):
        #Conta das Presen硳 Mensais
        if self.PresencaMensal == None:
           self.PresencaMensal = 0
        elif MesAtual in ['Abril','Junho','Setembro','Novembro']:
            if self.PresencaMensal >= 30:
                NumerodoMes += 1
        elif MesAtual in ['Janeiro','Mar篧,'Maio','Julho','Agosto','Outubro','Dezembro']:
            if self.PresencaMensal >= 31:
                NumerodoMes += 1
        elif MesAtual == 'Fevereiro':
            if self.PresencaMensal >= 28:
                NumerodoMes += 1     
        #Conta das faltas mensais
        if self.FaltaMensal == None:
            self.FaltaMensal = 0
        elif MesAtual in ['Abril','Junho','Setembro','Novembro']:
            if self.FaltaMensal >= 30:
                NumerodoMes += 1
        elif MesAtual in ['Janeiro','Mar篧,'Maio','Julho','Agosto','Outubro','Dezembro']:
            if self.FaltaMensal >= 31:
                NumerodoMes += 1
        elif MesAtual == 'Fevereiro':
            if self.FaltaMensal >= 28:
                NumerodoMes += 1     
    def ExibirInformacoes():
        print "As Informa絥s da Pessoa: "
        print "Nome: ", self.Nome
        print "CPF: ",self.CPF
        print "RG: ", self.RG
        print "SalᲩo: ",self.Salario
        print "Presen硠Total: ",self.PresencaTotal
        print "Falta Total: ",self.FaltaTotal
        print "Presen硠Mensal", self.PresencaMensal
        print "Falta Mensal", self.FaltaMensal
        
    #Repetir para todos os dias do m곍
        print "Digite o n򭥲o correspondente ao caso:"
        print "1. Pessoa Presente"
        print "2. Pessoa Faltou"
        SituacaodoDia = input()
        print "Registrando." #Fazer esses print ficarem numa 򮩣a linha
        print "Registrando.."
        print "Registrando..."
        if SituacaodoDia == 1:
            self.PresencaMensal+=1
        elif SituacaodoDia == 2:
            self.FaltaMensal+=1
        print "Registrado!"
        
def Menu():
    global i
    if NumerodoMes == None:
        print "Bem vindo ao gerenciamento de funcionᲩos,"
    print "Digite o n򭥲o correspondente ao que deseja fazer"
    print "1.........Cadastrar"
    print "2.........Anotar Falta ou presen硢
    Escolha = input()
    if Escolha == 1:
        Nome = raw_input("Digite o nome da pessoa")
        Pessoa(Nome).SetNome(Nome)
        
    elif Escolha ==2:
        self.ContadePresencaseFaltas()
Menu()
