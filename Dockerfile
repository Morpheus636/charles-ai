FROM python:3.10-slim

WORKDIR /opt

# Configure user
ARG USER_UID=1000
RUN adduser --shell /bin/sh --system --group --uid "${USER_UID}" default
RUN chown -R default /opt
USER default

# Copy project files
COPY --chown=default:default . .

# Setup poetry
ENV PATH "/home/default/.poetry/bin/:/home/default/.local/bin:$PATH"
RUN pip install poetry

# Install dependencies
RUN poetry install --no-dev

CMD ["poetry", "run", "python", "-m", "src.charles_ai"]
