import csv


rows=[]

with open("final_data.csv","r") as f:
    csvreader= csv.reader(f)
    for row in csvreader: #reading row by row
      rows.append(row)

headers= rows[0]
planet_data_rows=rows[1:] #from first to end row

planet_mass = [] 
planet_radius=[]
temp_planet_data_rows = list(planet_data_rows)

for planet_data in temp_planet_data_rows:
      planet_mass.append(planet_data[2])
      planet_radius.append(planet_data[3])

#converting mass into kg
for value in planet_mass:
    value * int(1.989)

# print(list(planet_mass))

#converting radius into meters
for val in planet_radius:
    val * int(6.957)

# print(list(planet_radius))

planet_gravity=[]
gravity = int(6.67*0.00000000001) * (planet_mass) / (planet_radius)*(planet_radius)
planet_gravity.append(gravity)

print(f"Planet gravity is: {planet_gravity}")






