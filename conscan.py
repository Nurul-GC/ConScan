# ******************************************************************************
#  Direitos Autorais (c) 2019-2021 Nurul GC                                    *
#                                                                              *
#  Jovem Programador                                                           *
#  Estudante de Engenharia de Telecomunicações                                 *
#  Tecnologia de Informação e de Medicina.                                     *
#  Foco Fé Força Paciência                                                     *
#  Allah no Comando.                                                           *
# ******************************************************************************

from datetime import datetime
from time import sleep
from platform import system
from socket import gaierror, error
import socket
import subprocess
import sys

if __name__ == '__main__':
    try:
        listaPortas = []
        print("""
    *****************************************************************************
    **  *********                       *********                              **
    ** **       **  *******  ****   ** **           ********  *****  ****   ** **
    ** **          **     ** ** **  **  *********  **        **   ** ** **  ** **
    ** **       ** **     ** **  ** **          ** **        ******* **  ** ** **
    **  *********   *******  **   ****  *********   ******** **   ** **   **** **
    *****************************************************************************
    **      [i] - SIMPLES SCRIPT-PROGRAMA QUE VERIFICA AS PORTAS               **
    **            DISPONÍVEIS PARA ESTABELECER A LIGAÇÃO A UM SERVIDOR!        **
    *****************************************************************************  
    """)
        servidorReservado = input("\nDigite o endereço de um Servidor Remoto para scanear:\n> ")

        # revertendo o endereço URL para IP
        servidorReservadoIP = socket.gethostbyname(servidorReservado)

        # registrando o tempo inicio
        inicio = datetime.now()

        print(f"""\n***Por favor aguarde enquanto processo as portas para conectar com Servidor de - ({servidorReservadoIP})***""")

        # criando o loop que verifica cada uma das 65535
        # possiveis portas para conexão
        for porta in range(1, 10):
            # iniciando a instância que será usada para as ligações
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # definindo o timeout da conexão
            sock.settimeout(120)

            # testando a ligação com o endereço IP e as possiveis portas
            resultado = sock.connect_ex((servidorReservadoIP, porta))

            # 302 -> found
            # 200 -> OK
            if resultado == 200:
                listaPortas.append(porta)
            sleep(0.5)
            sock.close()
    except KeyboardInterrupt:
        # capturando o encerramento do programa pelo usuario
        print('[!] - Processo Abortado pelo usuario..')
        sys.exit()
    except gaierror as e:
        # capturando a invalidação do endereço
        print(f"[!] - {e}..")
        sys.exit()
    except error as e:
        # capturando o erro de ligação
        print(f"[!] - {e}..")
        sys.exit()

    # registrando tempo final
    fim = datetime.now()

    # registrando o tempo total da operação
    total = fim-inicio

    print(f'\nEscaneamento Concluído em: {total}\nForam encontradas {len(listaPortas)} portas disponiveis..')
    print(f"""
****************************************************
*   [1] - IMPRIMIR A LISTA DE PORTAS DISPONÍVEIS   *
*   [s] - TERMINAR PROGRAMA                        *
****************************************************""")
    while True:
        r = input('\n> ')
        if r == '1':
            pass
        elif r == 's':
            pass
        else:
            pass
