import requests
import bs4

root_url = 'http://143.107.183.175:13180'
action_url = root_url + '/normalize'


class Normalizador(object):
	def __init__(self):
		None
	
	def envia_texto(self, tarefa, formato, conteudo):
		if formato == 1:
			campo = 'input_text'
		if formato == 2:
			campo = 'input_file'
		payload = {'task_norm': tarefa, 'input_type': formato, campo: conteudo}
		return requests.post(action_url, data=payload)
	
	def recebe_texto(self, tarefa, formato, conteudo):
		soup = bs4.BeautifulSoup(self.envia_texto(tarefa, formato, conteudo).text, "html.parser")
		return soup.get_text().strip('\n').split('\n\n')[1].split(':', 1)[1]
