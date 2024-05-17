from num2words import num2words
from transliterate import translit

text = """Ladies and gentlemen, I'm 78 years old and I finally got 15 minutes of 
fame once in a lifetime and I guess that this is mine. 
People have also told me to make these next few minutes escruciatingly embarrassing and to take vengeance of my enemies. 
Neither will happen.

More than 3 years ago I moved to Novo-Novsk, but worked on new Magnetic Storage for last 40. When I was 8...\n"""

print(translit(text, 'ru'))

num_1 = num2words(78, to='cardinal', lang='en')
rez_1 = translit(num_1, 'ru')

num_2 = num2words(15, to='cardinal', lang='en')
rez_2 = translit(num_2, 'ru')

num_3 = num2words(3, to='cardinal', lang='en')
rez_3 = translit(num_3, 'ru')

num_4 = num2words(40, to='cardinal', lang='en')
rez_4 = translit(num_4, 'ru')

num_5 = num2words(8, to='cardinal', lang='en')
rez_5 = translit(num_5, 'ru')

print(f"78 - {rez_1}\n15 - {rez_2}\n3 - {rez_3}\n40 - {rez_4}\n8 - {rez_5}")
