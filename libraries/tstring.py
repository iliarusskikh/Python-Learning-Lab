
##1 method
#name: str = 'Bob'
#age: int = 30
#
#message: str = f'My name is {name} and I am {age} years old.'
#print(message)
#
##2 method
#message2 = 'My name is {} and I am {} years old.'.format(name,age)
#
##3 method
#
#from string import Template
#
#template = Template('Hello, $name! U are $age')
#message = template.substitute(name='Bob', age=100)


# new method - t string
from string.templatelib import Template, convert

#this is a template object
template = t'Hello, {name}! You are {age} years old.'
print(template.string)#excludes { name} and {age} - interpolation slots
print(template.interpolations) #possible interpolations, '' 'bob' none
print(template.values) #see Bob and 30 , values if initialised

def build_template(t_string: Template) -> str:
    values: list[str] = []
    
    for i in t_string:
        if isinstance(i, str):
            values.append(i)
        else:
#            val: str = convert(i.value, i.conversion)
#            if i.format_spec:
#                val = format(val, i.format_spec)
            values.append(i.value)#val
            
            
    return ''.join(values) #recreate string from template
    
build_template(template)
print(template)

