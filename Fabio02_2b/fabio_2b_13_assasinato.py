#TODO: criar variavel S para armazenar qtd de respostas positivas
def main():

    p1 = str(input("Telefonou para a vítima ?: ")).lower()
    p2 = str(input("Esteve no local do crime ?: ")).lower()
    p3 = str(input("Mora perto da vítima ?: ")).lower()
    p4 = str(input("Devia para a vítima ?: ")).lower()
    p5 = str(input("Já trabalhou com a vítima ?: ")).lower()

    sim = 0
    if p1 == 's':
        sim += 1
    if p2 == 's':
        sim += 1
    if p3 == 's':
        sim += 1
    if p4 == 's':
        sim += 1
    if p5 == 's':
        sim += 1

    if sim == 2:
        status = 'suspeita'
    elif sim == 3 or sim == 4:
        status = 'cumplice'
    elif sim == 5:
        status = 'culpado'
    else:
        status = 'inocente'
        
    print(f'Status = {status}')
    

main()
