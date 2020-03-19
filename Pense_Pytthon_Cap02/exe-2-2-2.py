preco_do_livro = 24.95
preco_para_livraria = preco_do_livro * 0.6
preco_envio_1_exemplar = 3
preco_envio_demais_exemplar = 0.75
# Custo de 60 copias
custo_1_copia = preco_para_livraria + preco_envio_1_exemplar
custo_demais_copias = (preco_para_livraria * preco_envio_demais_exemplar) * 59

# custo total
custo_total = custo_1_copia + custo_demais_copias
print("Custo total: R${:.2f}".format(custo_total))

# Total