# 1ª Avaliação — Estrutura de Dados

Projeto desenvolvido para a **1ª Avaliação da disciplina de Estrutura de Dados**, do curso de Análise e Desenvolvimento de Sistemas.

A atividade teve como objetivo analisar um projeto Django fornecido pelo professor, identificar **8 erros intencionais**, explicar os problemas encontrados e realizar as correções necessárias para que o sistema funcionasse corretamente.

## Integrantes

- **Diovanna Oliveira Betta Costa**
- **Karam Assad**

---

## Sobre o projeto

O projeto representa um sistema escolar desenvolvido com **Python e Django**, contendo models para professores, alunos e aulas, além de configurações de Django Admin, Forms, Views, Templates e URLs.

Durante a avaliação foram encontrados erros distribuídos pelos seguintes arquivos:

- `portal/models.py`
- `portal/views.py`
- `portal/forms.py`
- `portal/admin.py`
- `portal/urls.py`
- `sistema/urls.py`
- `sistema/settings.py`

Ao todo, foram identificados e corrigidos os **8 erros solicitados na atividade**.

---

# Correções realizadas

## 1. Importação de `timezone`

**Arquivo:** `portal/models.py`

### Problema encontrado

O código utilizava `timezone.now` nos campos de data e hora dos Models, mas o `timezone` não havia sido importado.

### Correção

Foi adicionada a importação:

```python
from django.utils import timezone
```

Com isso, os campos que utilizam:

```python
default=timezone.now
```

passaram a funcionar corretamente.

---

## 2. Campo `matricula` definido como número inteiro

**Arquivo:** `portal/models.py`

### Problema encontrado

O campo `matricula` do Model `Aluno` estava definido como:

```python
matricula = models.IntegerField()
```

A matrícula funciona como um identificador e não como um valor utilizado para cálculos.

### Correção

O campo foi alterado para:

```python
matricula = models.CharField(max_length=10)
```

Dessa forma, a matrícula passa a ser armazenada como texto.

---

## 3. Caminho incorreto do Template

**Arquivo:** `portal/views.py`

### Problema encontrado

A View `index` tentava carregar o Template utilizando:

```python
'templates/portal/index.html'
```

Como o Django já procura os arquivos dentro da pasta `templates`, esse caminho estava incorreto.

### Correção

O caminho foi ajustado para:

```python
'portal/index.html'
```

A View passou então a localizar corretamente o arquivo existente em:

```text
portal/templates/portal/index.html
```

---

## 4. Importação incorreta do Model no Form

**Arquivo:** `portal/forms.py`

### Problema encontrado

O Model `Professor` estava sendo importado através de:

```python
from models import Professor
```

Porém, o Model está localizado dentro do app `portal`.

### Correção

A importação foi alterada para:

```python
from portal.models import Professor
```

Com isso, o `ProfessorForm`, criado através de `forms.ModelForm`, passou a reconhecer corretamente o Model utilizado.

---

## 5. Campo inexistente no Django Admin

**Arquivo:** `portal/admin.py`

### Problema encontrado

Na configuração do `ProfessorAdmin`, o `list_display` utilizava o campo:

```python
'especialidade'
```

Esse campo não existe no Model `Professor`.

O campo existente no Model é:

```python
disciplina
```

### Correção

O `list_display` foi ajustado para utilizar:

```python
list_display = ('id', 'nome', 'email', 'telefone', 'disciplina', 'ativo',)
```

Com isso, o cadastro de professores passou a ser exibido corretamente no Django Admin.

---

## 6. Rota de cadastro sem uma View correspondente

**Arquivo:** `portal/urls.py`

### Problema encontrado

A rota:

```python
path('cadastro/', views.cadastro)
```

fazia referência à View `cadastro`, porém essa View não existia no projeto.

### Correção

Foi criada a View correspondente em `portal/views.py`:

```python
def cadastro(request):
    return render(request, 'cadastro.html')
```

A rota foi mantida em `portal/urls.py`:

```python
path('cadastro/', views.cadastro, name='cadastro')
```

Também foi criado o Template utilizado pela View para que a rota pudesse ser carregada corretamente.

---

## 7. Problema no roteamento principal do projeto

**Arquivo:** `sistema/urls.py`

### Problema encontrado

O arquivo possuía uma definição de rota escrita em linguagem natural:

```python
path('cadastro/', preciso mostrar a página cadastro.html),
```

Esse trecho não corresponde à sintaxe Python/Django e impedia a execução do projeto.

Além disso, as URLs existentes no app `portal` precisavam ser ligadas ao arquivo principal de URLs.

### Correção

Foi utilizado o `include()`:

```python
from django.urls import path, include
```

E as URLs do app `portal` foram incluídas através de:

```python
path('', include('portal.urls')),
```

Assim, o projeto principal passou a reconhecer as rotas definidas em `portal/urls.py`.

---

## 8. App `portal` não registrado no projeto

**Arquivo:** `sistema/settings.py`

### Problema encontrado

O app `portal` não estava cadastrado em `INSTALLED_APPS`.

Sem esse registro, o Django não carregava corretamente os componentes pertencentes ao app.

### Correção

O app foi adicionado:

```python
INSTALLED_APPS = [
    ...
    'portal',
]
```

Após o registro, o Django passou a reconhecer os Models e demais arquivos pertencentes ao app.

---

# Banco de dados

Após as correções relacionadas aos Models e à configuração do app, foram criadas e aplicadas as migrations necessárias.

Foram utilizados os comandos:

```bash
python manage.py makemigrations
python manage.py migrate
```

A migration inicial do app `portal` realiza a criação dos Models:

- `Professor`
- `Aluno`
- `Aula`

---

# Como executar o projeto

## 1. Instalar as dependências

```bash
pip install django pillow
```

## 2. Aplicar as migrations

```bash
python manage.py migrate
```

## 3. Verificar o projeto

```bash
python manage.py check
```

## 4. Iniciar o servidor

```bash
python manage.py runserver
```

Por padrão, o servidor ficará disponível em:

```text
http://127.0.0.1:8000/
```

### Rotas utilizadas durante os testes

```text
http://127.0.0.1:8000/index/
http://127.0.0.1:8000/cadastro/
http://127.0.0.1:8000/admin/
```

---

# Validação final

Após a realização das correções, o projeto foi testado para verificar seu funcionamento.

Foram validados:

- os Models e suas migrations;
- o carregamento do Django Admin;
- o `ProfessorForm`;
- as Views;
- o carregamento dos Templates;
- o roteamento entre `sistema.urls` e `portal.urls`;
- as rotas `/index/` e `/cadastro/`;
- a execução do comando `python manage.py check`.

Após os ajustes, o projeto passou a executar corretamente, com os **8 erros propostos na avaliação identificados e corrigidos**.