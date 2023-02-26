life_expectancy_list = []

with open('cse110\week11\life-expectancy.csv', 'r') as health_file:
    for line in health_file:

        clean_line = line.strip()

        health_parts = line.split(",")

        try:
            country = health_parts[0]
            country_code = health_parts[1]
            if isinstance(health_parts[2], int):
                year = int(health_parts[2])
            else:
                year = 0
            
            life_expectancy = float(health_parts[3])
            row = f'{country} {country_code} {year} {life_expectancy}'

            life_expectancy_list.append(life_expectancy)
        except ValueError:
            pass

        
print(f'Min: {min(life_expectancy_list)}. Max: {max(life_expectancy_list)}')

        
        
