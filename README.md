<h1>email-distribution-program</h1>
<h2>
	Описание проекта:
</h2>
<p>
	Скрипт рассылает подготовленное письмо с указанного почтового ящика указанному списку получателей
</p>
<h3>
	Требования:
</h3>
<ul>
	<li>установлен python версии 3.0 и выше</li>
	<li>работа производится в IDE PyCharm</li>
</ul>

<h3>
	Перед началом работы со скриптом нужно:
</h3>
<p>
	-> установить python-dotenv, запустив команду pip install -U python-dotenv в cmd 
</p>
<a href="https://pypi.org/project/python-dotenv/">python-dotenv</a>

<h3>
	Для работы со скриптом нужно:
</h3>
<ol>
	<li>
		создать файл .env и поместить его в папку с проектом
		-> LOGIN=указать в нем почтовый ящик с которого будет производиться рассылка
		-> PASSWORD=password указанного выше почтового ящика
	</li>
	<li>
		в файле my.py
		-> в строке 38 указать через запятую в кавычках адреса получателей
		email_to=['','','']
	</li>
	<li>В PyCharm запустить программу Run -> Run my.py</li>
</ol>
