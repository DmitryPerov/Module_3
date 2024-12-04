def calculate_structure_sum(data_structure_to_calculate):
  #global count
  count = 0
  if isinstance(data_structure_to_calculate,dict):
      elements = list(data_structure_to_calculate.items()) #, data_structure_to_calculate.values()
  elif isinstance(data_structure_to_calculate,(list, tuple, set)):
      elements = data_structure_to_calculate
  else:
        # если это не список, не кортеж и не словарь, обернем в список для обработки
      elements = [data_structure_to_calculate]
  for element in elements:
      if isinstance(element,(int, float)):
        count += element
      elif isinstance(element, str):
        count +=len(element)
      elif isinstance(element,(list, tuple, dict, set)):
          count += calculate_structure_sum(element)  # рекурсивный вызов
          # другие типы данных игнорируем
  return count

#count = 0
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)

print(result)

