FROM postgres:17.4-alpine3.21

# Copy the database schema to the container
COPY schema.sql /docker-entrypoint-initdb.d/

# Set the environment variables
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=postgres

# Expose the port
EXPOSE 5432

# Start the database
CMD ["postgres"]