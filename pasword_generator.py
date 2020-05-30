import random, string 
length = int(input('introduce el tamaño de la contraseña:'))
letters = string.ascii_letters
nums = string.digit
chars = letters + nums +  '!@#$%&^/()=?¿ª'
rnd = random.SystemRandom()
print ('' .join(rnd.choice(chars) for i in range(length)))
