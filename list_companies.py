import requests, sys

companies = requests.get('https://raw.githubusercontent.com/poteto/hiring-without-whiteboards/master/README.md').text.split('\n')
del companies[:companies.index('## A - C')]
del companies[companies.index('## Also see:'):]
companies = list(filter(lambda item: any(keyword.lower() in item.lower() for keyword in sys.argv[1:]), companies))
companies = list(map(lambda item: item[item.index('[')+1:item.index(']')], companies))
print(*companies, sep='\n')
