# Nome do banco de dados e usuário
DB_NAME=
DB_USER=

# Diretório base para backups
BACKUP_ROOT=/backups

# Data e hora para nomeação dos backups
DATE=$(shell date +'%Y/%m')
TIMESTAMP=$(shell date +'%d-%m-%Y_%H-%M-%S')

# Caminho do diretório de backup
BACKUP_DIR=$(BACKUP_ROOT)/$(DATE)

# Nome do arquivo de backup
BACKUP_FILE=$(BACKUP_DIR)/$(TIMESTAMP).sql.gz

# Arquivo de log de restauração
RESTORE_LOG=$(BACKUP_ROOT)/restore.log

# Alvo padrão
all: backup

# Criação do backup
backup:
	@echo "Creating backup directory: $(BACKUP_DIR)"
	mkdir -p $(BACKUP_DIR)
	@echo "Starting backup for database: $(DB_NAME)"
	@if pg_dump -U $(DB_USER) -d $(DB_NAME) | gzip > $(BACKUP_FILE); then \
	    echo "Backup completed successfully: $(BACKUP_FILE)"; \
	else \
	    echo "Backup failed."; \
	    exit 1; \
	fi

# Restauração do banco de dados
restore:
	@if [ -z "$(RESTORE_FILE)" ]; then \
	    echo "Error: Provide the RESTORE_FILE variable when running make."; \
	    echo "Usage: make restore RESTORE_FILE=/path/to/backup.sql.gz"; \
	    exit 1; \
	fi
	@if [ ! -f "$(RESTORE_FILE)" ]; then \
	    echo "Error: The file $(RESTORE_FILE) does not exist."; \
	    exit 1; \
	fi
	@echo "Restoring database: $(DB_NAME) from $(RESTORE_FILE)"
	gunzip -c $(RESTORE_FILE) | psql -U $(DB_USER) $(DB_NAME) 2>> $(RESTORE_LOG)
	@if [ $$? -eq 0 ]; then \
	    echo "Restore completed successfully."; \
	else \
	    echo "Restore failed. Check log at $(RESTORE_LOG)."; \
	    exit 1; \
	fi

# Limpeza de backups antigos (opcional)
clean:
	@echo "Cleaning backups older than 7 days in $(BACKUP_ROOT)"
	find $(BACKUP_ROOT) -type f -mtime +7 -exec rm -v {} \;