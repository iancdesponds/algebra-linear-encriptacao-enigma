from enigma_gubs_ian.myfunctions import *
import numpy as np

permutation = np.random.permutation(26)
id_matrix = np.eye(26)
P = id_matrix[permutation]

permutation2 = np.random.permutation(26)
id_matrix2 = np.eye(26)
E = id_matrix2[permutation2]

# Teste das funções
msg_original = "ENIGMA"
print("Mensagem original:", msg_original)
print("")

one_hot = para_one_hot(msg_original)
print("Para one-hot:\n", one_hot)
string = para_string(one_hot)
print("One-hot para string:", string)
print("")

msg_cifrada = cifrar(msg_original, P)
print("Mensagem cifrada:", msg_cifrada)
msg_decifrada = de_cifrar(msg_cifrada, P)
print("Mensagem decifrada:", msg_decifrada)
print("")

msg_enigmada = enigma(msg_original, P, E)
print("Mensagem enigmada:", msg_enigmada)
msg_de_enigmada = de_enigma(msg_enigmada, P, E)
print("Mensagem de-enigmada:", msg_de_enigmada)
