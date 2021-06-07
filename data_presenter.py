open_file = open("CupcakeInvoices.csv")

for line in open_file:
    # print(value)
    line = line.strip()
    values = line.split(',')
    # print(values[2])

open_file.seek(0, 0)

total_per_order = []

for line in open_file:
    line = line.strip()
    values = line.split(',')
    number_of_cupcakes = int(values[3])

    cost_per_cupcake = float(values[4])

    total_per_order.append(number_of_cupcakes * cost_per_cupcake)
    # print(total_per_order)

  
orders_combined = sum(total_per_order)
print(orders_combined)

open_file.seek(0, 0)

for line in open_file:
    line = line.strip()
    values = line.split(',')
    

open_file.close()