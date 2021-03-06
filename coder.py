def morze(text):
	t = text.upper()

	toMorze = {'А':'•-',   'Б': '-•••',   'В': '•--',   'Г': '--•',
			   'Д': '-••',   'Е': '•',   'Ж': '•••-',   'З': '--••',
			   'И': '••',   'Й': '•---',   'К': '-•-',   'Л': '•-••',
			   'М': '--',   'Н': '-•',   'О': '---',   'П': '•--•',
			   'Р': '•-•',   'С': '•••',   'Т': '-',   'У': '••-',
			   'Ф': '••-•',   'Х': '••••',   'Ц': '-•-•',    'Ч': '---•',
			   'Ш': '----',   'Щ': '--•-',   'Ъ': '•--•-•',   'Ы': '-•--',
			   'Ь': '-••-',   'Э': '••-••',   'Ю': '••--',   'Я': '•-•-',
			   'Ё': '•',

			   'A': '•-',   'B': '-•••',   'C': '-•-•',    'D': '-••',
			   'E': '•',   'F': '••-•',   'G': '--•',       'H': '••••',      
			   'J': '•---',  'K': '-•-',       'L': '•-••',   'M': '--',            
			   'O': '---',   'P': '•--•',      'Q': '--•-',      'R': '•-•',
			   'S': '•••',   'T': '-',         'U': '••-',   'V': '•••-',   
			   'W': '•--',   'X': '-••-',   'Y': '-•--',      'Z': '--••',
			   'I': '••',    'N': '-•', 
			   
			   '0': '-----',   '1': '•----',  
			   '2': '••---',   '3': '•••--',  
			   '4': '••••-',   '5': '•••••',
			   '6': '-••••',   '7': '--•••',  
			   '8': '---••',   '9': '----•',

			   '•': '••••••',
			   ',': '•-•-•-',
			   '!': '--••--',
			   '?': '••--••',
			   "'": '•----•',
			   '"': '•-••-•',
			   ';': '-•-•-•',
			   ':': '---•••',
			   '-': '-••••-',
			   '+': '•-•-•',
			   '=': '-•••-',
			   '_': '••--•-',
			   '/': '-••-•',
			   '(': '-•--•',
			   ')': '-•--•-',
			   '&': '•-•••',
			   '$': '•••-••-',
			   '@': '•--•-•',
			   'End contact': '••-•-',

			   ' ': ' '}

	r = ''
	for i in range(len(t)):
		r += toMorze[t[i]]
	r += " " + toMorze["End contact"]
	return r