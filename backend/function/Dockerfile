FROM ghcr.io/astral-sh/uv:0.5.21 AS uv

# First, bundle the dependencies into the task root.
FROM public.ecr.aws/lambda/python:3.12 AS builder

# Set working directory
WORKDIR /app

# Enable bytecode compilation, to improve cold-start performance.
ENV UV_COMPILE_BYTECODE=1

# Disable installer metadata, to create a deterministic layer.
ENV UV_NO_INSTALLER_METADATA=1

# Enable copy mode to support bind mount caching.
ENV UV_LINK_MODE=copy

# Disable Python binary downloads
ENV UV_PYTHON_DOWNLOADS=never

# Bundle the dependencies into the Lambda task root
ENV UV_LOG=debug 
ENV RUST_BACKTRACE=full
COPY pyproject.toml uv.lock ./
RUN --mount=from=uv,source=/uv,target=/bin/uv \
    --mount=type=cache,target=/root/.cache/uv \
    uv export --frozen --no-emit-workspace --no-dev -o requirements.txt && \
    uv pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

FROM public.ecr.aws/lambda/python:3.12

# Copy the runtime dependencies from the builder stage.
COPY --from=builder ${LAMBDA_TASK_ROOT} ${LAMBDA_TASK_ROOT}

# Copy the application code.
COPY . ${LAMBDA_TASK_ROOT}
