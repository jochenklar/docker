FROM node:24-trixie

RUN apt-get update && apt-get install -y \
    curl \
    fd-find \
    git \
    ripgrep \
    && rm -rf /var/lib/apt/lists/*

RUN npm install -g @anthropic-ai/claude-code

# Run as non-root
RUN useradd -m -s /bin/bash claude
USER claude
WORKDIR /workspace

CMD ["claude", "--dangerously-skip-permissions"]
