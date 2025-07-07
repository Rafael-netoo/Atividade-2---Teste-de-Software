package org.example;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class DispensadoraTest {

    private Dispensadora dispensadora;

    @Test
    public void bacistests(){
        int[] cedulasInicial = {10, 10, 10, 10, 10, 10}; // Inicializando com 10 cédulas de cada valor
        Dispensadora dispensadora = new Dispensadora(cedulasInicial);
        int[] VALORES_CEDULAS = {100, 50, 20, 10, 5, 2};


        //teste do main
        try {
            int[] resultado = dispensadora.dispensar(280); // Exemplo que  pode ser atendido
            System.out.println("Cédulas usadas: ");
            for (int i = 0; i < resultado.length; i++) {
                System.out.println(VALORES_CEDULAS[i] + " reais: " + resultado[i] + " cédulas");
            }
        } catch (NaoEhPossivelDispensarValorException e) {
            System.out.println("Erro: " + e.getMessage());
        }

        //teste com valores exatos de celulas necessarias para valor solicitado

        int[] cedulasTeste2 = {1,1,0,0,0,0}; // Inicializando com 1 cédula de R$100,00 e 1 cédula de R$ 50,00
        Dispensadora dispensadora2 = new Dispensadora(cedulasTeste2);

        try {
            int[] resultado = dispensadora2.dispensar(150); // Exemplo que pode ser atendido
            System.out.println("Cédulas usadas: ");
            for (int i = 0; i < resultado.length; i++) {
                System.out.println(VALORES_CEDULAS[i] + " reais: " + resultado[i] + " cédulas");
            }
        } catch (NaoEhPossivelDispensarValorException e) {
            System.out.println("Erro: " + e.getMessage());
        }


        //teste com valores insuficientes(erro esperado)

        int[] cedulasTeste3 = {0,1,0,0,0,0}; // Inicializando com 1 cédula de R$ 100,00
        Dispensadora dispensadora3 = new Dispensadora(cedulasTeste3);

        try {
            int[] resultado = dispensadora3.dispensar(150); // Exemplo que não pode ser atendido
            System.out.println("Cédulas usadas: ");
            for (int i = 0; i < resultado.length; i++) {
                System.out.println(VALORES_CEDULAS[i] + " reais: " + resultado[i] + " cédulas");
            }
        } catch (NaoEhPossivelDispensarValorException e) {
            System.out.println("Erro: " + e.getMessage());
        }


        //teste para troco impossivel(erro esperado)
        int[] cedulasTeste4 = {0,0,0,0,1,1}; // inicializando com 1 cedula de R$ 5,00 e 1 cedula de R$ 2,00
        Dispensadora dispensadora4 = new Dispensadora(cedulasTeste4);

        try {
            int[] resultado = dispensadora4.dispensar(3); //
            System.out.println("Cédulas usadas: ");
            for (int i = 0; i < resultado.length; i++) {
                System.out.println(VALORES_CEDULAS[i] + " reais: " + resultado[i] + " cédulas");
            }
        } catch (NaoEhPossivelDispensarValorException e) {
            System.out.println("Erro: " + e.getMessage());
        }


    }


    @Test
    public void secondTests(){
        int[] cedulasInicial = {10, 10, 10, 10, 10, 10}; // Inicializando com 10 cédulas de cada valor
        Dispensadora dispensadora = new Dispensadora(cedulasInicial);
        int[] VALORES_CEDULAS = {100, 50, 20, 10, 5, 2};

       //verifica se a maquina remove as cedulas corretas e se as cedulas disponíveis após o processo serão as esperadas
        try {
            int[] resultado = dispensadora.dispensar(150); //
            int[] cedulasDisponiveisEsperadas = {9,9,10,10,10,10};
            assertArrayEquals(cedulasDisponiveisEsperadas, dispensadora.getCedulasDisponiveis(),"valores diferentes");
        } catch (NaoEhPossivelDispensarValorException e) {
            System.out.println("Erro: " + e.getMessage());
        }

        //Verificar se a Dispensadora mantém o controle correto das cédulas após mais de um saque.
        try{
            for(int i =0; i < 9; i++){
                dispensadora.dispensar(150);
            }
            for(int i =0; i <= 9; i++){
                dispensadora.dispensar(5);
            }
            int[] cedulasDisponiveisEsperadas = {0,0,10,10,0,10};
            assertArrayEquals(cedulasDisponiveisEsperadas, dispensadora.getCedulasDisponiveis(),"valores diferentes");
        }catch (NaoEhPossivelDispensarValorException e) {
            System.out.println("Erro: " + e.getMessage());
        }

    }







}