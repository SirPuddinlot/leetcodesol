def min_time_distributed(developmenttime, integrationtime):
  #given two lists, one called dev where there are n contributers and int where only 1 contributor
  #find optimal placements so that is it the minimum time for all persons
  critical_indices = []
  for i in range(len(developmenttime)):
    if integrationtime[i] <= developmenttime[i]:
      critical_indices.append(i)
  print(critical_indices)
  int_sum = sum(integrationtime[i] for i in critical_indices)
  for i in critical_indices:
      if developmenttime[i] >= int_sum:
          break
      else:
        int_sum -= integrationtime[i]
  return int_sum



def no_adjacent_pair(words):
  #given a list of words, keep track of # of substitutions made so that no adjacent element is the same
  #only letters, no #
  def count_substitutions(word):
      substitutions = 0
      word_list = list(word)
      length = len(word_list)
      i = 0
      while i < length - 1:
          if word_list[i] == word_list[i + 1]:
              substitutions += 1
              new_char = '1' 
              word_list[i + 1] = new_char
          i += 1
      return substitutions
  if words is None:
      return []
  return [count_substitutions(word) for word in words]
