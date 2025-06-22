# Backup e Restauração de Dados em Banco PostgreSQL

Um Makefile foi projetado para gerenciar backups e restaurações de um banco de dados PostgreSQL.

O resto deste README conterá uma explicação detalhada de cada parte:

---

## **1. Variáveis**

As variáveis são usadas para armazenar valores reutilizáveis no Makefile, tornando-o mais organizado e fácil de modificar.

- **`DB_NAME=YOUR_DB_NAME`**:
  - Define o nome do banco de dados para o backup ou restauração, onde você deve trocar `YOUR_DB_NAME` pelo nome do seu banco de dados.

- **`DB_USER=YOUR_USER_NAME`**:
  - Especifica o nome do usuário do banco de dados PostgreSQL, onde você deve trocar `YOUR_USER_NAME` pelo seu nome de usuário com acesso administrador ao banco de dados.

- **`BACKUP_ROOT=/backups`**:
  - Define o diretório raiz onde os backups serão armazenados, onde por padrão será `backups` mas pode ser alterado de acordo com sua vontade.

- **`DATE=$(shell date +'%Y/%m')`**:
  - Usa o comando `date` para criar uma string com o ano e o mês atuais no formato `YYYY/MM`.

- **`TIMESTAMP=$(shell date +'%d-%m-%Y_%H-%M-%S')`**:
  - Gera um carimbo de data e hora no formato `DD-MM-YYYY_HH-MM-SS`.

- **`BACKUP_DIR=$(BACKUP_ROOT)/$(DATE)`**:
  - Define o caminho do diretório de backup, incluindo ano e mês.

- **`BACKUP_FILE=$(BACKUP_DIR)/$(TIMESTAMP).sql.gz`**:
  - Especifica o nome completo do arquivo de backup.

- **`RESTORE_LOG=$(BACKUP_ROOT)/restore.log`**:
  - Define o caminho para o arquivo de log de restauração.

---

## **2. Alvo Padrão**

- **`all: backup`**:
  - Define `backup` como o alvo padrão que será executado caso nenhum outro alvo seja especificado.

---

## **3. Alvo `backup`**

Este alvo cria backups do banco de dados executando os passos a baixo.

1. **`@echo`**:
   - Exibe mensagens para o usuário explicando as etapas que estão sendo executadas.

2. **`mkdir -p $(BACKUP_DIR)`**:
   - Cria o diretório de backup, incluindo todos os diretórios pai necessários.

3. **`pg_dump -U $(DB_USER) -d $(DB_NAME) | gzip > $(BACKUP_FILE)`**:
   - Usa o comando `pg_dump` do Postgres para exportar o banco de dados e `gzip` para comprimir o resultado, armazenando-o no arquivo de backup.

4. **Estrutura condicional**:
   - Verifica se o comando foi bem-sucedido:
     - **`echo "Backup completed successfully: $(BACKUP_FILE)"`** se for bem-sucedido.
     - **`echo "Backup failed."` e `exit 1`** se falhar.

---

## **4. Alvo `restore`**

Este alvo restaura um backup existente.

1. **Verificação de variáveis**:
   - **`[ -z "$(RESTORE_FILE)" ]`**: Garante que o usuário forneça o caminho do arquivo de backup a ser restaurado.
   - **Mensagem de erro e exemplo de uso**:

     ```bash
     echo "Error: Provide the RESTORE_FILE variable when running make."
     echo "Usage: make restore RESTORE_FILE=/path/to/backup.sql.gz"
     ```

2. **Verificação de existência do arquivo**:
   - **`[ ! -f "$(RESTORE_FILE)" ]`**:
     - Garante que o arquivo fornecido existe.

3. **Comando de restauração**:
   - **`gunzip -c $(RESTORE_FILE) | psql -U $(DB_USER) $(DB_NAME) 2>> $(RESTORE_LOG)`**:
     - Descomprime o arquivo de backup e o passa diretamente para o comando `psql`, restaurando o banco de dados.
     - Redireciona mensagens de erro para um arquivo de log.

4. **Estrutura condicional**:
   - Verifica se a restauração foi bem-sucedida:
     - **`echo "Restore completed successfully."`** se bem-sucedida.
     - **`echo "Restore failed. Check log at $(RESTORE_LOG)."`** se falhar.

---

## **5. Alvo `clean`**

Este alvo remove backups antigos.

1. **Mensagem informativa**:
   - **`echo "Cleaning backups older than 7 days in $(BACKUP_ROOT)"`**: Informa o usuário sobre a limpeza.

2. **Comando de limpeza**:
   - **`find $(BACKUP_ROOT) -type f -mtime +7 -exec rm -v {} \;`**:
     - Localiza e remove arquivos no diretório `$(BACKUP_ROOT)` que são mais antigos que 7 dias.

---

### **Fluxo do Makefile**

1. **Backup**:
   - Execute:

     ```bash
     make backup
     ```

   - Resultado:
     - Um arquivo de backup é criado em `/backups/YYYY/MM`.

2. **Restauração**:
   - Execute:

     ```bash
     make restore RESTORE_FILE=/path/to/backup.sql.gz
     ```

   - Resultado:
     - Restaura o banco de dados do arquivo especificado.

3. **Limpeza**:
   - Execute:

     ```bash
     make clean
     ```

   - Resultado:
     - Remove backups antigos com mais de 7 dias.
