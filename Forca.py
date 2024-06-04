# Entrada
palavras_forca = ['gafanhoto', 'algoritmo', 'programacao']

NUM_MAX_ERRO = 5 # Número máximo de tentativas

def escolha_palavra(): # Escolher uma palavra da lista de palavras
    return palavras_forca[0]

def mostre_palavra_terminal(palavra, caracteres_usados): # Como a palavra aparecerá no terminal "---...-"
    palavra_ao_usuario = ''
    for letra in palavra:
        if letra in caracteres_usados:
            palavra_ao_usuario += letra
        else:
            palavra_ao_usuario += '-'
    print(f'Palavra: {palavra_ao_usuario}')

def mostre_tentativas_restantes(num_tent_rest):
    print(f'Número de tentativas restantes: {num_tent_rest}')

def mostre_estado_atual(palavra, caracteres_usados, num_tent_rest): # Estado atual
        mostre_palavra_terminal(palavra, caracteres_usados)
        print(f'Letras já utilizadas: {caracteres_usados}')
        mostre_tentativas_restantes(num_tent_rest)

def mensagem_de_vitoria():
    print('Você ganhou!')
    print(f'A palavra era: {palavra}')

def mensagem_de_derrota():
    print('Você perdeu!')
    print(f'A palavra era: {palavra}')

def soletrar_palavra(): ###
     for letra in palavra:
          palavra_soletrada = palavra_soletrada + [letra]
          
     
palavra = escolha_palavra()
caracteres_usados = []
num_erro = 0
num_tent_rest = NUM_MAX_ERRO - num_erro



while num_erro < NUM_MAX_ERRO:
    mostre_estado_atual(palavra, caracteres_usados, num_tent_rest)
    tent_letra=input('Selecione uma letra: ')

    if tent_letra not in palavra:
         num_erro += 1
         caracteres_usados = caracteres_usados + [tent_letra]

    if tent_letra in palavra:
        caracteres_usados = caracteres_usados + [tent_letra]
        if set(palavra).issubset(caracteres_usados):
            mensagem_de_vitoria()
            exit()
    
    elif num_erro == NUM_MAX_ERRO:
         mensagem_de_derrota()
         exit()