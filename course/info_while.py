# input()
name = input("your name is : ")
print(f"good afternoon, {name}")

age = int(input("how old are you? :"))
age_older = age+1
print(f"you will be {age_older}-years old next year, then")

# move elements from a list to another
toybox1 = ['woody','buzz','alan']
toybox2 = []
while toybox1:
    popped_toy = toybox1.pop()
    toybox2.append(popped_toy)
print(toybox1, toybox2)

# remove specific elements from a list
toybox1 = ['woody','buzz','alan','alan','alan','alan','jessie']
while 'alan' in toybox1:
    toybox1.remove('alan')
print(toybox1)

# create a dictionary based on users' inputs
survey=[]
add_surveyee = True
while add_surveyee:
    survey_item={}
    name_response = input("your name is : ")
    survey_item['name'] = name_response
    toy_response = input("name of your toy : ")
    survey_item['toy'] = toy_response
    color_response = input("its color is : ")
    survey_item['color'] = color_response
    survey.append(survey_item)
    add = input("wanna add a surveyee(y/n)?")
    if(add=='n'): add_surveyee = False
print(survey)


