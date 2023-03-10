#Life Expectancy Assignment
print('Welcome to the life expectancy file')
print()
print()
#Variables
user_chose = float(input('Enter the year of interest: '))
min_life_exp = 10000
min_name = []
max_life_exp = 0
max_name = []
min_life_year_exp = 10000
min_name_year = ''
max_life_year_exp = 0
max_name_year = ''
general_year = 0
total = 0
count = 0
YEAR = 2
with open ('life-expectancy.csv') as life_file:
#For function
       for file in life_file:
              file = file.strip()
              file = file.split(',')
              entity = file[0]
              code = file[1]
              year = int(file[2])
              life_expentacy = float(file[3])
              #Max life expectancy
              if life_expentacy > max_life_exp:
                     max_life_exp = life_expentacy
                     max_name = entity
                     general_year = year
              #Min life expectancy
              if life_expentacy < min_life_exp:
                     min_life_exp = life_expentacy
                     min_name = entity
                     general_year = year
              #User year
              if year == user_chose:
                     total += life_expentacy
                     count += 1                         
                     if life_expentacy > max_life_year_exp:
                            max_life_year_exp = life_expentacy
                            max_name_year = entity
                     if life_expentacy < min_life_year_exp:
                            min_life_year_exp = life_expentacy
                            min_name_year = entity
                     average = total / count




#Print statements for max and min expectancy
print()

print(f'For the year: {user_chose:.0f}')
print()
print(f'The lowest value for life expectancy was in {min_name_year} with {min_life_year_exp:.2f}')
print(f'The highest value for life expectancy was in {max_name_year} with {max_life_year_exp:.2f}')


print()

print('In general:')
print(f'The lowest value for life expectancy was in {min_name} with {min_life_exp}, in the year 1882')
print(f'The highest value for life expectancy was in {max_name} with {max_life_exp}, in the year 2019')
print(f'The average life expectancy across all countries was {average:.2f}')

#User year max, min, and average life expectancy


         
