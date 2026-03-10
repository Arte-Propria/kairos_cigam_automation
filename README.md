# ⏱️ Integração Automática de Batimentos de Ponto (Kairos → CIGAM)

## 📌 Sobre o Projeto

Este projeto tem como objetivo **automatizar o processo de extração e integração dos batimentos de ponto dos colaboradores** entre o sistema de controle de ponto **Kairos** e o **ERP CIGAM**.

Atualmente, o processo é realizado manualmente por um responsável, que precisa acessar o sistema Kairos, gerar um arquivo de batimentos dentro de um período específico e disponibilizá-lo em uma pasta de integração utilizada pelo CIGAM.  

Este projeto busca **eliminar tarefas manuais, reduzir erros operacionais e acelerar a integração das informações de ponto** dentro do ERP.

A automação foi desenvolvida em **Python**, utilizando requisições HTTP para comunicação com a **API REST do Kairos**, permitindo que o processo seja executado automaticamente.

---

# 🚀 Objetivo da Automação

Automatizar as seguintes etapas do processo:

1️⃣ Conectar-se à **API do sistema de ponto Kairos**  
2️⃣ Realizar chamadas aos endpoints necessários para obter dados de batimentos  
3️⃣ Gerar o arquivo no **mesmo layout utilizado pelo Kairos**  
4️⃣ Salvar automaticamente o arquivo na **pasta de integração do CIGAM**  
5️⃣ Permitir que o **CIGAM processe os batimentos automaticamente**

Com isso, o processo passa a funcionar de forma **mais rápida, confiável e escalável**.

---

# 🧠 Como Funciona o Processo

### 📥 1. Origem dos Dados

Os dados de batimentos são obtidos através da **API REST do Kairos**, que disponibiliza endpoints para consulta de informações relacionadas ao controle de ponto.

A API utiliza:

- **Método HTTP POST**
- **Headers de autenticação**
- **Endpoints específicos para consulta de dados**

---

### 📄 2. Estrutura do Arquivo Gerado

O Kairos gera um arquivo **TXT com layout fixo**, onde cada linha representa uma informação específica.

O arquivo possui a seguinte estrutura:

#### 🔹 Cabeçalho
Contém informações da empresa e do período de referência do arquivo.

Exemplo simplificado:

0000000001[identificação empresa][dados empresa][período do arquivo][data geração]


---

#### 🔹 Linhas de Batimento

Cada linha representa **um registro de batimento de ponto de um colaborador**.

Exemplo:

00105699472026-01-05T07:49:00-030050306919877 2026-01-05T07:49:06-03000503fc3000acc9ba4f065c6a25dab6d0260ec1b3a6e6dfd7f576d69cc86fe3a50c5


Esses registros seguem um **formato concatenado padronizado** contendo:

| Campo | Descrição |
|-----|-----|
| Código inicial | Código do registro |
| Data/Hora | Data e hora do batimento |
| Timezone | Informação de fuso horário |
| CPF | Identificação do colaborador |
| Data/Hora completa | Data/hora com precisão de segundos |
| Código intermediário | Código de identificação do evento |
| Hash | Código único do registro |

---

#### 🔹 Rodapé

Indica o **total de registros presentes no arquivo**.

Exemplo:

9999999990000000000000000000000000000000000000000000000000000229


---

# ⚙️ Tecnologias Utilizadas

Este projeto foi desenvolvido utilizando as seguintes tecnologias:

- 🐍 **Python**
- 🌐 **API REST**
- 📦 `requests` para chamadas HTTP
- 📄 Manipulação de arquivos `.txt`
- 📁 Integração com diretórios de rede

---

# 🏗️ Estrutura do Projeto

Estrutura inicial do projeto:

```
kairos-cigam-integration
│
├── src
│ ├── api
│ │ └── kairos_client.py
│ │
│ ├── services
│ │ └── batimentos_service.py
│ │
│ ├── utils
│ │ └── file_generator.py
│
├── config
│ └── settings.py
│
├── logs
│
├── main.py
│
├── requirements.txt
│
├── .gitignore
│
└── README.md
```


---

# 🔄 Fluxo da Automação

O fluxo de funcionamento da automação será:
```
Kairos API
│
│
▼
Python Script
│
│
▼
Geração do arquivo TXT
│
│
▼
Pasta de Integração
│
│
▼
CIGAM
```


---

# 📊 Benefícios da Automação

Implementar essa automação traz diversas vantagens:

✔ Redução de trabalho manual  
✔ Menor risco de erro humano  
✔ Padronização do processo  
✔ Integração mais rápida entre sistemas  
✔ Escalabilidade para novas funcionalidades  

---

# 🔮 Evoluções Futuras do Projeto

Após a primeira entrega, o projeto poderá evoluir para incluir novas funcionalidades:

- 🔎 Validação automática de batimentos inconsistentes
- 📊 Relatórios de falhas de integração
- 📧 Notificações automáticas
- 🔁 Reprocessamento automático de registros não integrados
- 📡 Integração direta com o CIGAM via API (caso disponível)

---

# 🔐 Segurança

Informações sensíveis como:

- Chaves de API
- Identificadores de empresa
- Credenciais
- Endpoints privados

**não são armazenadas diretamente no código**, sendo carregadas através de variáveis de ambiente ou arquivos de configuração ignorados pelo Git.

---

# 🧑‍💻 Autor

Projeto desenvolvido para automatizar processos internos de integração de sistemas corporativos.

---

# 💡 Filosofia do Projeto

Automação não é apenas sobre tecnologia — é sobre **liberar pessoas para fazer trabalhos mais inteligentes**.

> *“A melhor maneira de prever o futuro é criá-lo.”*  
> — **Alan Kay**