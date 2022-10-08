# https://www.beecrowd.com.br/judge/pt/runs/code/30182097
tem_gasto_viagem = int(input())
vel_med_viagem = int(input())

calc_gas = tem_gasto_viagem * (vel_med_viagem / 12)

print("%.3f" %  (calc_gas))
