nome = input()
salário = float(input())
vt_venda = float(input())
comissão = 15/100

salário_final = salário + vt_venda*comissão

print(f'TOTAL = R$ {salário_final:.2f}')