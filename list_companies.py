import re, requests, sys

companies = requests.get('https://raw.githubusercontent.com/poteto/hiring-without-whiteboards/master/README.md').text.split('\n')
del companies[:companies.index('## A - C')]
del companies[companies.index('## Also see:'):]
companies = list(filter(lambda item: any(re.search(r'\b' + keyword + r'\b', item, flags=re.IGNORECASE) for keyword in sys.argv[1:]), companies))
companies = list(map(lambda item: item[item.index('[') + 1:item.index(']')], companies))
print(*companies, sep='\n')
